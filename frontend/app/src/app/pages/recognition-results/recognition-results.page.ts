import { Component, ElementRef, OnInit, ViewChild } from '@angular/core';
import { ActivatedRoute } from '@angular/router';  // Importa ActivatedRoute para acceder a los parámetros
import { LoadingController, NavController } from '@ionic/angular';
import { HttpClient } from '@angular/common/http';
import { ApiService } from 'src/app/core/services/api-service.service';

@Component({
  selector: 'app-recognition-results',
  templateUrl: './recognition-results.page.html',
  styleUrls: ['./recognition-results.page.scss'],
  standalone: false,
})
export class RecognitionResultsPage implements OnInit {
  imageUrl: any;  // Variable para almacenar la URL de la imagen
  items = []
  imageId: any;
  tag: any;




  public getJsonValue: any;
  public StatusValue: any;
  public loading: any;
  public ItemValue: any;



  // Audio player logic
  @ViewChild('audioPlayer', { static: false }) audioPlayerRef!: ElementRef<HTMLAudioElement>;
  audioSrc: string = '';
  isPlaying = false;
  duration = 0;
  progress = 0;
  currentTime = 0;

  constructor(private activatedRoute: ActivatedRoute, private http: HttpClient, private api: ApiService, private loadingCtrl: LoadingController) { }  // Inyecta ActivatedRoute

  async ngOnInit() {


    //De esta forma recibimos el id de Image capture y lo pasamos a una variable en RecResults

    try {
      await this.showLoading();

      //De esta forma recibimos el id de Image capture y lo pasamos a una variable en RecResults
      /*this.activatedRoute.queryParams.subscribe (params => {
        this.imageId = params['imageId'];
        console.log('Se recibio el id de la imagen', this.imageId);
      });
      this.imageUrl = sessionStorage.getItem('ImagenCapturada');*/
    } catch (error: any) {
      console.log('error al cargar el id');
    }




    /*De esta forma almacenamos el id con el href
    this.imageUrl = sessionStorage.getItem('image_id');
    console.log("comenzando",this.imageUrl);
    */


    // Toma los datos desde el servidor json

  }
  /*public async getMethod() {
    console.log("Mostrando resultados");
    this.getJsonValue = await this.api.getImage(this.imageId);
    console.log(this.getJsonValue);
    if(this.getJsonValue.status != "processing")
      this.loading.remove();
    else
      this.getMethod();
    }*/


  async showLoading() {
    this.loading = await this.loadingCtrl.create({
      message: 'Cargando resultados...',
      spinner: 'circles',
      backdropDismiss: false,
    });

    await this.loading.present();
    console.log("Cargando informacion");

    this.activatedRoute.queryParams.subscribe(async params => {
      this.imageId = params['imageId'];
      console.log('Se recibio el id de la imagen', this.imageId);
      await this.showResults();
    });

  }

  async showResults() {
    console.log("Resultados");


    const maxRetries = 10;// Número de intentos
    const delayMs = 3000; //tiempo 
    let retries = 0;

    //Almacenar la imagen para probar que se capturo correctamente
    this.imageUrl = sessionStorage.getItem('ImagenCapturada');

    /*try { Try sin el repetidor
      

      //Almacenar la imagen para probar que se capturo correctamente
      this.imageUrl = sessionStorage.getItem('ImagenCapturada');

      //this.getJsonValue =await this.api.getImage(this.imageId);
      //De esta forma evitamos conflictos con el mock en el imageId

      
      //Decalro el id manualmente para que coincida con el de db.json
      const imgMock = 'img_002';
      console.log(imgMock);

      

      this.StatusValue = await this.api.getImage(imgMock);



      console.log("Get completado almacenando", this.StatusValue);
      console.log('carga terminada');
    
    }catch(error: any){
      console.log("No se pudo compeltar el get");
    }*/


    //Se hace el llamado al array para obtener el tag de la imagen
    /*if(this.StatusValue.status == "success"){
      this.tag = this.StatusValue.data.tags;
      console.log('tag tipo', this.tag);


      //
      await this.loading.dismiss();
    }else {
      console.log("Error leyendo el status");
    }*/


    const wait = (ms: number) => new Promise(resolve => setTimeout(resolve, ms));

    while (retries < maxRetries) {
      try {
        console.log('Comenzando');

        //const statusResult = await this.api.getImage(this.imageId);
        //this.getJsonValue =await this.api.getImage(this.imageId);
        //De esta forma evitamos conflictos con el mock en el imageId

        //Get 
        this.StatusValue = await this.api.getAnalysis(this.imageId);

        console.log("Get completado almacenando", this.StatusValue);
        console.log('carga terminada');
        console.log(`Intento numero ${retries + 1}:`, this.StatusValue);

        if (this.StatusValue.status == "success") {
          this.tag = this.StatusValue.data.tags;
          console.log('tag tipo', this.tag);

          //termino la carga
          await this.loading.dismiss();

          this.showMultimedia();
          return; //termino el repetidor de intentos
        } else {
          console.log("Error leyendo el status");
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
  async loadMultimedia(tag: string) {
    try {
      const multimedia = await this.api.getMultimedia(tag);
      console.log(multimedia);
      const audio = multimedia.data.find((item: any) => item.type === 'audio');
      const video = multimedia.data.find((item: any) => item.type === 'video');

      const cleanUrl = (url: string) => {
        return url.replace(/^.*assets\//, 'assets/'); // limpia hasta "assets/"
      };

      if (audio && audio.url) {
        this.audioSrc = /*cleanUrl(*/audio.url//);
        console.log('Audio cargado:', this.audioSrc);
      } else if (video && video.url) {
        this.audioSrc = cleanUrl(video.url);  // puedes usar otro nombre como `videoSrc`
        console.log('Video cargado:', this.audioSrc);
      } else {
        console.warn('No se encontró video ni audio.');
        this.audioSrc = '';
      }
    } catch (error) {
      console.error('Error al cargar multimedia:', error);
      this.audioSrc = '';
    }
    if (this.audioPlayerRef?.nativeElement) {
      const audio = this.audioPlayerRef.nativeElement;
      audio.load();  // <-- fuerza recarga de <source>
    }

  }
  //audio en recognition
  togglePlayPause() {
    const audio = this.audioPlayerRef.nativeElement;
    if (audio.paused) {
      audio.play();
      this.isPlaying = true;
    } else {
      audio.pause();
      this.isPlaying = false;
    }
  }

  rewind() {
    const audio = this.audioPlayerRef.nativeElement;
    audio.currentTime = Math.max(audio.currentTime - 10, 0);
  }

  forward() {
    const audio = this.audioPlayerRef.nativeElement;
    audio.currentTime = Math.min(audio.currentTime + 10, audio.duration);
  }

  updateProgress() {
    const audio = this.audioPlayerRef.nativeElement;
    this.currentTime = audio.currentTime;
    this.progress = audio.duration ? audio.currentTime / audio.duration : 0;
  }


  setDuration() {
    const audio = this.audioPlayerRef.nativeElement;
    this.duration = audio.duration;
  }

  seekAudio(event: any) {
    const audio = this.audioPlayerRef.nativeElement;
    const value = event.detail.value;
    audio.currentTime = value;
    this.currentTime = value;
  }

  formatTime(time: number): string {
    const minutes = Math.floor(time / 60);
    const seconds = Math.floor(time % 60);
    return `${this.pad(minutes)}:${this.pad(seconds)}`;
  }

  pad(value: number): string {
    return value < 10 ? '0' + value : '' + value;
  }

  async showMultimedia() {
    this.ItemValue = await this.api.getItemDetails(this.imageId);
    console.log('Detalles', this.ItemValue);
    await this.loadMultimedia(this.tag);
  }

}

