import { NgModule } from '@angular/core';
import { Routes, RouterModule } from '@angular/router';

import { ImageCapturePage } from './image-capture.page';

const routes: Routes = [
  {
    path: '',
    component: ImageCapturePage
  }
];

@NgModule({
  imports: [RouterModule.forChild(routes)],
  exports: [RouterModule],
})
export class ImageCapturePageRoutingModule {}
