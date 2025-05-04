import { NgModule } from '@angular/core';
import { CommonModule } from '@angular/common';
import { FormsModule } from '@angular/forms';

import { IonicModule } from '@ionic/angular';

import { ImageCapturePageRoutingModule } from './image-capture-routing.module';

import { ImageCapturePage } from './image-capture.page';

@NgModule({
  imports: [
    CommonModule,
    FormsModule,
    IonicModule,
    ImageCapturePageRoutingModule
  ],
  declarations: [ImageCapturePage]
})
export class ImageCapturePageModule {}
