import { Component, OnInit } from '@angular/core';
import { ActivatedRoute } from '@angular/router';  // Importa ActivatedRoute para acceder a los parámetros
import { HttpClient } from '@angular/common/http';
import { ApiService } from 'src/app/core/services/api-service.service';

@Component({
  selector: 'app-history',
  templateUrl: './history.page.html',
  styleUrls: ['./history.page.scss'],
  standalone: false,
})
export class HistoryPage implements OnInit {

  public items: any[] = [];
  private mockImages: any[] = []; //si tenemos el metodo Get lo cambiamos por --> private apiImages: any[] = [];


  constructor(private activatedRoute: ActivatedRoute, private http: HttpClient, private api: ApiService) { }

  async ngOnInit() {
    await this.loadImages(); // precarga actualmente la imagen del mock
    await this.loadData();
  }

  private async loadImages() {
    try {
      const res = await fetch('http://localhost:3000/images');
      //necesitamos cambiar el fecth...  por un --> this.apiImages = await this.api.getImages
      //propongo crear el metodo getImages en el api service
      this.mockImages = await res.json(); // si tenemos el metodo Get cambiamos la linea por un --> console.log(this.apiImages);
    } catch (error) {
      console.error('Error cargando mock de imágenes:', error);
    }
  }

  private getMostSpecificTag(imageId: string): string {
    const entry = this.mockImages.find(img => img.data.image_id === imageId); //si se aplica el metodo Get, cambiar mockImages por apiImages
    if (!entry) return 'desconocido';

    const tags = entry.data.tags;
    const genericTags = [tags[0]];
    const specific = tags.find((tag: any) => !genericTags.includes(tag.toLowerCase()));
    return specific || tags[0] || 'desconocido';
  }


async loadData() {
    try {
      const historyResponse = await this.api.getHistory();
      const historyData = historyResponse?.[0]?.data || {};

      const allItems: any[] = [];

      for (const category in historyData) {
        const entries = historyData[category];

        for (const entry of entries) {
          const tag = this.getMostSpecificTag(entry.image_id);
          let imageUrl = 'assets/images/default.jpg';

          try {
            const multimedia = await this.api.getMultimedia(tag);
            imageUrl = multimedia?.data?.find((m: any) => m.type === 'image')?.url || imageUrl;
          } catch (error) {
            console.warn(`Multimedia no encontrada para tag "${tag}"`);
          }

          allItems.push({
            //imageId: entry.image_id,
            timestamp: entry.timestamp,
            description: entry.description,
            category: category,
            tag: tag,
            name: tag,
            imageUrl: imageUrl
          });
          console.log('tag procesada:', tag);
          console.log('Imagen procesada:', imageUrl);
          console.log('ID de imagen:', entry.image_id);
          //console.log('Timestamp:', entry.timestamp);
          console.log('Descripción:', entry.description);
          console.log('Categoría:', category);
          console.log('Nombre:', tag);
        }
      }

      this.items = allItems;
      console.log('Items cargados:', this.items);
    } catch (error) {
      console.error('Error cargando historial:', error);
    }
  }



  /*
  async ngOnInit() {
    await this.getMethod();
    await this.showLoading();
    //await this.getImage();
  }

  public async getMethod() {
    this.getJsonValue = await this.api.getHistory();
    console.log(this.getJsonValue);
  }
public async getImage() {
    this.getJsonImage = await this.api.getImages(1);
    console.log(this.getJsonImage);
  }*/

   /*async showLoading() {
    const loading = await this.loadingCtrl.create({
      message: 'Dismissing after 3 seconds...',    });

    loading.present();
    loading.remove();
  }*/
}
