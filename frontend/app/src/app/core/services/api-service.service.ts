import { HttpClient } from '@angular/common/http';
import { Injectable } from '@angular/core';
import { firstValueFrom } from 'rxjs';
import { environment } from 'src/environments/environment';

@Injectable({
  providedIn: 'root'
})
export class ApiService {

  constructor(private http: HttpClient) { }

  async getItem(item_id: number): Promise<any> {
    try {
      const res = await firstValueFrom(this.http.get(environment.baseUrl + "/api/v1/items/" + item_id));
      return res;
    } catch (error) {
      console.error('Error fetching items:', error);
      throw error;
    }
  }
}