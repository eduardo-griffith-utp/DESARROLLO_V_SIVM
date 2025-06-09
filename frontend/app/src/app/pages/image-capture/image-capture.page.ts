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
  imageUrl: string | undefined;
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
      this.navController.navigateForward('/recognition-results', {
        queryParams: {
          imageUrl: this.imageUrl,  // Pasa la URL de la imagen
        },
      });

    } catch (error) {
      console.error('Error al tomar la foto:', error);
    }
  }

  async captureNow() {
    console.log('Botón presionado');
    try {
      const image = await Camera.getPhoto({
        quality: 90,
        allowEditing: false,
        resultType: CameraResultType.Base64,
        //source: CameraSource.Camera, de esta forma se declara si ejecutamos en un dispositivo real
        //Ejecucion modo developer 
        source: Capacitor.getPlatform() === 'web' ? CameraSource.Prompt : CameraSource.Camera
      });
      const base64Data = image.base64String;

      if (base64Data) {
        this.api.postItem(base64Data);
      } else {
        console.error('Error: la imagen no tiene datos base64.');
      }
      
      this.imageUrl = image.webPath;
      console.log('Imagen capturada al instante:', this.imageUrl);

      // Redirigir a la página de resultados, pasando la URL de la imagen
      this.navController.navigateForward('/recognition-results', {
        queryParams: {
          imageUrl: this.imageUrl,  // Pasa la URL de la imagen
        },
      });

    } catch (error) {
      console.error('Error al tomar la foto al instante:', error);
    }
  }

  async uploadImage() {
    console.log('Subir imagen seleccionado');
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