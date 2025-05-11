import { NgModule } from '@angular/core';
import { PreloadAllModules, RouterModule, Routes } from '@angular/router';

const routes: Routes = [
  {
    path: '',
    redirectTo: 'home',
    pathMatch: 'full'
  },
  {
    path: 'home',
    loadChildren: () => import('./pages/home/home.module').then( m => m.HomePageModule)
  },
  {
    path: 'image-capture',
    loadChildren: () => import('./pages/image-capture/image-capture.module').then( m => m.ImageCapturePageModule)
  },
  {
    path: 'recognition-results',
    loadChildren: () => import('./pages/recognition-results/recognition-results.module').then( m => m.RecognitionResultsPageModule)
  },
  {
    path: 'item-details',
    loadChildren: () => import('./pages/item-details/item-details.module').then( m => m.ItemDetailsPageModule)
  },
  {
    path: 'history',
    loadChildren: () => import('./pages/history/history.module').then( m => m.HistoryPageModule)
  },
  {
    path: 'settings',
    loadChildren: () => import('./pages/settings/settings.module').then( m => m.SettingsPageModule)
  },
  
  {
    path: 'settings-privacy',
    loadChildren: () => import('./pages/settings-privacy/settings-privacy.module').then( m => m.SettingsPrivacyPageModule)
  },
  
  {
    path: 'settings-lenguage',
    loadChildren: () => import('./pages/settings-lenguage/settings-lenguage.module').then( m => m.SettingsLenguagePageModule)
  },



];

@NgModule({
  imports: [
    RouterModule.forRoot(routes, { preloadingStrategy: PreloadAllModules })
  ],
  exports: [RouterModule]
})
export class AppRoutingModule {}
