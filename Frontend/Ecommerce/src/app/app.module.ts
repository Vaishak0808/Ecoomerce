import { NgModule } from '@angular/core';
import { BrowserModule } from '@angular/platform-browser';

import { CookieService } from 'ngx-cookie-service';
import { AppRoutingModule } from './app-routing.module';
import { AppComponent } from './app.component';
import { AdministratorComponent } from './administrator/administrator.component';
import { CustomerComponent } from './customer/customer.component';
import { ViewCustomerComponent } from './administrator/view-customer/view-customer.component';
import { ViewApprovedSellerComponent } from './administrator/view-approved-seller/view-approved-seller.component';
import { ViewRequestedSellerComponent } from './administrator/view-requested-seller/view-requested-seller.component';
import { RegistrationComponent } from './customer/registration/registration.component';
import { LoginComponent } from './customer/login/login.component';
import { ViewProductsComponent } from './customer/view-products/view-products.component';
import {EserviceService} from  './eservice.service';
import {HttpClientModule} from '@angular/common/http';
import { FormsModule,ReactiveFormsModule } from '@angular/forms';
import { HomepageComponent } from './homepage/homepage.component';
import { HeaderComponent } from './homepage/header/header.component';
import { FooterComponent } from './homepage/footer/footer.component';
import { BodyComponent } from './homepage/body/body.component';
import { NgbModule } from '@ng-bootstrap/ng-bootstrap';
import { ProductcardsComponent } from './productcards/productcards.component';
import { ViewProductComponent } from './view-product/view-product.component';
import { BuyShowProductdetailsComponent } from './buy-show-productdetails/buy-show-productdetails.component';

@NgModule({
  declarations: [
    AppComponent,
    AdministratorComponent,
    CustomerComponent,
    ViewCustomerComponent,
    ViewApprovedSellerComponent,
    ViewRequestedSellerComponent,
    RegistrationComponent,
    LoginComponent,
    ViewProductsComponent,
    HomepageComponent,
    HeaderComponent,
    FooterComponent,
    BodyComponent,
    ProductcardsComponent,
    ViewProductComponent,
    BuyShowProductdetailsComponent,
    
  ],
  imports: [
    BrowserModule,
    AppRoutingModule,
    HttpClientModule,
    FormsModule,
    ReactiveFormsModule,
    NgbModule,
  ],
  providers: [EserviceService,CookieService],
  bootstrap: [AppComponent]
})
export class AppModule { }



// JSON.parse(JSON.stringify(user)).token