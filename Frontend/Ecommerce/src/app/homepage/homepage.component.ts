import { Component, OnInit } from '@angular/core';

@Component({
  selector: 'app-homepage',
  templateUrl: './homepage.component.html',
  styleUrls: ['./homepage.component.css']
})
export class HomepageComponent implements OnInit {

  constructor() { 
    if (localStorage.getItem("VC_CART_USER_TYPE") ) {
      console.log('HOME-------------',localStorage.getItem("VC_CART_USER_TYPE") )
    }
  }

  ngOnInit(): void {
  }
  
}
