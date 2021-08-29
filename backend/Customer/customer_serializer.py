from django.db.models.base import Model
from django.db.models.query_utils import select_related_descend
from rest_framework import serializers
from Seller.models import *
from Customer.models import * 
from Seller.seller_serializer import SellerRegistrationSerializer
from Customer.customer_serializer import *


class ProductCartSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductCart
        fields = "__all__" 

class CustomerRegistrationSerializer(serializers.ModelSerializer):
    # CustomerId = ProductCartSerializer(read_only = True , many=True)
    userid = SellerRegistrationSerializer (read_only = True , many=True)
    class Meta:
        model = RegistrationDataTable
        fields = "__all__"

# class SellerProductDetailsSerializer(serializers.ModelSerializer): 
#     PId =  ProductCartSerializer(read_only = True , many=True)
#     class Meta:
#         model = SellerProductDetails
#         fields = "__all__"







class ProductFeedbackSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductFeedback
        fields = ('AddFeedback','Rating')

