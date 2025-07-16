import { NgModule } from '@angular/core';
import { CommonModule } from '@angular/common';
import { FormsModule } from '@angular/forms';

import { IonicModule } from '@ionic/angular';

import { ItemDetailsPageRoutingModule } from './item-details-routing.module';

import { ItemDetailsPage } from './item-details.page';

import { TranslateModule } from '@ngx-translate/core';

import { AudioPlayerModule } from 'src/app/components/audio-player/audio-player.module';

@NgModule({
  imports: [
    CommonModule,
    FormsModule,
    TranslateModule,
    IonicModule,
    ItemDetailsPageRoutingModule,
    AudioPlayerModule
  ],
  declarations: [ItemDetailsPage]
})
export class ItemDetailsPageModule {}
