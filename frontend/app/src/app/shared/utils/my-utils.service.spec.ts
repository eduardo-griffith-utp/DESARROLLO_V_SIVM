import { TestBed } from '@angular/core/testing';

import { MyUtilsService } from './my-utils.service';

describe('MyUtilsService', () => {
  let service: MyUtilsService;

  beforeEach(() => {
    TestBed.configureTestingModule({});
    service = TestBed.inject(MyUtilsService);
  });

  it('should be created', () => {
    expect(service).toBeTruthy();
  });
});
