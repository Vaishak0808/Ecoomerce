import { EserviceService } from './../eservice.service';
import { Component, OnInit } from '@angular/core';

@Component({
  selector: 'app-view-customer-orders',
  templateUrl: './view-customer-orders.component.html',
  styleUrls: ['./view-customer-orders.component.css']
})
export class ViewCustomerOrdersComponent implements OnInit {
CustomerOrders :any =[]
readonly APIUrl = 'http://127.0.0.1:8000';

  constructor(private service:EserviceService) { }

  ngOnInit(): void {
    this.service.CustomerOrderDetails().subscribe(data=>
      {
        this.CustomerOrders = data
        console.log("getting order  from db-----------------------------------------------",this.CustomerOrders)

      })
  }

}
