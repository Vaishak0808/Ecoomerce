from django.db.models.base import Model
from django.db.models.query_utils import select_related_descend
from rest_framework import serializers
from Seller.models import *
from Customer.models import * 
from Seller.seller_serializer import SellerRegistrationSerializer
 

class CustomerRegistrationSerializer(serializers.ModelSerializer):
    
    userid = SellerRegistrationSerializer (read_only = True , many=True)
    class Meta:
        model = RegistrationDataTable
        fields = "__all__"



class ProductCartSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductCart
        fields = ('')
class ProductFeedbackSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductFeedback
        fields = ('AddFeedback','Rating')

