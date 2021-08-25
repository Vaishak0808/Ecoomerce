import { Component, OnInit } from '@angular/core';
import {EserviceService} from '../../eservice.service';


@Component({
  selector: 'app-view-requested-seller',
  templateUrl: './view-requested-seller.component.html',
  styleUrls: ['./view-requested-seller.component.css']
})
export class ViewRequestedSellerComponent implements OnInit {

  UserType = 'Seller'

  constructor(private service:EserviceService) {

   }
  SellerList:any=[];
  readonly APIUrl = 'http://127.0.0.1:8000';
  Status=true;
  ngOnInit(): void {
    this.viewSellerlist();
  }

  viewSellerlist(){
    this.service.viewSellertoApprove().subscribe(data =>{
      this.SellerList=data;
      console.log(this.SellerList)
    });
   }
  AcceptSeller(data:any){
    var val={
      id:data,
      Status:this.Status,
      UserType:this.UserType
    };
    this.service.AcceptSeller(val).subscribe(res=>{
      alert(res)

    }); 
    this.viewSellerlist(); 
  }
  RejectSeller(data:any){
    console.log('Calling reject sellr',data)
    var val={
      CompanyId:data
    } 
    // var val = data
    console.log(val) 
    this.service.Rejectseller(val).subscribe(res=>{
      alert("Do you?")
    }); 
      this.viewSellerlist(); 


  }
  

}
