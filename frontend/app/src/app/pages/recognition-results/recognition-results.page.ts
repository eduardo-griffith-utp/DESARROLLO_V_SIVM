import { Component, OnInit } from '@angular/core';
import { ActivatedRoute } from '@angular/router';  // Importa ActivatedRoute para acceder a los parámetros
import { NavController } from '@ionic/angular';
import { HttpClient } from '@angular/common/http';
import { ApiService } from 'src/app/core/services/api-service.service';

@Component({
  selector: 'app-recognition-results',
  templateUrl: './recognition-results.page.html',
  styleUrls: ['./recognition-results.page.scss'],
  standalone: false,
})
export class RecognitionResultsPage implements OnInit {
  imageUrl: string | undefined;  // Variable para almacenar la URL de la imagen
  items = []

  public getJsonValue: any;
  public postJsonValue: any;
  constructor(private activatedRoute: ActivatedRoute, private http: HttpClient, private api: ApiService) {}  // Inyecta ActivatedRoute

  async ngOnInit() {
    await this.getMethod();
    

    // Recupera el parámetro 'imageUrl' de la URL de la página
    this.activatedRoute.queryParams.subscribe(params => {
      this.imageUrl = params['imageUrl'] || null;  // Asigna la URL de la imagen
    });

    // Toma los datos desde el servidor json

  }
  public async getMethod() {
    this.getJsonValue = await this.api.getItemDetails(2);
    console.log(this.getJsonValue);
  }
}