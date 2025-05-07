import { NgModule } from '@angular/core';
import { CommonModule } from '@angular/common';
import { FormsModule } from '@angular/forms';

import { IonicModule } from '@ionic/angular';

import { RecognitionResultsPageRoutingModule } from './recognition-results-routing.module';

import { RecognitionResultsPage } from './recognition-results.page';

@NgModule({
  imports: [
    CommonModule,
    FormsModule,
    IonicModule,
    RecognitionResultsPageRoutingModule
  ],
  declarations: [RecognitionResultsPage]
})
export class RecognitionResultsPageModule {}
