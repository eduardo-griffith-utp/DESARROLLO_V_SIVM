import {   Component, Input, ViewChild, ElementRef, ChangeDetectionStrategy, OnDestroy, OnChanges, SimpleChanges} from '@angular/core';
import { Subscription, interval } from 'rxjs';

@Component({
  selector: 'app-audio-player',
  templateUrl: './audio-player.component.html',
  styleUrls: ['./audio-player.component.scss'],
  standalone: false,
  changeDetection: ChangeDetectionStrategy.OnPush
})
export class AudioPlayerComponent implements OnDestroy {

  //Fuente de audio o video
  @Input() src = '';
  @ViewChild('audioPlayer', { static: false }) audioPlayerRef!: ElementRef<HTMLAudioElement>;

  //audioSrc = '';
  isPlaying = false;
  currentTime = 0;
  duration = 0;
  progress = 0;

  /* progreso cada 250 ms para no saturar el DOM */
  private tick$!: Subscription;

  ngOnDestroy() {
    this.tick$?.unsubscribe();
  }

  /* timer cuando load() termine */
  onLoadedMetadata() {
    const audio = this.audioPlayerRef.nativeElement;
    this.duration = audio.duration;

    // actualizar la barra sin ChangeDetector mareado
    this.tick$ = interval(250).subscribe(() => {
      if (this.isPlaying) {
        this.currentTime = audio.currentTime;
      }
    });
  }

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

    ngOnChanges(changes: SimpleChanges): void {
    if (changes['src'] && this.audioPlayerRef?.nativeElement) {
      this.audioPlayerRef.nativeElement.load(); // Forzar recarga
    }
  }
}
