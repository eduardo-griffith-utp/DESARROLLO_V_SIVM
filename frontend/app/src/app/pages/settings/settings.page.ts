import { Component } from '@angular/core';
import { ModalController } from '@ionic/angular';
@Component({
  selector: 'app-settings',
  templateUrl: './settings.page.html',
  styleUrls: ['./settings.page.scss'],
  standalone: false,
})
export class SettingsPage {
  notificationsEnabled: boolean = true;
  autoScanEnabled: boolean = false;
  darkModeEnabled: boolean = false;
  appVersion: string = '1.0.0';

  constructor(private modalCtrl: ModalController) {}



  toggleDarkMode() {
    document.body.classList.toggle('dark', this.darkModeEnabled);
  }
}