import { NgModule } from '@angular/core';
import { CommonModule } from '@angular/common';
import { FormsModule } from '@angular/forms';

import { IonicModule } from '@ionic/angular';

import { SettingsPrivacyPageRoutingModule } from './settings-privacy-routing.module';

import { SettingsPrivacyPage } from './settings-privacy.page';

@NgModule({
  imports: [
    CommonModule,
    FormsModule,
    IonicModule,
    SettingsPrivacyPageRoutingModule
  ],
  declarations: [SettingsPrivacyPage]
})
export class SettingsPrivacyPageModule {}
