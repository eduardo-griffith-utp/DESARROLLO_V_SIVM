import { NgModule } from '@angular/core';
import { CommonModule } from '@angular/common';
import { FormsModule } from '@angular/forms';

import { IonicModule } from '@ionic/angular';

import { HistoryNidPageModule } from './history-nid-routing.module';

import { historyNidPage } from './history-nid.page';

@NgModule({
  imports: [
    CommonModule,
    FormsModule,
    IonicModule,
    HistoryNidPageModule
  ],
  declarations: [historyNidPage]
})
export class historyNidPageModule {}
