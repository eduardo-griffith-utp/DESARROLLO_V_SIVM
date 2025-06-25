import { ComponentFixture, TestBed } from '@angular/core/testing';
import { SettingsLenguagePage } from './settings-lenguage.page';

describe('SettingsLenguagePage', () => {
  let component: SettingsLenguagePage;
  let fixture: ComponentFixture<SettingsLenguagePage>;

  beforeEach(() => {
    fixture = TestBed.createComponent(SettingsLenguagePage);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
