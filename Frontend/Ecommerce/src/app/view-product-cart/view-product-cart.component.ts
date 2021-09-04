import { Component, OnInit } from '@angular/core';
import { EserviceService } from '../eservice.service';
@Component({
  selector: 'app-view-product-cart',
  templateUrl: './view-product-cart.component.html',
  styleUrls: ['./view-product-cart.component.css']
})
export class ViewProductCartComponent implements OnInit {
readonly APIUrl = 'http://127.0.0.1:8000';
cartList :any=[]
userid:any|undefined;
data:any|undefined;
cart: any=[]
product:any=[]
constructor(private service:EserviceService) { }

  ngOnInit(): void {
    this.getcartdetails()
} 
deleteCartProduct(id:any){
    this.service.deleteCartProduct(id).subscribe(res=>{
      alert(res.toString())
      this.getcartdetails()
    })
    
  }
  


getcartdetails(){
    if (localStorage.getItem("VC_CART_TOKEN") ) {
    this.service.getCartDetails().subscribe(res=>{
    this.cart = res;
  
  console.log(res)
})
}
}
}


