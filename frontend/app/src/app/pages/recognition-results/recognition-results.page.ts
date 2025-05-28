import { Component, OnInit } from '@angular/core';
import { ActivatedRoute } from '@angular/router';  // Importa ActivatedRoute para acceder a los parámetros
import { NavController } from '@ionic/angular';
import { HttpClient } from '@angular/common/http';

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
  constructor(private activatedRoute: ActivatedRoute, private http: HttpClient) {}  // Inyecta ActivatedRoute

  ngOnInit() {
    this.getMethod();
    

    // Recupera el parámetro 'imageUrl' de la URL de la página
    this.activatedRoute.queryParams.subscribe(params => {
      this.imageUrl = params['imageUrl'] || null;  // Asigna la URL de la imagen
    });

    // Toma los datos desde el servidor json

  }
  public getMethod() {
    this.http.get('http://localhost:3000/items').subscribe((res:any)=> {
      console.log(res);
      this.getJsonValue = res;
    })
  }
}