import { ComponentFixture, TestBed } from '@angular/core/testing';

import { BuyProductPageComponent } from './buy-product-page.component';

describe('BuyProductPageComponent', () => {
  let component: BuyProductPageComponent;
  let fixture: ComponentFixture<BuyProductPageComponent>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      declarations: [ BuyProductPageComponent ]
    })
    .compileComponents();
  });

  beforeEach(() => {
    fixture = TestBed.createComponent(BuyProductPageComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
