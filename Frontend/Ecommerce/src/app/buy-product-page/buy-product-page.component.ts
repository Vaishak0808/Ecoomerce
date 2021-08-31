import { EserviceService } from './../eservice.service';
import { Component, OnInit } from '@angular/core';
import { ActivatedRoute } from '@angular/router';



@Component({
  selector: 'app-buy-product-page',
  templateUrl: './buy-product-page.component.html',
  styleUrls: ['./buy-product-page.component.css']
})
export class BuyProductPageComponent implements OnInit {

readonly APIUrl = 'http://127.0.0.1:8000';
listofproduct : any = []
state : boolean = false;
Pincode : any;
Phonenumber:any;
Address :any;
count = 1;
totalprice :any;

  constructor(private service:EserviceService,private route: ActivatedRoute) { 
    
  }

  ngOnInit(): void {
    if(localStorage.getItem("VC_CART_TOKEN")){

    let id = this.route.snapshot.params.ProductId; 
    this.service.GetUserAndProduct(id).subscribe(data =>{
    this.listofproduct=data;
    console.log(this.listofproduct)
    this.Address = this.listofproduct.userdetails.Address
    console.log("address =",this.Address)
    this.Pincode = this.listofproduct.userdetails.Pincode
    console.log("Pincode =",this.Pincode)
    this.totalprice = this.listofproduct.product.PPrice
    console.log("price",this.totalprice)

    this.Phonenumber = this.listofproduct.userdetails.PhoneNumber
    console.log("Phonenumber =",this.Phonenumber)


  })}
}
changeaddress(){
  this.state = true
}
updatestate(){
  this.state = false
}
sub(){
  
  if (this.count>1){
      this.count = this.count - 1
      this.totalprice = parseInt(this.totalprice )-parseInt( this.listofproduct.product.PPrice)
  }
}
add(){
  this.count = this. count + 1
  this.totalprice = parseInt(this.totalprice )+ parseInt(this.listofproduct.product.PPrice)
}
placeorder(){
  var val ={
    Quantity : this.count,
    CustomerId : this.listofproduct.userdetails.id ,
    ProductId : this.listofproduct.product.ProductId ,
    Address : this.Address,
    TotalPrice : this.totalprice,
    Phonenumber: this.Phonenumber,
    PinCode : this.Pincode


  }
  this.service.AddOrders(val).subscribe(res=>{
    alert(res.toString())
  })

}
}
