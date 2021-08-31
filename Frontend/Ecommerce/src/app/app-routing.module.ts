import { BuyProductPageComponent } from './buy-product-page/buy-product-page.component';
import { NgModule, Component } from '@angular/core';
import { RouterModule, Routes } from '@angular/router';
import { AdministratorComponent } from './administrator/administrator.component';
// import { SellerComponent } from './seller/seller.component';
import { CustomerComponent } from './customer/customer.component';
import { FooterComponent } from './homepage/footer/footer.component';
import { BodyComponent } from './homepage/body/body.component';
import { ViewCustomerComponent } from './administrator/view-customer/view-customer.component';
import { ViewApprovedSellerComponent } from './administrator/view-approved-seller/view-approved-seller.component';
import { ViewRequestedSellerComponent } from './administrator/view-requested-seller/view-requested-seller.component';
import { RegistrationComponent } from './customer/registration/registration.component';
import { LoginComponent } from './customer/login/login.component';
import { ViewProductsComponent } from './customer/view-products/view-products.component';
import { HomepageComponent } from './homepage/homepage.component';
import { BuyShowProductdetailsComponent } from './buy-show-productdetails/buy-show-productdetails.component';
import { ProductcardsComponent } from './productcards/productcards.component';
import { ViewProductCartComponent } from './view-product-cart/view-product-cart.component';

const routes: Routes = [
  {path:'',component:HomepageComponent},
  {path :'Placeorder/:ProductId',component:BuyProductPageComponent},
  {path:'BuyProduct/:ProductId',component:BuyShowProductdetailsComponent},
  // {path:'BuyProduct',component:BuyShowProductdetailsComponent},
  
  // {path:'Homepage',component:HomepageComponent},
  {path:'body',component:BodyComponent},
  {path:'footer',component:FooterComponent},
  {path:'myCart',component:ViewProductCartComponent},

  // {path:'Productcard',component:ProductcardsComponent,
  //   children:[
  //     {
  //       path:'BuyProduct',
  //       component:BuyShowProductdetailsComponent
  //     }
  //   ]
  // },

  {path:'administrator',component:AdministratorComponent,
    children: [
      {
        path: 'viewcustomer',
        component: ViewCustomerComponent
      },
      {
        path: 'viewapprovedseller',
        component: ViewApprovedSellerComponent
      },
      {
      path: 'viewrequestedseller',
      component: ViewRequestedSellerComponent
      }]
      }
    
  ]


@NgModule({
  imports: [RouterModule.forRoot(routes)],
  exports: [RouterModule]
})
export class AppRoutingModule { }
