import { HttpClient } from '@angular/common/http';
import { Injectable } from '@angular/core';
import { firstValueFrom } from 'rxjs';
import { environment } from 'src/environments/environment';
import { AbstractApiService } from './abstract-api.service'; // si usas la interfaz

@Injectable({
  providedIn: 'root'
})
export class MockApiService extends AbstractApiService {

  private mockBaseUrl = environment.mockBaseUrl || 'http://localhost:3000';

  constructor(private http: HttpClient) {
    super();
  }

  async postImage(base64Image: string): Promise<any> {
    const payload = {
      image: base64Image,
      timestamp: Date.now()
    };

    // Simula "guardar" la imagen en /images
    return await firstValueFrom(this.http.post(`${environment.mockBaseUrl}/images`, payload));
  }

  async getImage(imageId: string): Promise<any> {
    return await firstValueFrom(this.http.get(`${environment.mockBaseUrl}/images/${imageId}/analysis`));
  }

  async getItemDetails(itemId: string): Promise<any> {
    return await firstValueFrom(this.http.get(`${environment.mockBaseUrl}/items/${itemId}`));
  }

  async getItem(): Promise<any> {
    return await firstValueFrom(this.http.get(`${environment.mockBaseUrl}/items`));
  }

  async getMultimedia(multimediaTag: string): Promise<any> {
    // No hay "by-tag" en json-server, pero puedes simularlo así:
    return await firstValueFrom(this.http.get(`${environment.mockBaseUrl}/multimedia/${multimediaTag}`));
  }

  async getHistory(): Promise<any> {
    return await firstValueFrom(this.http.get(`${environment.mockBaseUrl}/history`));
  }
}
