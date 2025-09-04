import { Component, OnInit, OnDestroy } from '@angular/core';
import { Camera, CameraResultType, CameraSource } from '@capacitor/camera';
import { NavController } from '@ionic/angular';  // Importa NavController para navegar


@Component({
  selector: 'app-image-capture', // Selector actualizado
  templateUrl: './image-capture.page.html', // Referencia al nuevo nombre del HTML
  styleUrls: ['./image-capture.page.scss'], // Referencia al nuevo nombre del SCSS
  standalone: false,
})





export class ImageCapturePage implements OnInit, OnDestroy {
  imageUrl: string | undefined;
  isCameraActive = false;
  videoStream: MediaStream | undefined;

  constructor(private navController: NavController) {}  // Inyecta NavController

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
        resultType: CameraResultType.Uri,
        source: CameraSource.Camera,
      });

      this.imageUrl = image.webPath;
      console.log('Imagen capturada:', this.imageUrl);

      // Redirigir a la página de resultados, pasando la URL de la imagen
      this.navController.navigateForward('/recognition-results', {
        queryParams: {
          imageUrl: this.imageUrl,  // Pasa la URL de la imagen
        },
      });

    } catch (error) {
      console.error('Error al tomar la foto:', error);
    }
  }

  async uploadImage() {
    console.log('Subir imagen seleccionado');
  }
}