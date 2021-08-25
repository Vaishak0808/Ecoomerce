import { Component, OnInit } from '@angular/core';

@Component({
  selector: 'app-productcards',
  templateUrl: './productcards.component.html',
  styleUrls: ['./productcards.component.css']
})
export class ProductcardsComponent implements OnInit {

  constructor() {
    
   }

  ngOnInit(): void {
    
  }

  listofcards = ["1","2","3",'4','5','6','7',"1","2","3",'4','5','6','7']
}
