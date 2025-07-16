import { NgModule, CUSTOM_ELEMENTS_SCHEMA  } from '@angular/core';
import { CommonModule } from '@angular/common';
import { FormsModule } from '@angular/forms';

import { IonicModule } from '@ionic/angular';

import { TranslateModule } from '@ngx-translate/core';

import { AudioPlayerComponent } from './audio-player.component';

@NgModule({
  declarations: [AudioPlayerComponent],
  imports: [
    CommonModule,
    FormsModule,
    TranslateModule,
    IonicModule,
  ],
  exports: [AudioPlayerComponent],
  schemas: [CUSTOM_ELEMENTS_SCHEMA]
  })
export class AudioPlayerModule  {}
