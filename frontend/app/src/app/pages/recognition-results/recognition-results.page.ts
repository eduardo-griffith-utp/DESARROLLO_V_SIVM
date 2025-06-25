import { Component, OnInit } from '@angular/core';
import { ActivatedRoute } from '@angular/router';  // Importa ActivatedRoute para acceder a los parámetros


@Component({
  selector: 'app-recognition-results',
  templateUrl: './recognition-results.page.html',
  styleUrls: ['./recognition-results.page.scss'],
  standalone: false,
})
export class RecognitionResultsPage implements OnInit {
  imageUrl: string | undefined;  // Variable para almacenar la URL de la imagen

  constructor(private activatedRoute: ActivatedRoute) {}  // Inyecta ActivatedRoute

  ngOnInit() {
    // Recupera el parámetro 'imageUrl' de la URL de la página
    this.activatedRoute.queryParams.subscribe(params => {
      this.imageUrl = params['imageUrl'];  // Asigna la URL de la imagen
    });
  }
}