import { Component, OnInit } from '@angular/core';
import { ActivatedRoute } from '@angular/router';  // Importa ActivatedRoute para acceder a los parámetros
import { LoadingController, NavController } from '@ionic/angular';
import { HttpClient } from '@angular/common/http';
import { ApiService } from 'src/app/core/services/api-service.service';

@Component({
  selector: 'app-history',
  templateUrl: './history.page.html',
  styleUrls: ['./history.page.scss'],
  standalone: false,
})
export class HistoryPage implements OnInit {

  public getJsonValue: any;
  public getJsonImage: any;
  public imageId: any;
    public items: any[] = [];
  public tag : any;
  public image: any;


  constructor(private activatedRoute: ActivatedRoute, private http: HttpClient, private api: ApiService, private loadingCtrl: LoadingController) { }

  async ngOnInit() {
    await this.loadData();
  }

async loadData() {
  this.tag = 'banana';
  const historyRes = await this.api.getHistory();
  const multimediaRes = await this.api.getMultimedia(this.tag); // Sin filtro
  this.image = multimediaRes.data.find((item: any) => item.type === 'image')?.url || 'assets/images/default.jpg';
  const historyData = historyRes[0].data;
  const multimediaData = multimediaRes;

  const allItems: any[] = [];

  for (const category in historyData) {
    const entries = historyData[category];

    for (const entry of entries) {
      const imageId = entry.image_id;
      const tag = entry.tag;

      const multimediaItem = multimediaData.find((item: any) => item.id === tag);
      const imageUrl = multimediaItem?.data?.find((m: any) => m.type === 'image')?.url || 'assets/images/default.jpg';

      allItems.push({
        category,
        imageId,
        description: entry.description,
        imageUrl,
        tag,
        name: tag
      });
    }
  }

  this.items = allItems;
  console.log(this.items);
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

   async showLoading() {
    const loading = await this.loadingCtrl.create({
      message: 'Dismissing after 3 seconds...',    });

    loading.present();
    loading.remove();
  }
}
