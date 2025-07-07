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
  tag: any;

  public getJsonValue: any;
  public StatusValue: any;
  public loading: any;
  constructor(private activatedRoute: ActivatedRoute, private http: HttpClient, private api: ApiService, private loadingCtrl: LoadingController) {}  // Inyecta ActivatedRoute

  async ngOnInit() {
    

    //De esta forma recibimos el id de Image capture y lo pasamos a una variable en RecResults

    try {
      await this.showLoading();

      //De esta forma recibimos el id de Image capture y lo pasamos a una variable en RecResults
      /*this.activatedRoute.queryParams.subscribe (params => {
        this.imageId = params['imageId'];
        console.log('Se recibio el id de la imagen', this.imageId);
      });
      this.imageUrl = sessionStorage.getItem('ImagenCapturada');*/
    }catch (error: any) {
      console.log('error al cargar el id');
    }




    /*De esta forma almacenamos el id con el href
    this.imageUrl = sessionStorage.getItem('image_id');
    console.log("comenzando",this.imageUrl);
    */
  

    // Toma los datos desde el servidor json

  }
  /*public async getMethod() {
    console.log("Mostrando resultados");
    this.getJsonValue = await this.api.getImage(this.imageId);
    console.log(this.getJsonValue);
    if(this.getJsonValue.status != "processing")
      this.loading.remove();
    else
      this.getMethod();
    }*/
  

  async showLoading() {
    this.loading = await this.loadingCtrl.create({
      message: 'Cargando resultados...',
      spinner: 'circles',
      backdropDismiss: false,
    });

    await this.loading.present();
    console.log("Cargando informacion");

    this.activatedRoute.queryParams.subscribe (async params => {
      this.imageId = params['imageId'];
      console.log('Se recibio el id de la imagen', this.imageId);
      await this.showResults();
    });
    
  }

  async showResults() {
    console.log("Resultados");


    const maxRetries = 10;// Número de intentos
    const delayMs = 3000; //tiempo 
    let retries = 0;

    //Almacenar la imagen para probar que se capturo correctamente
    this.imageUrl = sessionStorage.getItem('ImagenCapturada');

    /*try { Try sin el repetidor
      

      //Almacenar la imagen para probar que se capturo correctamente
      this.imageUrl = sessionStorage.getItem('ImagenCapturada');

      //this.getJsonValue =await this.api.getImage(this.imageId);
      //De esta forma evitamos conflictos con el mock en el imageId

      
      //Decalro el id manualmente para que coincida con el de db.json
      const imgMock = 'img_002';
      console.log(imgMock);

      

      this.StatusValue = await this.api.getImage(imgMock);



      console.log("Get completado almacenando", this.StatusValue);
      console.log('carga terminada');
    
    }catch(error: any){
      console.log("No se pudo compeltar el get");
    }*/


    //Se hace el llamado al array para obtener el tag de la imagen
    /*if(this.StatusValue.status == "success"){
      this.tag = this.StatusValue.data.tags;
      console.log('tag tipo', this.tag);


      //
      await this.loading.dismiss();
    }else {
      console.log("Error leyendo el status");
    }*/


    const wait = (ms: number) => new Promise(resolve => setTimeout(resolve, ms));

  while (retries < maxRetries) {
    try {
      console.log('Comenzando');

      //const statusResult = await this.api.getImage(this.imageId);
      //this.getJsonValue =await this.api.getImage(this.imageId);
      //De esta forma evitamos conflictos con el mock en el imageId

      //Get 
      this.StatusValue = await this.api.getAnalysis(this.imageId);

      console.log("Get completado almacenando", this.StatusValue);
      console.log('carga terminada');
      console.log(`Intento numero ${retries + 1}:`, this.StatusValue);

      if(this.StatusValue.status == "success"){
        this.tag = this.StatusValue.data.tags;
        console.log('tag tipo', this.tag);
      
      //termino la carga
        await this.loading.dismiss();
      return; //termino el repetidor de intentos
      
    }else {
      console.log("Error leyendo el status");
      await wait(delayMs);
      retries++;
    }

    }catch (error) {
      console.error('Error al consultar el estado de la imagen:', error);
      return; // Detener
    }
  }
  console.warn('Se alcanzó el número máximo de reintentos sin obtener resultados.');

  }
}

