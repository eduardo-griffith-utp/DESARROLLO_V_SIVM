import { Component, OnInit } from '@angular/core';
import { ActivatedRoute } from '@angular/router';  // Importa ActivatedRoute para acceder a los parámetros
import { LoadingController, NavController } from '@ionic/angular';
import { HttpClient } from '@angular/common/http';
import { ApiService } from 'src/app/core/services/api-service.service';

@Component({
  selector: 'app-recognition-results',
  templateUrl: './recognition-results.page.html',
  styleUrls: ['./recognition-results.page.scss'],
  standalone: false,
})
export class RecognitionResultsPage implements OnInit {
  imageUrl: any;  // Variable para almacenar la URL de la imagen
  items = []

  public getJsonValue: any;
  public postJsonValue: any;
  public loading: any;
  constructor(private activatedRoute: ActivatedRoute, private http: HttpClient, private api: ApiService, private loadingCtrl: LoadingController) {}  // Inyecta ActivatedRoute

  async ngOnInit() {
    await this.showLoading();

    this.imageUrl = sessionStorage.getItem('image_id');
    console.log("comenzando");
    await this.getMethod();
    // Toma los datos desde el servidor json

  }
  public async getMethod() {
    console.log("hola");
    this.getJsonValue = await this.api.getImage(this.imageUrl);
    console.log(this.getJsonValue);
    if(this.getJsonValue.status != "processing")
    this.loading.remove();
  else
    this.getMethod();
  }
  

  async showLoading() {
    this.loading = await this.loadingCtrl.create({
      message: 'Dismissing after 3 seconds...',    });
      
    this.loading.present();
  }
}

