import { NgModule } from '@angular/core';
import { RouterModule, Routes } from '@angular/router';
import { AdministratorComponent } from './administrator/administrator.component';
// import { SellerComponent } from './seller/seller.component';
import { CustomerComponent } from './customer/customer.component';
import { ViewCustomerComponent } from './administrator/view-customer/view-customer.component';
import { ViewApprovedSellerComponent } from './administrator/view-approved-seller/view-approved-seller.component';
import { ViewRequestedSellerComponent } from './administrator/view-requested-seller/view-requested-seller.component';
import { RegistrationComponent } from './customer/registration/registration.component';
import { LoginComponent } from './customer/login/login.component';
import { ViewProductsComponent } from './customer/view-products/view-products.component';
import { HomepageComponent } from './homepage/homepage.component';


const routes: Routes = [
  {path:'',component:HomepageComponent},
  {path:'Homepage',component:HomepageComponent},
  {path:'administrator',component:AdministratorComponent,
    children: [
      {
        path: 'viewcustomer',
        component: ViewCustomerComponent,
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
