import { ComponentFixture, TestBed } from '@angular/core/testing';
import { RouterModule } from '@angular/router';
import { IonicModule } from '@ionic/angular';

import { historyNidPage } from './history-nid.page';

describe('historyNidPage', () => {
  let component: historyNidPage;
  let fixture: ComponentFixture<historyNidPage>;

  beforeEach(async () => {
    fixture = TestBed.createComponent(historyNidPage);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
