import { Component, OnInit } from '@angular/core';

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

  constructor() { }

  ngOnInit() {
    // Simulación de datos cargados desde un JSON
    const data = {
      title: 'Perro',
      image: 'assets/images/dog.webp',
      description: 'El perro (Canis familiaris o Canis lupus familiaris, dependiendo de si se lo considera una especie o una subespecie del lobo)...'
    };

    this.itemTitle = data.title;
    this.itemImage = data.image;
    this.itemDescription = data.description;
  }
}


