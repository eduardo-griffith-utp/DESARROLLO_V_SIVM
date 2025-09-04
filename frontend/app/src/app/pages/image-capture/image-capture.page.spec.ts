import { ComponentFixture, TestBed } from '@angular/core/testing';
import { ImageCapturePage } from './image-capture.page';

describe('ImageCapturePage', () => {
  let component: ImageCapturePage;
  let fixture: ComponentFixture<ImageCapturePage>;

  beforeEach(() => {
    fixture = TestBed.createComponent(ImageCapturePage);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
