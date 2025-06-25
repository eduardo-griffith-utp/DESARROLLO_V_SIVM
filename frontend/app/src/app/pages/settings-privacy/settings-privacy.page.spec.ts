import { ComponentFixture, TestBed } from '@angular/core/testing';
import { SettingsPrivacyPage } from './settings-privacy.page';

describe('SettingsPrivacyPage', () => {
  let component: SettingsPrivacyPage;
  let fixture: ComponentFixture<SettingsPrivacyPage>;

  beforeEach(() => {
    fixture = TestBed.createComponent(SettingsPrivacyPage);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
