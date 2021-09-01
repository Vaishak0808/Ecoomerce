from typing import Tuple
from django.db.models import fields
from rest_framework import serializers
from Seller.models import  RegistrationDataTable, SellerProductDetails, SellerRegistration 
from Seller.models import *
from Customer.customer_serializer import * 

class ProductOrderDetailsDetailsSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductOrderDetails
        fields ="__all__"
        depth =1
class PostOrderDetailsSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductOrderDetails
        fields = "__all__"
class GETProductCartSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductCart
        fields = "__all__" 
        depth =1
class POSTProductCartSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductCart
        fields = "__all__" 
    
class SellerProductDetailsSerializer(serializers.ModelSerializer): 
    PId =  POSTProductCartSerializer(read_only = True , many=True)
    itemId = PostOrderDetailsSerializer(read_only = True,many = True)
    itemId = ProductOrderDetailsDetailsSerializer(read_only = True,many = True)
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





# CUSTOMER -------------------------------------------------------------------------------------------------------------------------------------------------





class CustomerRegistrationSerializer(serializers.ModelSerializer):
    CId = PostOrderDetailsSerializer(read_only = True,many = True)
    CustomerId = POSTProductCartSerializer(read_only = True , many=True)
    userid = SellerRegistrationSerializer (read_only = True , many=True)
    class Meta:
        model = RegistrationDataTable
        fields = "__all__"









class ProductFeedbackSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductFeedback
        fields = ('AddFeedback','Rating')
