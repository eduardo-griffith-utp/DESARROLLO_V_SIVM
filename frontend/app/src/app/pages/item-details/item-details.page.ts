import { Component, OnInit } from '@angular/core';
import { ActivatedRoute } from '@angular/router';
import { HttpClient } from '@angular/common/http';

@Component({
  selector: 'app-item-details',
  templateUrl: './item-details.page.html',
  styleUrls: ['./item-details.page.scss'],
  standalone: false,
})
export class ItemDetailsPage implements OnInit {

  itemTitle: string = '';
  itemImage: string = '';
  itemDescription: string = '';

  constructor(
    private route: ActivatedRoute,
    private http: HttpClient
  ) {}

  ngOnInit() {
    // Recuperar parámetros de la URL
    this.route.queryParams.subscribe(params => {
      this.itemImage = params['imageUrl'] || 'assets/images/dog.webp';
    });

    // Obtiene los datos desde un servidor JSON
    this.http.get<any>('http://localhost:3000/data')
      .subscribe(data => {
        // Asigna datos principales
        this.itemTitle = data.title || 'Perro';
        this.itemDescription = data.description || 'El perro (Canis familiaris o Canis lupus familiaris, dependiendo de si se lo considera una especie o una subespecie del lobo)...';

      });
  }

}
