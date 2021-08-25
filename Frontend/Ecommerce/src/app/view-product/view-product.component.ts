import { Component, OnInit } from '@angular/core';
import {EserviceService} from '../eservice.service';

@Component({
  selector: 'app-view-product',
  templateUrl: './view-product.component.html',
  styleUrls: ['./view-product.component.css']
})
export class ViewProductComponent implements OnInit {
  view_product_list:any=[]
  constructor(private service:EserviceService) { }

  ngOnInit(): void {
    this.viewproductdetails()
  }

  viewproductdetails(){
    this.service.ViewProduct().subscribe(data =>{
      this.view_product_list=data;
    });
  }
}
