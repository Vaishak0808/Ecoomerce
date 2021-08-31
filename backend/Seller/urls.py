from Seller.views import *
from django.conf.urls import include, url;
from django.urls import path
# from rest_framework import routers
# from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.authtoken.views import obtain_auth_token



# router = routers.DefaultRouter() 
urlpatterns = [
    #sellerRegistration
    
    # url(r'^',include(router.urls)),
    
    # url(r'^sellerregistration/$',sellerregistration,name="sellerregistration"),
    # url(r'^sellerregistration/([0-9]+)$',sellerregistration,name="sellerregistration"), 
    url(r'^sellerregistrations/$',sellerregistrations.as_view()),

    # Add,delete,update Product
    url(r'AddProduct/',addproducts.as_view()),
    
    path('GetSingleProduct/<str:id>/',GetSingleProduct),
    path('GetUserAndProduct/<str:id>/',getUserAndProduct.as_view()),

    path('AddToCart/',viewCartProduct.as_view()),

      url(r'^feedback/$',productfeedback),
      url(r'^feedback/([0-9]+)$',productfeedback),
      url(r'^customerregistration/$',customerregistration.as_view()), 
      url(r'^Welcome/',Welcome.as_view()),

      url(r'^login/',obtain_auth_token,name="login"),


      url('PlaceOrder/',PlaceOrder.as_view()),
      url('myOrders/',myOrders.as_view()),
] 