import { Component, OnInit, OnDestroy } from '@angular/core';
import { Camera, CameraResultType, CameraSource } from '@capacitor/camera';

@Component({
  selector: 'app-image-capture', // Selector actualizado
  templateUrl: './image-capture.page.html', // Referencia al nuevo nombre del HTML
  styleUrls: ['./image-capture.page.scss'], // Referencia al nuevo nombre del SCSS
  standalone: false,
})
export class ImageCapturePage implements OnInit, OnDestroy { // Clase renombrada a ImageCapturePage
  imageUrl: string | undefined;
  isCameraActive = false;
  videoStream: MediaStream | undefined;

  constructor() {}

  async ngOnInit() {
    this.startCameraPreview();
  }

  ngOnDestroy() {
    this.stopCameraPreview();
  }

  async startCameraPreview() {
    try {
      const stream = await navigator.mediaDevices.getUserMedia({
        video: { facingMode: 'environment' }, // 'user' para la cámara frontal
        audio: false,
      });
      this.videoStream = stream;
      this.isCameraActive = true;
      this.attachVideoToElement();
    } catch (error) {
      console.error('Error al acceder a la cámara:', error);
      this.isCameraActive = false;
      // Aquí puedes mostrar un mensaje de error al usuario
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
        resultType: CameraResultType.Uri,
        source: CameraSource.Camera,
      });

      this.imageUrl = image.webPath;
      console.log('Imagen capturada:', this.imageUrl);
      // Aquí puedes procesar la imagen capturada
    } catch (error) {
      console.error('Error al tomar la foto:', error);
      // Aquí puedes manejar el error
    }
  }

  async uploadImage() {
    // Implementa la lógica para subir la imagen
    console.log('Subir imagen seleccionado');
  }
}