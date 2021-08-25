import { ComponentFixture, TestBed } from '@angular/core/testing';

import { ViewRequestedSellerComponent } from './view-requested-seller.component';

describe('ViewRequestedSellerComponent', () => {
  let component: ViewRequestedSellerComponent;
  let fixture: ComponentFixture<ViewRequestedSellerComponent>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      declarations: [ ViewRequestedSellerComponent ]
    })
    .compileComponents();
  });

  beforeEach(() => {
    fixture = TestBed.createComponent(ViewRequestedSellerComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
