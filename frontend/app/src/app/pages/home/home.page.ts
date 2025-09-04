import { Component, OnInit } from '@angular/core';
import { HttpClient } from '@angular/common/http'

@Component({
  selector: 'app-home', // El selector ahora es 'app-home'
  templateUrl: './home.page.html', // Asumiendo que tu HTML se llama 'home.page.html'
  styleUrls: ['./home.page.scss'], // Asumiendo que tus estilos se llaman 'home.page.scss'
  standalone: false,
})
export class HomePage implements OnInit { // La clase ahora se llama 'HomePage'

  constructor(
    private http: HttpClient
  ) { }

  ngOnInit() {
    this.http.get('http://localhost:3000/Imagen')
      .subscribe(res => {
        console.log(res);
      })
  }

  scanear() { // El nombre de la función se mantiene igual, asumiendo que su lógica sigue siendo relevante en la página de inicio
    console.log('Función de escaneo activada desde la página de inicio');
    // Aquí iría la lógica para iniciar el escaneo (por ejemplo, usando un plugin como Capacitor Barcode)
  }

}