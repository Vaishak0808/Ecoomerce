import { Component, OnInit } from '@angular/core';

@Component({
  selector: 'app-homepage',
  templateUrl: './homepage.component.html',
  styleUrls: ['./homepage.component.css']
})
export class HomepageComponent implements OnInit {

  showSellProduct : boolean=false;
  constructor() { 
     
    if (localStorage.getItem("SellProductActive") ===  'show' ) {
      this.showSellProduct = true 
    }
  }

  ngOnInit(): void {
  }
  
}
