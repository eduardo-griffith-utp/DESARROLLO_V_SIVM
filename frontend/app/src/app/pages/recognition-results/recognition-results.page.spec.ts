import { ComponentFixture, TestBed } from '@angular/core/testing';
import { RecognitionResultsPage } from './recognition-results.page';

describe('RecognitionResultsPage', () => {
  let component: RecognitionResultsPage;
  let fixture: ComponentFixture<RecognitionResultsPage>;

  beforeEach(() => {
    fixture = TestBed.createComponent(RecognitionResultsPage);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
