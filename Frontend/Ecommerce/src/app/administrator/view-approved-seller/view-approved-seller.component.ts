import { Component, OnInit } from '@angular/core';
import {EserviceService} from '../../eservice.service';


@Component({
  selector: 'app-view-approved-seller',
  templateUrl: './view-approved-seller.component.html',
  styleUrls: ['./view-approved-seller.component.css']
})
export class ViewApprovedSellerComponent implements OnInit {
  
  constructor(private service:EserviceService) { }
  SellerdataList:any=[];
  readonly APIUrl = 'http://127.0.0.1:8000';


  ngOnInit(): void {
    this.viewapprovedsellerlist()
  }
  viewapprovedsellerlist(){
    this.service.viewapprovedseller().subscribe(data=>{
    this.SellerdataList=data;
    });

}
}

