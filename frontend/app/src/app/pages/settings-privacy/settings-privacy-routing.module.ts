import { NgModule } from '@angular/core';
import { Routes, RouterModule } from '@angular/router';

import { SettingsPrivacyPage } from './settings-privacy.page';

const routes: Routes = [
  {
    path: '',
    component: SettingsPrivacyPage
  }
];

@NgModule({
  imports: [RouterModule.forChild(routes)],
  exports: [RouterModule],
})
export class SettingsPrivacyPageRoutingModule {}
