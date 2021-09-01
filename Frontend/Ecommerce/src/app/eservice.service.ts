import { Injectable } from '@angular/core';
import { HttpClient, HttpHeaders } from '@angular/common/http';
import { Observable } from 'rxjs';
import { CookieService } from 'ngx-cookie-service';
import { map,filter } from 'rxjs/operators';

@Injectable({
  providedIn: 'root'
})
export class EserviceService {
result_TOKEN : any;
passing_Token : any;
value:any;
CART_DATA :any;
token :any ;
  readonly APIUrl = 'http://127.0.0.1:8000';
 
  constructor(private http:HttpClient,private cookieService: CookieService) { }
  

  // ADMIN 
  viewcustomer():Observable<any[]>{
    return this.http.get<any[]>(this.APIUrl+'/ViewCustomer/');
  }
  viewSellertoApprove():Observable<any[]>{
    return this.http.get<any[]>(this.APIUrl+'/ViewSellerToApproveDetails/');
  }
  viewapprovedseller():Observable<any[]>{
    return this.http.get<any[]>(this.APIUrl+'/ViewApprovedSellerDetails/');
  }
  AcceptSeller(val:any){
    return this.http.put(this.APIUrl+'/ViewSellerToApproveDetails/',val)
  }
  Rejectseller(val:any){
    console.log('calling service')
    return this.http.delete(this.APIUrl+'/ViewSellerToApproveDetails/',val);
  }
  // CUSTOMER
  CustomerRegistration(val:any){
    return this.http.post(this.APIUrl+'/customerregistration/',val);
  }
  logincustomer(val:any){ 
    return this.http.post(this.APIUrl+'/login/',val).
    pipe(
      map(user  =>{ 
        if(user){
          // console.log(user)
           this.result_TOKEN =JSON.parse(JSON.stringify(user)).token
          // console.log('--------------',this.result_TOKEN)
          this.cookieService.set('VC_CART_TOKEN',this.result_TOKEN);
          localStorage.setItem('VC_CART_TOKEN',this.result_TOKEN); 
          window.sessionStorage.setItem("VC_CART_TOKEN", this.result_TOKEN);  

        }
      }
      
      )
    );
  }
  logout(){
    localStorage.removeItem("VC_CART_TOKEN");
    this.cookieService.delete('VC_CART_TOKEN');
    window.sessionStorage.removeItem("VC_CART_TOKEN");

    
    localStorage.removeItem('VC_CART_ID'); 
    localStorage.removeItem('VC_CART_USER_TYPE'); 
  }


  // SELLER

 SellerRegistraion(formdata:any){
    // this.result_TOKEN = localStorage.getItem('VC_CART_TOKEN')
    // this.passing_Token={"LOGIN_TOKEN":this.result_TOKEN } 
    // console.log('seller reg' ,this.result_TOKEN)
    return this.http.post(this.APIUrl+'/sellerregistrations/',formdata )
    // return this.http.post(this.APIUrl+'/sellerregistrations/',formdata,{headers: new HttpHeaders().set('Authorization',this.result_TOKEN) })
    
  }
  Welcome(){
    this.result_TOKEN = localStorage.getItem('VC_CART_TOKEN')
    this.token = `Token `+ this.result_TOKEN
    // console.log(this.token)
    return this.http.get(this.APIUrl+'/Welcome/',{headers: new HttpHeaders().set('Authorization',this.token)})

  }
  ViewProduct():Observable<any[]>{
    return this.http.get<any[]>(this.APIUrl+'/AddProduct/');
  }
  Addproduct(formdata:any){
    return this.http.post(this.APIUrl+'/AddProduct/',formdata);
  }
  viewSingleProduct(data:any){
    return this.http.get<any[]>(this.APIUrl+'/GetSingleProduct/'+data);
  }

// Cart
 AddToCart(data:any){
  
   return this.http.post(this.APIUrl+'/AddToCart/',data);
 }
 getCartDetails(){
  this.result_TOKEN = localStorage.getItem('VC_CART_TOKEN')
  this.token = `Token`+ this.result_TOKEN
  console.log("token:",this.token)
  //  return this.http.get(this.APIUrl+'/AddToCart/',{headers: new HttpHeaders().set('Authorization',this.token)});
  return this.http.get(this.APIUrl+'/AddToCart/',{headers: new HttpHeaders().set('Authorization',this.token)})
  
 }
 GetUserAndProduct(data:any){
  // console.log(this.result_TOKEN)
  return this.http.get<any[]>(this.APIUrl+'/GetUserAndProduct/'+data)
 }
 AddOrders(data:any){
   return this.http.post(this.APIUrl+'/PlaceOrder/',data)
 }
 MyOrder(){
     return this.http.get(this.APIUrl+'/myOrders/')
 }
CustomerOrderDetails(){
  return this.http.get(this.APIUrl+'/PlaceOrder/')
}

}
