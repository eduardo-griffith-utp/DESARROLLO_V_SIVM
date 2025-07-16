import {   Component, Input, ViewChild, ElementRef, ChangeDetectionStrategy, OnDestroy, OnChanges, SimpleChanges} from '@angular/core';
import { Subscription, interval } from 'rxjs';

@Component({
  selector: 'app-info-card',
  templateUrl: './info-card.component.html',
  styleUrls: ['./info-card.component.scss'],
  standalone: false
})
export class InfoCardComponent implements OnChanges {

  @Input() title: string = '';
  @Input() description: string = '';
  @Input() imageUrl: string = '';
  @Input() audioSrc: string = '';

  @ViewChild('audioPlayer', { static: false }) audioPlayerRef!: ElementRef<HTMLAudioElement>;

  ngOnChanges(changes: SimpleChanges): void {
    if (changes['audioSrc'] && changes['audioSrc'].currentValue) {
      setTimeout(() => {
        if (this.audioPlayerRef?.nativeElement) {
          this.audioPlayerRef.nativeElement.load();
          console.log('Audio player reloaded in component.');
        }
      });
    }
  }

}
