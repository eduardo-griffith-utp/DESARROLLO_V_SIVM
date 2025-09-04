import { ComponentFixture, TestBed } from '@angular/core/testing';
import { ItemDetailsPage } from './item-details.page';

describe('ItemDetailsPage', () => {
  let component: ItemDetailsPage;
  let fixture: ComponentFixture<ItemDetailsPage>;

  beforeEach(() => {
    fixture = TestBed.createComponent(ItemDetailsPage);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
