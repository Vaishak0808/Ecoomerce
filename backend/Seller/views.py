from django.shortcuts import render
from django.views.decorators import csrf
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from django.http import JsonResponse, response
from Seller.models import *
from Seller.seller_serializer import *
from django.core.files.storage import default_storage
from rest_framework.views import APIView
from rest_framework import status
from rest_framework.parsers import FileUploadParser
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework.authtoken.models import Token



##########################################################

#Seller Registration,Update,delete

class sellerregistrations(APIView):
    def get(self,request):
        Seller = SellerRegistration.objects.all()
        Seller_serializer = SellerRegistrationSerializer(Seller)
        return Response(Seller_serializer.data)
    USER_TOKEN ='' 
    parser_class = (FileUploadParser,) 
    def post(self,request,*args,**kwarg): 
        print("----------POST-------" )     
        seller_serializer = SellerRegistrationSerializer(data = request.data) 
        print("-- ------   serializer   ------",seller_serializer)   
        if seller_serializer.is_valid(): 
            seller_serializer.save()            
            return Response(seller_serializer.data , status=status.HTTP_201_CREATED)
        else:
            return Response( status=status.HTTP_400_BAD_REQUEST) 
    def put(self,pk,request):
        Seller = SellerRegistration.objects.get(id=pk)
        Seller_Serializer = SellerRegistrationSerializer(Seller,data = request.data)
        if Seller_Serializer.is_valid():
            Seller_Serializer.save()
            return Response("Updated Succesfully",Seller_Serializer.data)
        return Response("Error in updating",Seller_Serializer.errors)
    def delete(self,pk,request):
        Seller = SellerRegistration.objects.get(id=pk)
        Seller.delete()
        return Response("Deleted Successfully")


class addproducts(APIView):
    def get(self,request):
        product = SellerProductDetails.objects.all()
        if product:
            product_serializer = SellerProductDetailsSerializer(product)
            return Response(product_serializer.data)
        else:
            return Response('NO DATA ')
    parser_class = (FileUploadParser,)
    def post(self,request,*args,**kwarg):
        
        product_serializer = SellerProductDetailsSerializer(data = request.data)
        print("////////////////////////////////////////////////////")
        print("product_Serializer",product_serializer)
        if product_serializer.is_valid():
            print("------------inside valid---------------------")
            product_serializer.save()
            return Response(product_serializer.data,status=status.HTTP_201_CREATED)
        else:
            
            return Response( status=status.HTTP_400_BAD_REQUEST) 




# @csrf_exempt
# def sellerregistration(request,id=0):
#     if request.method == "GET":
#         Seller = SellerRegistration.objects.all()
#         Seller_serializer = SellerRegistrationSerializer(Seller, many=True)
#         return JsonResponse(Seller_serializer.data, safe=False)
#     elif request.method == "POST":
#         Seller_data = JSONParser().parse(request)
#         print("########################################################################seller_data###############",Seller_data)
#         Seller_serializer = SellerRegistrationSerializer(data = Seller_data)
#         print("#######################################    seller_serializer       ###############",Seller_serializer)

#         if Seller_serializer.is_valid():
#            Seller_serializer.save()
#            return JsonResponse("Added Successfully", safe=False)
#         else:
#             return JsonResponse("Adding Failed" ,safe=False)
#     elif request.method == "PUT":
#         Seller_data = JSONParser().parse(request)
#         Seller = SellerRegistration.objects.get(CId = Seller_data['CId'])
#         Seller_serializer = SellerRegistrationSerializer(Seller ,data = Seller_data)
#         if Seller_serializer.is_valid():
#             Seller_serializer.save()
#             return JsonResponse("Updated Successfully", safe=False)
#         else:
#             return JsonResponse("Updating Failed", safe=False)
#     elif request.method == "DELETE":
#         Customer =SellerRegistration.objects.get(CId = id)
#         Customer.delete()
#         return JsonResponse("Deleted Successfully", safe=True)

#########################################################

# Add,Update,Delete ProductDetails
@csrf_exempt
def AddProducts(request,id=0):
    if request.method == "GET":
        Product = SellerProductDetails.objects.all()
        Product_serializer = SellerProductDetailsSerializer(Product, many=True)
        return JsonResponse(Product_serializer.data, safe=False)
    elif request.method == "POST":
        Seller_data = JSONParser().parse(request)
        Product_serializer = SellerProductDetailsSerializer(data = Seller_data)
        if Product_serializer.is_valid():
           Product_serializer.save()
           return JsonResponse("Added Successfully", safe=False)
        else:
            return JsonResponse("Adding Failed" ,safe=False)
    elif request.method == "PUT":
        Product_data = JSONParser().parse(request)
        Product = SellerProductDetails.objects.get(ProductId = Product_data['ProductId'])
        Product_serializer = SellerProductDetailsSerializer(Product ,data = Product_data)
        if Product_serializer.is_valid():
            Product_serializer.save()
            return JsonResponse("Updated Successfully", safe=False)
        else:
            return JsonResponse("Updating Failed", safe=False)
    elif request.method == "DELETE":
        Customer =SellerRegistration.objects.get(CId = id)
        Customer.delete()
        return JsonResponse("Deleted Successfully", safe=True)










        # USER_TOKEN=request.headers.get('Authorization')
        # print("-------    TOKEN -----------",request.headers.get('Authorization'))  