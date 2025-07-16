import { NgModule } from '@angular/core';
import { CommonModule } from '@angular/common';
import { FormsModule } from '@angular/forms';

import { IonicModule } from '@ionic/angular';

import { ItemDetailsPageRoutingModule } from './item-details-routing.module';

import { ItemDetailsPage } from './item-details.page';

import { TranslateModule } from '@ngx-translate/core';

//import { AudioPlayerModule } from 'src/app/components/audio-player/audio-player.module';

import { InfoCardModule } from 'src/app/components/info-card/info-card.module';

@NgModule({
  imports: [
    CommonModule,
    FormsModule,
    TranslateModule,
    IonicModule,
    ItemDetailsPageRoutingModule,
    //AudioPlayerModule,
    InfoCardModule
  ],
  declarations: [ItemDetailsPage]
})
export class ItemDetailsPageModule {}
