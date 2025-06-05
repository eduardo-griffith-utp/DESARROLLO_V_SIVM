import { Injectable } from '@angular/core';

import { HttpClient, HttpEvent, HttpHandler, HttpInterceptor, HttpRequest, HttpResponse} from '@angular/common/http'
import { Observable, of } from 'rxjs';


@Injectable({
  providedIn: 'root'
})


export class ServicesService implements HttpInterceptor {
  private apiUrl = 'http://localhost:3000/api'
  constructor() { }
  intercept(request: HttpRequest<any>, next: HttpHandler): Observable<HttpEvent<any>> {
    
    const mockResponse = this.getMockResponse(request);

    if (mockResponse) {
      return of(new HttpResponse({
        status: 200,
        body: mockResponse
      }));
    }

    return next.handle(request);
  }

  private getMockResponse(request: HttpRequest<any>): any {
  
    // Lógica para determinar qué respuesta mock enviar
    // basada en la URL y método de la petición
  }

}
