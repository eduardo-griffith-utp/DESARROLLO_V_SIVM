using System;
using System.Collections.Generic;
using System.IO;
using System.Linq;
using Microsoft.ML;
using Microsoft.ML.Data;
using System.Drawing;
using System.Drawing.Imaging;
using Microsoft.Extensions.Configuration;
using Microsoft.Extensions.Configuration.Json;
using Tensorflow.Keras.Engine;

namespace SimpleImageClassifier
{
    class Program
    {
        // Configuration settings
        private static string _trainingFolder;
        private static string _modelDirectoryPath;
        private static string _modelPath;

        static void Main(string[] args)
        {
            Console.WriteLine("===============================================");
            Console.WriteLine("   DEMO SIMPLE DE CLASIFICACIÓN DE IMÁGENES");
            Console.WriteLine("===============================================");

            // Load configuration from appsettings.json
            LoadConfiguration();

            // Crear carpetas si no existen
            Directory.CreateDirectory(_modelDirectoryPath);
            Directory.CreateDirectory(_trainingFolder);

            _modelPath = Path.Combine(_modelDirectoryPath, "model.zip");

            // Crear MLContext con semilla fija para resultados reproducibles
            MLContext mlContext = new MLContext(seed: 1);

            Console.WriteLine("\n¿Qué deseas hacer?");
            Console.WriteLine("1. Entrenar modelo (requiere carpetas de imágenes por categoría)");
            Console.WriteLine("2. Clasificar una imagen");

            Console.Write("\nSelecciona una opción (1-2): ");
            string option = Console.ReadLine();

            try
            {
                switch (option)
                {
                    case "1":
                        TrainAndSaveModel(mlContext);
                        break;
                    case "2":
                        ClassifyImage(mlContext);
                        break;
                    default:
                        Console.WriteLine("Opción inválida.");
                        break;
                }
            }
            catch (Exception ex)
            {
                Console.WriteLine($"Error: {ex.Message}");
                Console.WriteLine(ex.StackTrace);
            }

            Console.WriteLine("\nPresiona cualquier tecla para salir...");
            Console.ReadKey();
        }

        /// <summary>
        /// Loads configuration from appsettings.json
        /// </summary>
        private static void LoadConfiguration()
        {
            try
            {
                // Get the path of appsettings.json
                string basePath = Directory.GetCurrentDirectory();
                string appsettingsPath = Path.Combine(basePath, "appsettings.json");

                // Check if appsettings.json exists
                if (!File.Exists(appsettingsPath))
                {
                    Console.WriteLine($"Error: No se encontró el archivo appsettings.json en: {appsettingsPath}");
                    Environment.Exit(1);
                }

                // Build configuration
                IConfiguration config = new ConfigurationBuilder()
                    .AddJsonFile(appsettingsPath, optional: false, reloadOnChange: true)
                    .Build();

                // Read settings
                _trainingFolder = config["TrainingFolder"];
                _modelDirectoryPath = config["ModelPath"];

                Console.WriteLine("Configuración cargada correctamente:");
                Console.WriteLine($"- Carpeta de imágenes: {_trainingFolder}");
                Console.WriteLine($"- Ruta del modelo: {_modelDirectoryPath}");

                // Ensure we have valid paths
                if (string.IsNullOrEmpty(_trainingFolder) || string.IsNullOrEmpty(_modelDirectoryPath))
                {
                    throw new InvalidOperationException("Error: Faltan configuraciones en el archivo appsettings.json.");
                }
            }
            catch (Exception ex)
            {
                Console.WriteLine($"Error al cargar la configuración: {ex.Message}");
                Console.WriteLine("Asegúrate de que el archivo appsettings.json existe y tiene el formato correcto.");
                Environment.Exit(1);
            }
        }

        /// <summary>
        /// Método simplificado para entrenar y guardar un modelo de clasificación de imágenes
        /// </summary>
        private static void TrainAndSaveModel(MLContext mlContext)
        {
            Console.WriteLine("\n[ENTRENAMIENTO DEL MODELO]");

            // Comprobar si existen subcarpetas con imágenes
            var categoriesFolders = Directory.GetDirectories(_trainingFolder);
            if (categoriesFolders.Length == 0)
            {
                Console.WriteLine($"Error: No se encontraron subcarpetas con categorías en {_trainingFolder}");
                Console.WriteLine("Debes crear subcarpetas, una para cada categoría, y colocar imágenes dentro.");
                Console.WriteLine("Ejemplo: /assets/images/perros/, /assets/images/gatos/, etc.");
                return;
            }

            // Mostrar información de las categorías encontradas
            Console.WriteLine("\nCategorías encontradas:");
            foreach (var folder in categoriesFolders)
            {
                string categoryName = Path.GetFileName(folder);
                int imageCount = Directory.GetFiles(folder, "*.*", SearchOption.TopDirectoryOnly)
                    .Count(file => file.EndsWith(".jpg") || file.EndsWith(".jpeg") || file.EndsWith(".png"));

                Console.WriteLine($"- {categoryName}: {imageCount} imágenes");
            }

            try
            {
                // Paso 1: Cargar las imágenes y extraer características
                Console.WriteLine("\nCargando y procesando imágenes...");

                List<ImageData> imageDataList = new List<ImageData>();

                foreach (var folder in categoriesFolders)
                {
                    string categoryName = Path.GetFileName(folder);
                    var imageFiles = Directory.GetFiles(folder)
                        .Where(f => f.EndsWith(".jpg") || f.EndsWith(".jpeg") || f.EndsWith(".png"));

                    foreach (var file in imageFiles)
                    {
                        // Extraer características básicas
                        var features = ExtractFeatures(file);

                        imageDataList.Add(new ImageData
                        {
                            ImagePath = file,
                            Label = categoryName,
                            Features = features
                        });
                    }
                }

                if (imageDataList.Count == 0)
                {
                    Console.WriteLine("No se encontraron imágenes válidas para el entrenamiento.");
                    return;
                }

                // Paso 2: Crear IDataView a partir de la lista de datos
                Console.WriteLine($"Se cargaron {imageDataList.Count} imágenes para entrenamiento.");

                IDataView imageData = mlContext.Data.LoadFromEnumerable(imageDataList);

                // Paso 3: Dividir datos en conjuntos de entrenamiento y prueba
                var trainTestData = mlContext.Data.TrainTestSplit(imageData, testFraction: 0.2);

                // Paso 4: Definir pipeline de procesamiento y entrenamiento
                Console.WriteLine("Definiendo pipeline de entrenamiento...");

                var pipeline = mlContext.Transforms.Conversion.MapValueToKey("LabelKey", "Label")
                    .Append(mlContext.MulticlassClassification.Trainers.SdcaMaximumEntropy(
                        labelColumnName: "LabelKey",
                        featureColumnName: "Features"))
                    .Append(mlContext.Transforms.Conversion.MapKeyToValue(
                        "PredictedLabel", "PredictedLabel"));

                // Paso 5: Entrenar el modelo
                Console.WriteLine("Entrenando el modelo...");
                var model = pipeline.Fit(trainTestData.TrainSet);

                // Paso 6: Evaluar el modelo
                Console.WriteLine("Evaluando el modelo...");
                var predictions = model.Transform(trainTestData.TestSet);

                // Evaluar el modelo usando los nombres de columna específicos
                var metrics = mlContext.MulticlassClassification.Evaluate(
                    predictions,
                    labelColumnName: "LabelKey",
                    predictedLabelColumnName: "PredictedLabel");

                Console.WriteLine($"Precisión: {metrics.MicroAccuracy:P2}");

                // Paso 7: Guardar el modelo
                Console.WriteLine($"Guardando el modelo en {_modelPath}");
                mlContext.Model.Save(model, imageData.Schema, _modelPath);

                Console.WriteLine("¡Modelo entrenado y guardado con éxito!");
            }
            catch (Exception ex)
            {
                Console.WriteLine($"Error durante el entrenamiento: {ex.Message}");
                Console.WriteLine(ex.StackTrace);
            }
        }

        /// <summary>
        /// Clasifica una imagen utilizando el modelo entrenado
        /// </summary>
        private static void ClassifyImage(MLContext mlContext)
        {
            Console.WriteLine("\n[CLASIFICACIÓN DE IMAGEN]");

            // Verificar si existe el modelo
            if (!File.Exists(_modelPath))
            {
                Console.WriteLine("Error: No se encontró un modelo entrenado.");
                Console.WriteLine("Primero debes entrenar el modelo (opción 1).");
                return;
            }

            Console.WriteLine("Ingresa la ruta completa de la imagen a clasificar:");
            string imagePath = Console.ReadLine();

            if (!File.Exists(imagePath))
            {
                Console.WriteLine("Error: La imagen no existe. Verifica la ruta.");
                return;
            }

            try
            {
                // Cargar el modelo
                ITransformer model = mlContext.Model.Load(_modelPath, out var modelSchema);

                // Crear motor de predicción
                var predictionEngine = mlContext.Model.CreatePredictionEngine<ImageData, ImagePrediction>(model);

                // Extraer características de la imagen
                var features = ExtractFeatures(imagePath);

                // Mostrar características extraídas
                Console.WriteLine("\nCaracterísticas extraídas:");
                for (int i = 0; i < features.Length; i++)
                {
                    Console.WriteLine($"- Característica {i + 1}: {features[i]:F4}");
                }

                // Preparar datos para predicción
                var inputData = new ImageData
                {
                    ImagePath = imagePath,
                    Label = string.Empty,
                    Features = features
                };

                // Realizar predicción
                Console.WriteLine("\nRealizando predicción...");
                var prediction = predictionEngine.Predict(inputData);

                // Mostrar resultados
                Console.WriteLine("\nResultados de la clasificación:");
                Console.WriteLine($"La imagen fue clasificada como: {prediction.PredictedLabel}");

                // Intentar mostrar puntuación si está disponible
                if (prediction.Score > 0)
                {
                    Console.WriteLine($"Puntuación: {prediction.Score:P2}");
                }
            }
            catch (Exception ex)
            {
                Console.WriteLine($"Error durante la clasificación: {ex.Message}");
                Console.WriteLine(ex.StackTrace);
            }
        }

        /// <summary>
        /// Extrae características básicas de una imagen para su clasificación
        /// </summary>
        private static float[] ExtractFeatures(string imagePath)
        {
            try
            {
                using (var image = Image.FromFile(imagePath))
                {
                    // Características básicas normalizadas
                    float width = image.Width / 1000.0f;
                    float height = image.Height / 1000.0f;
                    float ratio = width / (height > 0 ? height : 1);

                    using (var bitmap = new Bitmap(image))
                    {
                        // Calcular promedios de color
                        float totalR = 0, totalG = 0, totalB = 0;
                        int sampledPixels = 0;
                        int stepSize = Math.Max(1, Math.Min(bitmap.Width, bitmap.Height) / 50);

                        for (int x = 0; x < bitmap.Width; x += stepSize)
                        {
                            for (int y = 0; y < bitmap.Height; y += stepSize)
                            {
                                var pixel = bitmap.GetPixel(x, y);
                                totalR += pixel.R / 255.0f;
                                totalG += pixel.G / 255.0f;
                                totalB += pixel.B / 255.0f;
                                sampledPixels++;
                            }
                        }

                        float avgR = sampledPixels > 0 ? totalR / sampledPixels : 0.5f;
                        float avgG = sampledPixels > 0 ? totalG / sampledPixels : 0.5f;
                        float avgB = sampledPixels > 0 ? totalB / sampledPixels : 0.5f;
                        float brightness = (avgR + avgG + avgB) / 3.0f;
                        float colorDominance = Math.Max(Math.Max(avgR, avgG), avgB);

                        // Vector de características de tamaño fijo (8)
                        return new float[] {
                            width,
                            height,
                            ratio,
                            avgR,
                            avgG,
                            avgB,
                            brightness,
                            colorDominance
                        };
                    }
                }
            }
            catch (Exception ex)
            {
                Console.WriteLine($"Error procesando imagen {imagePath}: {ex.Message}");
                // Devolver valores por defecto
                return new float[] { 0.5f, 0.5f, 1.0f, 0.5f, 0.5f, 0.5f, 0.5f, 0.5f };
            }
        }
    }

    /// <summary>
    /// Clase para representar los datos de una imagen y sus características
    /// </summary>
    public class ImageData
    {
        public string ImagePath { get; set; }
        public string Label { get; set; }

        [VectorType(8)]
        public float[] Features { get; set; }
    }

    /// <summary>
    /// Clase para representar la predicción del modelo
    /// </summary>
    public class ImagePrediction
    {
        [ColumnName("PredictedLabel")]
        public string PredictedLabel { get; set; }

        [ColumnName("Score")]
        public float[] Scores { get; set; }

        public float Score => Scores != null && Scores.Length > 0 ? Scores.Max() : 0;
    }
}