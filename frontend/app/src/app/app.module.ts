import { NgModule } from '@angular/core';
import { BrowserModule } from '@angular/platform-browser';
import { RouteReuseStrategy } from '@angular/router';

import { IonicModule, IonicRouteStrategy } from '@ionic/angular';

import { AppComponent } from './app.component';
import { AppRoutingModule } from './app-routing.module';
import { ServicesService } from './core/services/services.service';
import { HttpClient, HttpClientModule } from '@angular/common/http'
import { TranslateLoader, TranslateModule } from '@ngx-translate/core';
import { TranslateHttpLoader } from '@ngx-translate/http-loader';
import { ApiService } from 'src/app/core/services/api-service.service';
import { MockApiService } from 'src/app/core/services/mock-api.service';
import { AbstractApiService } from 'src/app/core/services/abstract-api.service';
import { environment } from 'src/environments/environment';

export function HttpLoaderFactory(http: HttpClient) {
  return new TranslateHttpLoader(http);
}


@NgModule({
  declarations: [AppComponent],
  imports: [BrowserModule, IonicModule.forRoot(), AppRoutingModule, HttpClientModule,
    TranslateModule.forRoot(
      {
      loader:{
        provide:TranslateLoader,
        useFactory:HttpLoaderFactory,
        deps:[HttpClient]
      }
    }
    )
  ],
  providers: [HttpClient, ServicesService,{  provide: RouteReuseStrategy, useClass: IonicRouteStrategy}, { provide: AbstractApiService, useClass: environment.useMock ? MockApiService : ApiService }],
  bootstrap: [AppComponent],
})
export class AppModule {}
