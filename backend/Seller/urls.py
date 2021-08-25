from Seller.views import *
from django.conf.urls import include, url

# from rest_framework import routers
from rest_framework.authtoken.views import ObtainAuthToken


# router = routers.DefaultRouter() 
urlpatterns = [
    #sellerRegistration
    
    # url(r'^',include(router.urls)),
    
    # url(r'^sellerregistration/$',sellerregistration,name="sellerregistration"),
    # url(r'^sellerregistration/([0-9]+)$',sellerregistration,name="sellerregistration"), 
    url(r'^sellerregistrations/$',sellerregistrations.as_view()),

    # Add,delete,update Product
    url(r'AddProduct/$',addproducts.as_view()),
    # url(r'^AddProduct/$',AddProducts), 
    # url(r'^AddProduct/([0-9]+)$',AddProducts),

    # url(r'^auth/',ObtainAuthToken.as_view()) , 
    
] 