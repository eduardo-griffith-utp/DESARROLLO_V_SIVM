import { NgModule } from '@angular/core';
import { CommonModule } from '@angular/common';
import { FormsModule } from '@angular/forms';

import { IonicModule } from '@ionic/angular';

import { SettingsLenguagePageRoutingModule } from './settings-lenguage-routing.module';

import { SettingsLenguagePage } from './settings-lenguage.page';

@NgModule({
  imports: [
    CommonModule,
    FormsModule,
    IonicModule,
    SettingsLenguagePageRoutingModule
  ],
  declarations: [SettingsLenguagePage]
})
export class SettingsLenguagePageModule {}
