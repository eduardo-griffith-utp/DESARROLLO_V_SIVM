import { Component } from '@angular/core';
@Component({
  selector: 'app-root',
  templateUrl: 'app.component.html',
  styleUrls: ['app.component.scss'],
  standalone: false,
})
export class AppComponent {
  public progress = 0;

  constructor() {
    setInterval(() => {
      this.progress += 0.01;

      /*if (this.progress > 1) {
        setTimeout(() => {
          this.progress = 0;
        }, 1000);
      }*/
    }, 50);
  }
  
}
