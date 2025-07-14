import { Component, OnInit } from '@angular/core';
import { ActivatedRoute } from '@angular/router';  // Importa ActivatedRoute para acceder a los parámetros
import { NavController } from '@ionic/angular';
import { HttpClient } from '@angular/common/http';
import { AbstractApiService } from 'src/app/core/services/abstract-api.service';

@Component({
  selector: 'app-history',
  templateUrl: './history.page.html',
  styleUrls: ['./history.page.scss'],
  standalone: false,
})
export class HistoryPage implements OnInit {

  public getJsonValue: any;
  public getJsonImage: any;
    public items: any[] = [];


  constructor(private activatedRoute: ActivatedRoute, private http: HttpClient, private api: AbstractApiService) { }

  async ngOnInit() {
    await this.loadData();
  }

async loadData() {
  const historyRes = await this.api.getHistory();
  const multimediaRes = await this.api.getMultimedia(''); // Sin filtro

    const multimediaData = multimediaRes;

    const allItems: any[] = [];

    for (const historyEntry of historyRes) {
      const historyData = historyEntry.data;

      for (const category in historyData) {
        const entries = historyData[category];

        for (const entry of entries) {
          const imageId = entry.image_id;
          const tag = entry.tag;

          const multimediaItem = multimediaData.find((item: any) => item.id === tag);
          const imageUrl = multimediaItem?.data?.find((m: any) => m.type === 'image')?.url || 'assets/images/default.jpg';
          //const videoUrl = multimediaItem?.data?.find((m: any) => m.type === 'video')?.url || 'assets/video/default-video.mp4';

          const normalizedtag = tag.toLowerCase();

          allItems.push({
            category,
            imageId,
            //description: entry.description,
            description: `${normalizedtag}_desc`,
            imageUrl,
            tag, //: normalizedtag,
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
}}
