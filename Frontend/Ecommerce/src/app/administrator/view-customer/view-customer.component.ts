import { Component, OnInit } from '@angular/core';
import {EserviceService} from '../../eservice.service';
@Component({
  selector: 'app-view-customer',
  templateUrl: './view-customer.component.html',
  styleUrls: ['./view-customer.component.css']
})
export class ViewCustomerComponent implements OnInit {

  constructor(private service:EserviceService) {
   }
  CustomerList:any=[];


  ngOnInit(): void {
    this.viewcustomerlist();
  }


  viewcustomerlist(){
    this.service.viewcustomer().subscribe(data =>{
      this.CustomerList=data;
    });
  }
}
