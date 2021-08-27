import { Component, OnInit } from '@angular/core';
import { EserviceService } from '../eservice.service';

@Component({
  selector: 'app-productcards',
  templateUrl: './productcards.component.html',
  styleUrls: ['./productcards.component.css']
})
export class ProductcardsComponent implements OnInit { 
  ProductList:any=[];
  readonly APIUrl = 'http://127.0.0.1:8000';
  constructor(private service: EserviceService) {
  }
  


  ngOnInit(): void {
    this.viewProduct()

    
  }
  viewProduct(){
    this.service.ViewProduct().subscribe(data =>{
    this.ProductList=data;
    console.log(this.ProductList)

    });
  


}
}
