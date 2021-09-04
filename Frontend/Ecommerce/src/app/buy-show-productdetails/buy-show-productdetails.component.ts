import { Component, Input, OnInit } from '@angular/core';
import { ActivatedRoute, Router } from '@angular/router';
import { EserviceService } from '../eservice.service'; 

@Component({
  selector: 'app-buy-show-productdetails',
  templateUrl: './buy-show-productdetails.component.html',
  styleUrls: ['./buy-show-productdetails.component.css']
})
export class BuyShowProductdetailsComponent implements OnInit {

readonly APIUrl = 'http://127.0.0.1:8000';

USER_TOKEN :boolean=false;;
listofproduct :any =[]; 
response :any |undefined;
userid :any |undefined;
  constructor(private service: EserviceService,private route: ActivatedRoute,private router:Router) { }

  ngOnInit(): void {
    if(localStorage.getItem("VC_CART_TOKEN")){
      this.USER_TOKEN =true
    }
    let id = this.route.snapshot.params.ProductId; 
    this.service.viewSingleProduct(id).subscribe(data =>{
      this.listofproduct=data;

      console.log("singledata",data)
    }) 
  }
  addToCart(){
   
    if(localStorage.getItem("VC_CART_TOKEN")){
      this.service.Welcome().subscribe(res=>{ 
        this.response = res
        this.userid = this.response.userid       
        var val = {
        Quantity:1,
        ProductId:this.route.snapshot.params.ProductId,
        id:this.userid
      }
        this.service.AddToCart(val).subscribe(res=>{
           
      })
     })
    }
    else{
      alert("PLease Login")
    }
  } 
  
}

