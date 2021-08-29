import { Component, OnInit } from '@angular/core'; 
import { FormBuilder , FormGroup } from '@angular/forms';
import {EserviceService} from  '../../eservice.service';
import { NavigationStart, Router } from '@angular/router';
import { map,filter } from 'rxjs/operators';
import {ActivatedRoute} from '@angular/router';


import { Observable } from 'rxjs';
@Component({
  selector: 'app-header',
  templateUrl: './header.component.html',
  styleUrls: ['./header.component.css']
})
export class HeaderComponent implements OnInit {
  showModal = false;
  accountModal = false;
  showdrop = false;
  showsellerloginModal = false;
  sellerregistraioModal = false;
  AddProductModal = false;
  hai:any;
  form: FormGroup | any;
  productform :FormGroup | any;
  response : any;
  FirstName :string | undefined;
  LastName :string | undefined;
  Address  :string | undefined;
  Pincode :number | undefined;
  PhoneNumber :number | undefined;
  Email:string | undefined;
  Username:string | undefined;
  Password :string | undefined;
  IdProof :string | undefined;
  Website :string | undefined;
  CompanyName : string |undefined;
  FormBuilder: any;
  username :string | undefined;
  password :string | undefined;
  isLoggedIn : boolean=false;
  token : any;
  user:any | undefined;
  userForeign :any  | undefined
  UserType :any | undefined
  checktype : any | undefined
  USERTYPE : any |undefined
  i : any |undefined
  SellProductActive: any|undefined;
  CompanyId :any |undefined;
  constructor(private formBuilder: FormBuilder,private service:EserviceService,private router:Router ,private route: ActivatedRoute) {
    this.token =localStorage.getItem("VC_CART_TOKEN")
    // console.log("id",JSON.parse(JSON.stringify(this.token)))
    if (localStorage.getItem("VC_CART_TOKEN") ) {
      this.isLoggedIn=true
    }
    if(localStorage.getItem("VC_CART_USER_TYPE")){
      this.UserType=localStorage.getItem("VC_CART_USER_TYPE")
    }
   } 
  

  ngOnInit(): void { 
        this.productform = this.formBuilder.group({
          PCategory:[''],
          PName:[''],
          PDescription:[''],
          PPhoto:[''],
          PPrice:[''],
          sellername:[''],
          
        });

        this.form = this.formBuilder.group({ 
          
          CompanyName:[''],
          PhoneNumber:[''],
          CompanyAddress:[''],
          CompanyPin:[''],
          Proof: [''],
          CompanyEmail:[''],
          CompanyWebsite:[''],  
          Email:[''],
          // UserId:[ localStorage.getItem("token")]
         });
        //  this.UserType = this.router.getCurrentNavigation()
         
        //  this.UserType = this.route.snapshot.paramMap.get("USER_TYPE")   
        // console.log("USERTYPE FROM URL",this.UserType)
    }
   
    SellProduct(){
      // console.log(this.SellProductActive)  
          localStorage.setItem('SellProductActive','show'); 
      console.log(this.SellProductActive) 
    }
    onChange(event:any){
      if(event.target.files.length >0){
        const file = event.target.files[0];
        this.form.get('Proof').setValue(file);
      }
    }
    calling(){
      console.log('lllllllllllllllllllllllllllllll')
      this.userForeign=this.service.Welcome().subscribe(res=>{
        // formData.append('UserId')
        this.hai = res 
        this.userForeign =this.hai.userid
        this.UserType = this.hai.UserType
        this.CompanyId = this.hai.CompanyId
        console.log('user-------------------------',this.userForeign,this.UserType,this.CompanyId) 
      })
    }
    onSubmit(){
      const formData = new FormData(); 
        
        formData.append('CompanyName',this.form.get('CompanyName').value);
        formData.append('CompanyAddress',this.form.get('CompanyAddress').value);
        formData.append('CompanyPin',this.form.get('CompanyPin').value);
        formData.append('CompanyPhonenumber',this.form.get('PhoneNumber').value);
        formData.append('Proof',this.form.get('Proof').value);
        formData.append('CompanyWebsite',this.form.get('CompanyWebsite').value);
        formData.append('CompanyEmail',this.form.get('Email').value);
        // formData.append('UserId',this.userForeign)
        formData.append('id',this.userForeign)
        
          
        
          this.service.SellerRegistraion(formData).subscribe(
            res=>{
              alert("Added Succefully")
            }
          ); 
       
    }
    UserRegistration(){
      var val = {
        first_name:this.FirstName,
        last_name:this.LastName,
        Address:this.Address,
        Pincode:this.Pincode,
        PhoneNumber:this.PhoneNumber,
        email:this.Email,
        username:this.Username,
        password:this.Password
      };
      this.service.CustomerRegistration(val).subscribe(res=>{
        console.log("values",val)
        alert("Created Succefully");
      })
    }   
    login(){
      var val ={
        username : this.username,
        password : this.password
      };
      this.service.logincustomer(val).subscribe(res=>{   
        this.UserType=this.service.Welcome().subscribe(res=>{ 
          this.hai = res 
          this.userForeign =this.hai.userid
          this.UserType = this.hai.UserType
          localStorage.setItem('VC_CART_ID',this.userForeign); 
          localStorage.setItem('VC_CART_USER_TYPE',this.UserType); 
          console.log('FROM HEADER  -------------->',this.userForeign,this.UserType) 
          if (this.UserType === "ADMIN"){
            // console.log("inside ADMINNN")
            this.router.navigate(['administrator']);
          }
          else{
            // console.log("iam seller")

            this.router.navigate(['/']);
            // this.router.navigate(['Homepage',{'USER_TYPE':this.UserType}]);
          }
         
        })
        })  
    }
    logout(){
      this.service.logout()
      window.location.reload();
      this.router.navigate(['/'])
    }

    // ADD Product
    
    onChangeProduct(event:any){
      if(event.target.files.length >0){
        const file = event.target.files[0];
        this.productform.get('PPhoto').setValue(file);
    }
  }
    AddProduct()
    {
      const productdata = new FormData(); 
        
        productdata.append('PCategory',this.productform.get('PCategory').value);
        productdata.append('PName',this.productform.get('PName').value);
        productdata.append('PDescription',this.productform.get('PDescription').value);
        productdata.append('PPhoto',this.productform.get('PPhoto').value);
        productdata.append('PPrice',this.productform.get('PPrice').value);
        productdata.append('sellername',this.productform.get('sellername').value);
        productdata.append('CompanyId',this.CompanyId)
        
          
        
          this.service.Addproduct(productdata).subscribe(
            res=>{
              alert("Added Succefully")
            }
          ); 

    }
}

