import { Component, OnInit } from '@angular/core';
import { Router } from '@angular/router';
import { EserviceService } from '../eservice.service';

@Component({
  selector: 'app-productcards',
  templateUrl: './productcards.component.html',
  styleUrls: ['./productcards.component.css']
})
export class ProductcardsComponent implements OnInit { 
  ProductList:any=[];
  readonly APIUrl = 'http://127.0.0.1:8000';
  constructor(private service: EserviceService,private router:Router) {
    // this.viewAllProduct()

  }
  


  ngOnInit(): void {
    // this.viewAllProduct()
    this.service.ViewProduct().subscribe(data =>{
      this.ProductList=data;
      console.log(this.ProductList)
  
      });
    
  }
  // viewAllProduct(){
  //   this.service.ViewProduct().subscribe(data =>{
  //   this.ProductList=data;
  //   console.log(this.ProductList)
// 
  //   });
    

    // }
    viewSingleProductDetails(ProductId:any){
      console.log("buy");
      // this.router.navigate( ['/BuyProduct',ProductId]).then();
      this.router.navigateByUrl('/BuyProduct', { state: { ProductId:ProductId} })
  }


}


