import { Component, OnInit } from '@angular/core';
import { ActivatedRoute } from '@angular/router';  // Importa ActivatedRoute para acceder a los parámetros
import { NavController } from '@ionic/angular';
import { HttpClient } from '@angular/common/http';
import { ApiService } from 'src/app/core/services/api-service.service';


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
  public getJsonValue: any;

  constructor(
    private route: ActivatedRoute, private activatedRoute: ActivatedRoute, private http: HttpClient, private api: ApiService
    
  ) {}

  async ngOnInit() {
    // Recuperar parámetros de la URL
    this.route.queryParams.subscribe(params => {
      this.itemImage = params['imageUrl'] || 'assets/images/dog.webp';
    });

    // Obtiene los datos desde un servidor JSON
  await this.getMethod();
  }

  public async getMethod() {
    this.getJsonValue = await this.api.getItem();
    console.log(this.getJsonValue);
  }

}
