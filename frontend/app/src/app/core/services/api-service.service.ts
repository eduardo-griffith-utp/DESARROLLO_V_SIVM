import { HttpClient } from '@angular/common/http';
import { Injectable } from '@angular/core';
import { firstValueFrom } from 'rxjs';
import { environment } from 'src/environments/environment';

@Injectable({
  providedIn: 'root'
})
export class ApiService {

  constructor(private http: HttpClient) { }


  async postItem(): Promise<any> {
    const timestamp = new Date().toISOString();

    try {
      const uniqueId = 'img_' + Math.random().toString(36).substring(2, 8);
    } catch (error){
      console.error("Error posting items")
    }
  }

  async getimages(): Promise <any> {
    try {
      const res = await firstValueFrom(this.http.get(environment.baseUrl + "/appi/v1/images"));
      return res;
    } catch (error) {
      console.error('Error fetching items:', error);
      throw error;
    }
  }

  async getItemDetails(item_id: number): Promise<any> {
    try {
      const res = await firstValueFrom(this.http.get(environment.baseUrl + "/api/v1/items/" + item_id));
      return res;
    } catch (error) {
      console.error('Error fetching items:', error);
      throw error;
    }
  }

  async getItem(): Promise<any> {
    try {
      const res = await firstValueFrom(this.http.get(environment.baseUrl +"/appi/v1/items"));
      return res;
    } catch (error) {
      console.error('Error fetching items', error);
      throw error;
    }
  }

  async getMultumedia(multimedia_tag: number): Promise <any> {
    try {
      const res = await firstValueFrom(this.http.get(environment.baseUrl + "/appi/v1/multimedia/by-tag/" + multimedia_tag));
      return res;
    } catch (error) {
      console.error('Error fetching items:', error);
      throw error;
    }
  }
  async getHistory(): Promise <any> {
    try {
      const res = await firstValueFrom(this.http.get(environment.baseUrl + "/appi/v1/history"));
      return res;
    } catch (error) {
      console.error('Error fetching items:', error);
      throw error;
    }
  }
  
  

}