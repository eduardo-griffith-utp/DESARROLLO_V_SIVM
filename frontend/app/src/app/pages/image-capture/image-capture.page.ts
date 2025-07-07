import { Component, OnInit, OnDestroy } from '@angular/core';
import { Camera, CameraResultType, CameraSource } from '@capacitor/camera';
import { NavController } from '@ionic/angular';  // Importa NavController para navegar
import { HttpClient } from '@angular/common/http';
import { ApiService } from 'src/app/core/services/api-service.service';
import { ActivatedRoute } from '@angular/router';
import { Capacitor } from '@capacitor/core';

@Component({
  selector: 'app-image-capture', // Selector actualizado
  templateUrl: './image-capture.page.html', // Referencia al nuevo nombre del HTML
  styleUrls: ['./image-capture.page.scss'], // Referencia al nuevo nombre del SCSS
  standalone: false,
})
export class ImageCapturePage implements OnInit, OnDestroy {
  //imageUrl: string | undefined;
  public imageUrl:  any;
  public imageId: any; 


  isCameraActive = false;
  videoStream: MediaStream | undefined;

    zoomLevel = 1.0;
  
  constructor(private navController: NavController, private activatedRoute: ActivatedRoute, private http: HttpClient, private api: ApiService) {}  // Inyecta NavController

  async ngOnInit() {
    this.startCameraPreview();
  }

  ngOnDestroy() {
    this.stopCameraPreview();
  }

  async startCameraPreview() {
    try {
      const stream = await navigator.mediaDevices.getUserMedia({
        video: { facingMode: 'environment' }, // Cámara trasera
        audio: false,
      });
      this.videoStream = stream;
      this.isCameraActive = true;
      this.attachVideoToElement();
    } catch (error) {
      console.error('Error al acceder a la cámara:', error);
      this.isCameraActive = false;
    }
  }

  stopCameraPreview() {
    if (this.videoStream) {
      this.videoStream.getTracks().forEach((track) => track.stop());
      this.videoStream = undefined;
      this.isCameraActive = false;
    }
  }

  attachVideoToElement() {
    const videoElement = document.querySelector('video');
    if (videoElement && this.videoStream) {
      videoElement.srcObject = this.videoStream;
    }
  }

  async takePicture() {
    try {
      const image = await Camera.getPhoto({
        quality: 90,
        allowEditing: false,
        resultType: CameraResultType.Base64,
        source: CameraSource.Camera,
      });

      this.imageUrl = image.webPath;
      console.log('Imagen capturada:', this.imageUrl);

      // Redirigir a la página de resultados, pasando la URL de la imagen
      this.uploadImage();

    } catch (error) {
      console.error('Error al tomar la foto:', error);
    }
  }







  public async captureNow() {
    console.log('Botón presionado');

    try {
    const image = await Camera.getPhoto({
      quality: 90,
      allowEditing: false,
      resultType: Capacitor.getPlatform() === 'web' ? CameraResultType.DataUrl : CameraResultType.Base64,
      source: Capacitor.getPlatform() === 'web' ? CameraSource.Prompt : CameraSource.Camera
    });

    this.imageUrl = image.webPath;
    const base64Data = Capacitor.getPlatform() === 'web' ? image.dataUrl : image.base64String;

    console.log('Resultado de imagen:', image);

    if (base64Data) {
      try {
      const result = await this.api.postImage(base64Data);
      console.log('Respuesta completa de la API :', result);

      if (result?.id && result?.image) {
        
        this.imageId = `img_${String(result.id).padStart(3, '0')}`;
        // De esta forma el id de la imagen queda guardada de la forma img_001, como esta en la api
        
        //prueba de mock para almacenar la imagen
        sessionStorage.setItem('ImagenCapturada', base64Data);


        console.log('Imagen fue enviada correctamente. ID:', this.imageId);
        this.navController.navigateForward('/recognition-results', {
          queryParams: {
            imageId: this.imageId,
          }
        });
/*
        sessionStorage.setItem('image_id', this.imageId);
        location.href = "/recognition-results";*/


      } else {
        console.warn('La respuesta no contiene los datos esperados:', result);
      }

    } catch (error) {
      console.error('Error al hacer el POST a la API:', error);
    }
  } else {
    console.warn('No se obtuvo la imagen en base64');
  }

      /*if(base64Data){
        let result = await this.api.postImage(base64Data);
        console.log('Respuesta completa de la API (POST):', result);
        const imageResult = result.images?.[0]; //Acceder al objeto en la api


        if (imageResult.status === 'success') {
          this.imageId = imageResult.data?.image_id;
          
          console.log('Imagen fue enviada correctamente', this.imageId);
        } else{
          console.warn('La api no respondio correctamente', result);
        }

        
      } else  {
        console.warn('no se obtuvo la imagen base64');
      }*/
     
     } 
    catch (error) {
      console.error('Error al tomar o enviar la imagen:', error);
    }

    //await this.uploadImage();
  }





  async uploadImage() {
  const maxRetries = 10;// Número de intentos
  const delayMs = 3000;// Espera entre intentos en milisegundos
  let retries = 0;

  const wait = (ms: number) => new Promise(resolve => setTimeout(resolve, ms));

  while (retries < maxRetries) {
    try {
      const statusResult = await this.api.getImage(this.imageId);
      console.log(`Intento numero ${retries + 1}:`, statusResult);

      if (statusResult?.status === 'success') {
        const data = statusResult.data;
        this.navController.navigateForward('/recognition-results', {
          queryParams: {
            imageId: this.imageId,
            tags: JSON.stringify(data.tags),
            confidence: JSON.stringify(data.confidence_scores),
          }
        });

        console.log('Resultados obtenidos y navegación completada');
        return; // Stop de intentos





      } else {
        console.log('Imagen aún procesándose, reintentando...');
        await wait(delayMs);
        retries++;
      }

    } catch (error) {
      console.error('Error al consultar el estado de la imagen:', error);
      return; // Detener
    }
  }



  

  console.warn('Se alcanzó el número máximo de reintentos sin obtener resultados.');
}
  
  zoomIn() {
    if (this.zoomLevel < 3) { // máximo zoom 3x
      this.zoomLevel += 1;
      this.applyZoom();
    }
  }

  zoomOut() {
    if (this.zoomLevel > 1) {
      this.zoomLevel -= 1;
      this.applyZoom();
    }
  }

  applyZoom() {
    const videoElement = document.querySelector('video');
    if (videoElement) {
      videoElement.style.transform = `scale(${this.zoomLevel.toFixed(2)})`;
    }
  }
}