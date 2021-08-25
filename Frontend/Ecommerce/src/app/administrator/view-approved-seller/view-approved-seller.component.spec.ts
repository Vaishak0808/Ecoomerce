import { ComponentFixture, TestBed } from '@angular/core/testing';

import { ViewApprovedSellerComponent } from './view-approved-seller.component';

describe('ViewApprovedSellerComponent', () => {
  let component: ViewApprovedSellerComponent;
  let fixture: ComponentFixture<ViewApprovedSellerComponent>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      declarations: [ ViewApprovedSellerComponent ]
    })
    .compileComponents();
  });

  beforeEach(() => {
    fixture = TestBed.createComponent(ViewApprovedSellerComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
