import { HttpClient } from '@angular/common/http';
import { Injectable } from '@angular/core';
import { firstValueFrom } from 'rxjs';
import { environment } from 'src/environments/environment';

@Injectable({
  providedIn: 'root'
})
export class ApiService {

  constructor(private http: HttpClient) {}

  async postItem(): Promise<any> {
    const timestamp = new Date().toISOString();
    const uniqueId = 'img_' + Math.random().toString(36).substring(2, 8);

    const payload = {
      id: uniqueId,
      timestamp: timestamp,
      description: "Descripción",
      status: "processing"
    };

    try {
      const res = await firstValueFrom(this.http.post(environment.baseUrl + "/api/v1/items", payload));
      return res;
    } catch (error) {
      console.error('Error posting item:', error);
      throw error;
    }
  }

  async getImages(imageId: number): Promise<any> {
    try {
      const res = await firstValueFrom(
        this.http.get(`${environment.baseUrl}/api/v1/images/${imageId}/analysis`)
      );
      return res;
    } catch (error) {
      console.error('Error fetching image analysis:', error);
      throw error;
    }
  }

  async getItemDetails(itemId: number): Promise<any> {
    try {
      const res = await firstValueFrom(
        this.http.get(`${environment.baseUrl}/api/v1/items/${itemId}`)
      );
      return res;
    } catch (error) {
      console.error('Error fetching item details:', error);
      throw error;
    }
  }

  async getItem(): Promise<any> {
    try {
      const res = await firstValueFrom(
        this.http.get(`${environment.baseUrl}/api/v1/items`)
      );
      return res;
    } catch (error) {
      console.error('Error fetching items:', error);
      throw error;
    }
  }

  async getMultimedia(multimediaTag: number): Promise<any> {
    try {
      const res = await firstValueFrom(
        this.http.get(`${environment.baseUrl}/api/v1/multimedia/by-tag/${multimediaTag}`)
      );
      return res;
    } catch (error) {
      console.error('Error fetching multimedia:', error);
      throw error;
    }
  }

  async getHistory(): Promise<any> {
    try {
      const res = await firstValueFrom(
        this.http.get(`${environment.baseUrl}/api/v1/history`)
      );
      return res;
    } catch (error) {
      console.error('Error fetching history:', error);
      throw error;
    }
  }
}
