import { ComponentFixture, TestBed } from '@angular/core/testing';

import { ViewProductCartComponent } from './view-product-cart.component';

describe('ViewProductCartComponent', () => {
  let component: ViewProductCartComponent;
  let fixture: ComponentFixture<ViewProductCartComponent>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      declarations: [ ViewProductCartComponent ]
    })
    .compileComponents();
  });

  beforeEach(() => {
    fixture = TestBed.createComponent(ViewProductCartComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
