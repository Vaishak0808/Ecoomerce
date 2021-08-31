import { ComponentFixture, TestBed } from '@angular/core/testing';

import { ViewCustomerOrdersComponent } from './view-customer-orders.component';

describe('ViewCustomerOrdersComponent', () => {
  let component: ViewCustomerOrdersComponent;
  let fixture: ComponentFixture<ViewCustomerOrdersComponent>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      declarations: [ ViewCustomerOrdersComponent ]
    })
    .compileComponents();
  });

  beforeEach(() => {
    fixture = TestBed.createComponent(ViewCustomerOrdersComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
