import { Component, Input, OnInit } from '@angular/core';
import { ActivatedRoute } from '@angular/router';
import { EserviceService } from '../eservice.service';


@Component({
  selector: 'app-buy-show-productdetails',
  templateUrl: './buy-show-productdetails.component.html',
  styleUrls: ['./buy-show-productdetails.component.css']
})
export class BuyShowProductdetailsComponent implements OnInit {

readonly APIUrl = 'http://127.0.0.1:8000';

listofproduct :any =[]; 
response :any |undefined;
userid :any |undefined;
  constructor(private service: EserviceService,private route: ActivatedRoute) { }

  ngOnInit(): void {
    let id = this.route.snapshot.params.ProductId; 
    this.service.viewSingleProduct(id).subscribe(data =>{
      this.listofproduct=data;
      // console.log("singledata",data)
    }) 
  }
  addToCart(){
   
    if(localStorage.getItem("VC_CART_TOKEN")){
      this.service.Welcome().subscribe(res=>{ 
        this.response = res
        this.userid = this.response.userid
        // console.log("userid :",this.userid)
        // console.log("pId :",this.route.snapshot.params.ProductId)
      
        var val = {
        Quantity:2,
        ProductId:this.route.snapshot.params.ProductId,
        id:this.userid
      }
      // console.log("SENDING CART DATA",val)
    
      this.service.AddToCart(val).subscribe(res=>{
        alert(res.toString())
      })
     })
    }
    else{
      alert("PLease Login")
    }
  }
  
}

