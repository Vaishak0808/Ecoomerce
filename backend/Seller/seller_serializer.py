from typing import Tuple
from django.db.models import fields
from rest_framework import serializers
from Seller.models import  RegistrationDataTable, SellerProductDetails, SellerRegistration 
from Seller.models import *
from Customer.customer_serializer import *

class SellerProductDetailsSerializer(serializers.ModelSerializer): 
    # PId =  ProductCartSerializer(read_only = True , many=True)
    class Meta:
        model = SellerProductDetails
        fields = "__all__"

class SellerSingleProductDetailsSerializer(serializers.ModelSerializer): 
    class Meta:
        model = SellerProductDetails
        fields = "__all__"

class SellerRegistrationSerializer(serializers.ModelSerializer): 
    sellerid = SellerProductDetailsSerializer (read_only = True , many=True)
    class Meta:
        model = SellerRegistration 
        fields ="__all__"
 
class SellerUpdationRegistrationSerializer(serializers.ModelSerializer):
    class Meta:
        model = SellerRegistration
        fields = ( "id" ,  "Status")
class CustomerUpdationSerializser(serializers.ModelSerializer):
    class Meta:
        model =  RegistrationDataTable
        fields = ("UserType",)
# class ProductOrderDetailsDetailsSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = ProductOrderDetails
#         fields = ('Quantity','OrderDate')