from tensorflow.keras import layers, models
from tensorflow.keras.models import save_model, load_model
from tensorflow.keras.applications import MobileNetV2
import json
import os

class CNNModel:
    def __init__(self, input_shape, num_classes, class_names=None):
        self.input_shape = input_shape
        self.num_classes = num_classes
        self.class_names = class_names

    def build_model(self):
        base_model = MobileNetV2(
            input_shape=self.input_shape,
            include_top=False,
            weights='imagenet'
        )
        base_model.trainable = False  # Puedes cambiar a True más adelante para fine-tuning

        model = models.Sequential([
            base_model,
            layers.GlobalAveragePooling2D(),
            layers.Dense(128, activation='relu'),
            layers.Dropout(0.5),
            layers.Dense(self.num_classes, activation='softmax')
        ])

        model.compile(
            optimizer='adam',
            loss='sparse_categorical_crossentropy',
            metrics=['accuracy']
        )

        if self.class_names is not None:
            model.class_names = self.class_names

        return model

    @staticmethod
    def save_model_with_classes(model, filepath, class_names=None):
        os.makedirs(os.path.dirname(filepath), exist_ok=True)
        if class_names is not None:
            class_file = os.path.join(os.path.dirname(filepath), 'class_names.json')
            with open(class_file, 'w') as f:
                json.dump(class_names, f)
        model.save(filepath)

    @staticmethod
    def save_model(model, path, class_names=None):
        model.save(path)
        if class_names is not None:
            metadata_path = os.path.splitext(path)[0] + '_metadata.json'
            with open(metadata_path, 'w') as f:
                json.dump({'class_names': class_names}, f)

    @staticmethod
    def load_model(path):
        model = models.load_model(path)
        metadata_path = os.path.splitext(path)[0] + '_metadata.json'
        class_names = None
        if os.path.exists(metadata_path):
            with open(metadata_path, 'r') as f:
                metadata = json.load(f)
                class_names = metadata.get('class_names')
        elif hasattr(model, 'class_names'):
            class_names = model.class_names
        return model, class_names
