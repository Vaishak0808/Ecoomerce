import { ComponentFixture, TestBed } from '@angular/core/testing';

import { BuyShowProductdetailsComponent } from './buy-show-productdetails.component';

describe('BuyShowProductdetailsComponent', () => {
  let component: BuyShowProductdetailsComponent;
  let fixture: ComponentFixture<BuyShowProductdetailsComponent>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      declarations: [ BuyShowProductdetailsComponent ]
    })
    .compileComponents();
  });

  beforeEach(() => {
    fixture = TestBed.createComponent(BuyShowProductdetailsComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
