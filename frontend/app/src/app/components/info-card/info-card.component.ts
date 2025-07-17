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
  @Input() descriptionMaxLength: number = 45;

  @ViewChild('audioPlayer', { static: false }) audioPlayerRef!: ElementRef<HTMLAudioElement>;

  // New properties for description management
  public showFullDescription: boolean = false;
  public truncatedDescription: string = '';
  public needsReadMore: boolean = false;

  ngOnChanges(changes: SimpleChanges): void {
    if (changes['audioSrc'] && changes['audioSrc'].currentValue) {
      setTimeout(() => {
        if (this.audioPlayerRef?.nativeElement) {
          this.audioPlayerRef.nativeElement.load();
          console.log('Audio player reloaded in component.');
        }
      });
    }

    // New: Handle description truncation on changes
    if (changes['description']) {
      this.updateDescriptionDisplay();
    }
  }
  private updateDescriptionDisplay() {
    if (this.description.length > this.descriptionMaxLength) {
      this.truncatedDescription = this.description.substring(0, this.descriptionMaxLength) + '...';
      this.needsReadMore = true;
    } else {
      this.truncatedDescription = this.description;
      this.needsReadMore = false;
    }
    this.showFullDescription = false;
  }

  toggleDescription(): void {
    this.showFullDescription = !this.showFullDescription;
  }

}
