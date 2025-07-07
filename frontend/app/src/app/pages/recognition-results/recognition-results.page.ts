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
  imageId: any;

  public getJsonValue: any;
  public postJsonValue: any;
  public loading: any;
  constructor(private activatedRoute: ActivatedRoute, private http: HttpClient, private api: ApiService, private loadingCtrl: LoadingController) {}  // Inyecta ActivatedRoute

  async ngOnInit() {
    

    //De esta forma recibimos el id de Image capture y lo pasamos a una variable en RecResults

    try {
      await this.showLoading();

      //De esta forma recibimos el id de Image capture y lo pasamos a una variable en RecResults
      this.activatedRoute.queryParams.subscribe (params => {
        this.imageId = params['imageId'];
        console.log('Se recibio el id de la imagen', this.imageId);
      });
    this.imageUrl = sessionStorage.getItem('ImagenCapturada');
    }catch (error: any) {
      console.log('error al cargar el id');
    }




    /*De esta forma almacenamos el id con el href
    this.imageUrl = sessionStorage.getItem('image_id');
    console.log("comenzando",this.imageUrl);
    */
  

    // Toma los datos desde el servidor json

  }
  public async getMethod() {
    console.log("Mostrando resultados");
    this.getJsonValue = await this.api.getImage(this.imageId);
    console.log(this.getJsonValue);
    if(this.getJsonValue.status != "processing")
      this.loading.remove();
    else
      this.getMethod();
    }
  

  async showLoading() {
    this.loading = await this.loadingCtrl.create({
      message: 'Cargando resultados...',
      duration: 8000,
    });
    console.log("Loading");
    this.loading.present();
  }
}

