import { NgModule } from '@angular/core';
import { Routes, RouterModule } from '@angular/router';

import { SettingsLenguagePage } from './settings-lenguage.page';

const routes: Routes = [
  {
    path: '',
    component: SettingsLenguagePage
  }
];

@NgModule({
  imports: [RouterModule.forChild(routes)],
  exports: [RouterModule],
})
export class SettingsLenguagePageRoutingModule {}
