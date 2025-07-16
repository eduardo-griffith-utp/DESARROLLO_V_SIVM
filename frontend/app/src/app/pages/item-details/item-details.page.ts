import { Component, OnInit, ViewChild, ElementRef } from '@angular/core';
import { ActivatedRoute } from '@angular/router';  // Importa ActivatedRoute para acceder a los parámetros
import { NavController } from '@ionic/angular';
import { HttpClient } from '@angular/common/http';
import { ApiService } from 'src/app/core/services/api-service.service';


@Component({
  selector: 'app-item-details',
  templateUrl: './item-details.page.html',
  styleUrls: ['./item-details.page.scss'],
  standalone: false,
})
export class ItemDetailsPage implements OnInit {

  itemTitle: string = '';
  itemImage: string = '';
  itemDescription: string = '';
  public getJsonValue: any;


  /* Audio player logic
  @ViewChild('audioPlayer', { static: false }) audioPlayerRef!: ElementRef<HTMLAudioElement>;*/
    audioSrc: string = '';
    /*isPlaying = false;
    duration = 0;
    progress = 0;
    currentTime = 0;*/

  constructor(
    private route: ActivatedRoute, private activatedRoute: ActivatedRoute, private http: HttpClient, private api: ApiService

  ) {}

  async ngOnInit() {
    this.route.queryParams.subscribe(async params => {
    const multimediaTag = params['tag']; // por ejemplo: 'banana'
    this.itemTitle = params['name'] || 'nombre no disponible';
    this.itemDescription = params['description'] || 'Descripción no disponible';
    this.itemImage = params['imageUrl'] || 'assets/images/default.jpg';

    if (multimediaTag) {
      await this.loadMultimedia(multimediaTag);
    }
  });

  await this.getMethod();
  }

  public async getMethod() {
    this.getJsonValue = await this.api.getItem();
    console.log(this.getJsonValue);

  }

  async loadMultimedia(tag: string) {
    try {
        const multimedia = await this.api.getMultimedia(tag);
        const audio = multimedia.data.find((item: any) => item.type === 'audio');
        const video = multimedia.data.find((item: any) => item.type === 'video');

        /*const cleanUrl = (url: string) => {
          return url.replace(/^.*assets\//, 'assets/'); // limpia hasta "assets/"
        };*/

        if (audio && audio.url) {
          //this.audioSrc = cleanUrl(audio.url);
          console.log('Audio cargado:', this.audioSrc);
        } else if (video && video.url) {
          //this.audioSrc = cleanUrl(video.url);  // puedes usar otro nombre como `videoSrc`
          console.log('Video cargado:', this.audioSrc);
        } else {
          console.warn('No se encontró video ni audio.');
          this.audioSrc = '';
        }
      } catch (error) {
        console.error('Error al cargar multimedia:', error);
        this.audioSrc = '';
      }
      /*if (this.audioPlayerRef?.nativeElement) {
        const audio = this.audioPlayerRef.nativeElement;
        audio.load();  // <-- fuerza recarga de <source>
      }*/

  }

  /*/ audio
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
*/
}
