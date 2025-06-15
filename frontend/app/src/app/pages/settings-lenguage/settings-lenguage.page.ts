import { Component, OnInit } from '@angular/core';
import { TranslateService } from '@ngx-translate/core';

@Component({
  selector: 'app-settings-lenguage',
  templateUrl: './settings-lenguage.page.html',
  styleUrls: ['./settings-lenguage.page.scss'],
  standalone: false,
})
export class SettingsLenguagePage implements OnInit {

    lang:string ='';

  constructor(private translateService:TranslateService) { }

  ngOnInit(): void  {
    this.lang = localStorage.getItem('lang') || 'es';
  }

    ChangeLang(lang:any){
    const selectedLanguage = lang.target.value;
    localStorage.setItem('lang',selectedLanguage);
    this.translateService.use(selectedLanguage);

  }

}
