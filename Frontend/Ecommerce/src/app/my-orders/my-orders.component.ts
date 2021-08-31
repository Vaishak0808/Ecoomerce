import { EserviceService } from './../eservice.service';
import { Component, OnInit } from '@angular/core';

@Component({
  selector: 'app-my-orders',
  templateUrl: './my-orders.component.html',
  styleUrls: ['./my-orders.component.css']
})
export class MyOrdersComponent implements OnInit {

Myorder :any =[]
readonly APIUrl = 'http://127.0.0.1:8000';
constructor(private service:EserviceService) { }

  ngOnInit(): void {
    this.service.MyOrder().subscribe(data =>
      {
         this.Myorder = data
         console.log("MYORDERS",this.Myorder)
      })
  }
  CancelOrder(){
    
  }
}
