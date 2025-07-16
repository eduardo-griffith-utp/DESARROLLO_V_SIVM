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

  public getJsonValue: any;
  public getJsonImage: any;
  public imageId: any;
    public items: any[] = [];
  public tag : any;
  public image: any;


  constructor(private activatedRoute: ActivatedRoute, private http: HttpClient, private api: ApiService) { }

  async ngOnInit() {
    await this.loadData();
  }

async loadData() {
  const historyRes = await this.api.getHistory();

  const allItems: any[] = [];

  for (const historyEntry of historyRes) {
    const historyData = historyEntry.data;

    for (const category in historyData) {
      const entries = historyData[category];

      for (const entry of entries) {
        const imageId = entry.image_id;
        const description = entry.description;


        const imageAnalysis = await this.api.getAnalysis(imageId);
        const tags: string[] = imageAnalysis.data.tags || [];
        const mainTag = tags[1] || tags[0];


        const multimediaItem = await this.api.getMultimedia(mainTag);
        const imageUrl = multimediaItem?.data?.find((m: any) => m.type === 'image')?.url || 'assets/images/default.jpg';
        const videoUrl = multimediaItem?.data?.find((m: any) => m.type === 'video')?.url || '';
        const audioUrl = multimediaItem?.data?.find((m: any) => m.type === 'audio')?.url || '';

        allItems.push({
          category,
          imageId,
          imageUrl,
          videoUrl,
          audioUrl,
          description,
          tag: mainTag,
          name: mainTag
        });
      }
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

   /*async showLoading() {
    const loading = await this.loadingCtrl.create({
      message: 'Dismissing after 3 seconds...',    });

    loading.present();
    loading.remove();
  }*/
}
