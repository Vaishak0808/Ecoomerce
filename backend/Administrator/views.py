from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from django.http import JsonResponse
from Customer.models import *
from Customer.customer_serializer import *
from Seller.models import *
from Seller.seller_serializer import *
from django.http.response import JsonResponse
from rest_framework.views import APIView
from rest_framework import status
from rest_framework.parsers import FileUploadParser
from rest_framework.response import Response

#view Customer ################################
@csrf_exempt
def ViewCustomerDetails(request):
    if request.method == "GET":
        Customer = RegistrationDataTable.objects.all()
        Customer_serializer = CustomerRegistrationSerializer(Customer, many=True)
        return JsonResponse(Customer_serializer.data, safe=False)

#view Approved Seller #######################
@csrf_exempt
def ViewApprovedSellerDetails(request):
    if request.method == "GET":
        Seller = SellerRegistration.objects.all().filter(Status= True)
        Seller_serializer = SellerRegistrationSerializer(Seller , many=True)
        return JsonResponse(Seller_serializer.data,safe=False)

#view seller details to approve ###############
@csrf_exempt
def ViewSellerToApproveDetails(request,id=0):
    if request.method == "GET":
        Seller = SellerRegistration.objects.all().filter(Status=False)
        Seller_serializer = SellerRegistrationSerializer(Seller, many=True)
        return JsonResponse(Seller_serializer.data,safe=False)
    elif request.method == "PUT":
        Seller_data = JSONParser().parse(request)
        User_details = {'id': Seller_data['id'],
                        'UserType':Seller_data['UserType']}
        Seller_details ={'id':Seller_data['id'],
                            'Status':Seller_data['Status']}
        # print("User detils............................",User_details)
        # print("Seller details.................../....",Seller_details)
        # print("Sellerdata...........................",Seller_data)
        Customer = RegistrationDataTable.objects.get(id=Seller_data['id'])
        Seller = SellerRegistration.objects.get(id = Seller_data['id'])
        Customer_serializer = CustomerUpdationSerializser(Customer,data = User_details)
        Seller_serializer = SellerUpdationRegistrationSerializer(Seller,data = Seller_details)
        if Seller_serializer.is_valid() and Customer_serializer.is_valid():
            Customer_serializer.save()
            Seller_serializer.save()
            return JsonResponse("Approved", safe=False)
        return JsonResponse('failed',safe=False)
@csrf_exempt
def rejectrequestedseller(request,id):
    if request.method == "DELETE":
        print('--------------INSIDE DELETE--------------',request) 
        print("companyid",id)
        Reject = SellerRegistration.objects.get(CompanyId=id)
        print("\nREJECT SELLER\n",Reject)
        Reject.delete()
        return JsonResponse("Deleted Succesffuly",safe=False)
    else:
        return JsonResponse("Deleting Failed",safe=False)  



