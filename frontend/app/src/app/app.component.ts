import { Component } from '@angular/core';
import { SplashScreen } from '@capacitor/splash-screen';
import { Platform } from '@ionic/angular';
import { IonProgressBar } from '@ionic/angular/standalone';


@Component({
  selector: 'app-root',
  templateUrl: 'app.component.html',
  styleUrls: ['app.component.scss'],
  standalone: false,
})
export class AppComponent {
  public progress = 0;
  splash =true;

  showSplash = true;
  constructor(){
    setTimeout(() => {
      this.showSplash = false;
    }, 5000);


    setInterval(() => {
      this.progress += 0.011;

    }, 50);
  }

  
  
  /*constructor(private platform: Platform) {
     this.initializeApp();
  }

  initializeApp() {
    this.platform.ready().then(() => {
      setTimeout(() => {
        SplashScreen.hide();
      }, 3000);
    });
  }*/
}

