import { platformBrowserDynamic } from '@angular/platform-browser-dynamic';

//Se declaran los componentes para ejecutar en la web la camara
import { enableProdMode } from '@angular/core';
import { defineCustomElements } from '@ionic/pwa-elements/loader';
import { environment } from './environments/environment';


defineCustomElements(window);

import { AppModule } from './app/app.module';

platformBrowserDynamic().bootstrapModule(AppModule)
  .catch(err => console.log(err));


if (environment.production) {
  enableProdMode();
}

platformBrowserDynamic()
  .bootstrapModule(AppModule)
  .catch(err => console.log(err));