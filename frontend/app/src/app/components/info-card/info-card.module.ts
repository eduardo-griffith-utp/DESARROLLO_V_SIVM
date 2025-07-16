import { NgModule, CUSTOM_ELEMENTS_SCHEMA  } from '@angular/core';
import { CommonModule } from '@angular/common';
import { FormsModule } from '@angular/forms';

import { IonicModule } from '@ionic/angular';

import { TranslateModule } from '@ngx-translate/core';

import { InfoCardComponent } from './info-card.component';

import { AudioPlayerModule } from '../audio-player/audio-player.module';

@NgModule({
  declarations: [InfoCardComponent],
  imports: [
    CommonModule,
    FormsModule,
    TranslateModule,
    AudioPlayerModule,
    IonicModule
  ],
  exports: [InfoCardComponent],
  schemas: [CUSTOM_ELEMENTS_SCHEMA]
  })
export class InfoCardModule {}
