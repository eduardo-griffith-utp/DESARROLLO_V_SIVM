import { NgModule } from '@angular/core';
import { Routes, RouterModule } from '@angular/router';

import { historyNidPage } from './history-nid.page';

const routes: Routes = [
  {
    path: '',
    component: historyNidPage
  }
];

@NgModule({
  imports: [RouterModule.forChild(routes)],
  exports: [RouterModule],
})
export class HistoryNidPageModule {}
