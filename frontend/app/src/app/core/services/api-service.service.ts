import { HttpClient } from '@angular/common/http';
import { Injectable } from '@angular/core';
import { firstValueFrom } from 'rxjs';
import { environment } from 'src/environments/environment';

@Injectable({
  providedIn: 'root'
})
export class ApiService {

  constructor(private http: HttpClient) {}

  async postImage(base64: string): Promise<any> {
    const payload = {
      image: base64 //this.apiService.postItem(base64DataFromCamera);

    };

    try {
      const res: any = await firstValueFrom(this.http.post(environment.baseUrl + "/api/v1/images/capture", payload));
      if (res.status === 'success') {
        console.log('Imagen recibida y procesada correctamente');
        console.log('ID de imagen:', res.data.image_id);
        console.log('Timestamp:', res.data.timestamp);
      } else if(res.status === 'processing'){
        console.log('Imagen procesandose');
      }

      return res;
      //return this.http.post<any> ("/api/v1/images/capture", payload).toPromise();
      

    } catch (error: any) {
      if (error.status === 400) {
        console.error('Error 400 - Solicitud mal formada');
      } else if (error.status === 404) {
        console.error('Error 404 - Recurso no encontrado');
      } else if (error.status === 500) {
        console.error('Error 500 - Error interno del servidor');
      } else {
        console.error('Error desconocido:', error);
      }

      throw error;
    }
  }

  async getImage(imageId: string): Promise<any> {
    try {
      //const res = await firstValueFrom(this.http.get(`${environment.baseUrl}/api/v1/images/${imageId}/analysis`));

      //De esta forma se filtra el id manualmente
      const url = `${environment.baseUrl}/api/v1/images/${imageId}/analysis`;
      const res = await firstValueFrom(this.http.get<any[]>(url));
      
      if (!res.length) {
        throw new Error(`Imagen con ID ${imageId} no encontrada`);
      }
      return res[0];
    } catch (error) {
      console.error('Error analizando el id:', error);
      throw error;
    }
  }

  async getItemDetails(itemId: string): Promise<any> {
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

  async getMultimedia(multimediaTag: string): Promise<any> {
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
