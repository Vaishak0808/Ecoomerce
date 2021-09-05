import { EserviceService } from './../eservice.service';
import { Component, OnInit } from '@angular/core';

@Component({
  selector: 'app-view-customer-orders',
  templateUrl: './view-customer-orders.component.html',
  styleUrls: ['./view-customer-orders.component.css']
})
export class ViewCustomerOrdersComponent implements OnInit {
CustomerOrders :any =[]
Id : any;
readonly APIUrl = 'http://127.0.0.1:8000';
Processing :boolean = true;
Out_for_Delivery:boolean= false;
Delivered : boolean = false;
disable : boolean = false;

  constructor(private service:EserviceService) { }

  ngOnInit(): void {
    this.getOrders()
  }
  removeOrders(val:any){
    this.service.removeOrders(val).subscribe(data=>{
        alert(data.toString())
        this.getOrders()
    })
  }
  getOrders(){
    this.service.CustomerOrderDetails().subscribe(data=>
      {
        this.CustomerOrders = data
        console.log("getting order  from db-----------------------------------------------",this.CustomerOrders)

      })
  }
  ProcessingOrder(val:any){
    let OrderStatus = 'Processing'
    this.Id = val
      var details = {
        OrderId : val,
        OrderStatus : OrderStatus
        }
        console.log("details:",details)
        this.service.updateOderdStatus(details).subscribe(data =>{
          alert(data.toString())
          // this.Processing = false;
          this.Out_for_Delivery = true;
          this.getOrders()
    })

  }
  OutforDeliveryOrder(val:any){
    let OrderStatus = 'Out for Delivery'
    this.Id =val
      var details = {
        OrderId : val,
        OrderStatus : OrderStatus
        }
        console.log("details:",details)
        this.service.updateOderdStatus(details).subscribe(data =>{
          alert(data.toString())
          this.Out_for_Delivery = false;
          this.Delivered = true;

          this.getOrders()
        })

  }
  DeliveredOrder(val:any){
    let OrderStatus = 'Delivered'
    this.Id =val

      var details = {
        OrderId : val,
        OrderStatus : OrderStatus
        }
        console.log("details:",details)
        this.service.updateOderdStatus(details).subscribe(data =>{
          alert(data.toString())
          this.Delivered = false;
          this.Processing = true;
          // this.disable = true;
          this.getOrders()

        })

  }
}
