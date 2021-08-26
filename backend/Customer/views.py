from django.contrib.auth.models import Permission
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from django.http import JsonResponse
from Seller.models import *
from Customer.customer_serializer import *
from Customer.models import *
from rest_framework.views import APIView
from rest_framework.authtoken.models import Token
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from django.http import Http404
from rest_framework.parsers import FileUploadParser

# @csrf_exempt

class customerregistration(APIView): 
     
    def post(self,request ,*args,**kwarg):  
        serializers = CustomerRegistrationSerializer(data=request.data)
        data ={}
        print('------------------------------',serializers)
        if serializers.is_valid():
            print('inside valid------------------------')
            account = serializers.save()
            data['response']='registerd0'
            data['username']= account.username
            token,create = Token.objects.get_or_create(user=account)
            data['token'] =token.key
            account.set_password(account.password)
            account.save()
        else:
            data = "error"

        return Response(data) 


class Welcome(APIView): 
    # Permission_classes = (IsAuthenticated)
    def get(self,request):
        # userobj = RegistrationDataTable.objects.get(id=request.user.id)
        sellerobj = SellerRegistration.objects.get(id=request.user.id).CompanyId
        # print('===============================================================================',userobj)
        print('----------------------------------------------------------',sellerobj)
        content ={'user':str(request.user),'userid':str(request.user.id),'UserType':str(request.user.UserType),'CompanyId':sellerobj}
        # id ={'companyId':str(request.user.userid["CompanyId"])}
        # id = {'companyId':str(request.userid["CompanyId"])}
        # print("--------------------COmpanyID-----------------------",id)
        # print("-------------------------Company------------------CONTENTS",content)
        return Response(content)


            

 



















# Customer Registration  ###########################################  
@csrf_exempt
# def customerregistration(request,id=0):
#     if request.method == "GET":
#         Customer = RegistrationDataTable.objects.all()
#         Customer_serializer = CustomerRegistrationSerializer(Customer, many=True)
#         return JsonResponse(Customer_serializer.data, safe=False)
#     elif request.method == "POST":        
#         Customer_data = JSONParser().parse(request)
#         Customer_serializer = CustomerRegistrationSerializer(data = Customer_data)        
#         if Customer_serializer.is_valid():
#             Customer_serializer.save()
#             return JsonResponse("Added Successfully", safe=False)
            
#         else:
#             return JsonResponse("Adding Failed" ,safe=False)
#     elif request.method == "PUT":
#         Customer_data = JSONParser().parse(request)
#         Customer = RegistrationDataTable.objects.get(id = Customer_data['id'])
#         print('---------------------',Customer_data)
#         Customer_serializer = CustomerRegistrationSerializer(Customer ,data = Customer_data)
#         print('------------------',Customer_serializer)
#         print("valid",Customer_serializer.is_valid())
#         if Customer_serializer.is_valid():
#             print()

#             Customer_serializer.save()
#             return JsonResponse("Updated Successfully", safe=False)
#         else:
#             return JsonResponse("Updating Failed", safe=False)
#     elif request.method == "DELETE":
#         Customer = RegistrationDataTable.objects.get(id = id)
#         Customer.delete()
#         return JsonResponse("Deleted Successfully", safe=False)


#Product Feedback  #################################################
@csrf_exempt
def productfeedback(request,id=0):
    if request.method == "GET":
        feedback = ProductCart.objects.all()
        feedback_serializer = ProductCartSerializer(feedback , many=True)
        return JsonResponse(feedback_serializer.data, safe=False)
    elif request.method =="POST":
        feedback = JSONParser().parse(request)
        feedback_serializer = ProductCartSerializer(data = feedback)
        if feedback_serializer.is_valid():
            feedback_serializer.save()
            return JsonResponse("Added Successfully", safe=False)
        else:
            return JsonResponse("Adding Failed", safe=False)
    elif request.method == "PUT":
        feedback = JSONParser().parse(request)
        feedback_data = RegistrationDataTable.objects.get(FeedBackId = feedback['FeedBackId'])
        feedback_serializer = CustomerRegistrationSerializer(feedback_data ,data = feedback)
        if feedback_serializer.is_valid():
            feedback_serializer.save()
            return JsonResponse("Updated Successfully", safe=False)
        else:
            return JsonResponse("Updating Failed", safe=False)
    elif request.method == "DELETE":
        feedback = RegistrationDataTable.objects.get(FeedBackId = id)
        feedback.delete()
        return JsonResponse("Deleted Successfully", safe=False)


# View Cart ###################################

def ViewCartProduct(request):
    if request.method == "GET":
        Cart = ProductCart.objects.all()
        Cart_serializer = ProductCartSerializer(Cart , many=True)
        return JsonResponse(Cart_serializer.data, safe=False)
    elif request.method =="POST":
        Cart = JSONParser().parse(request)
        Cart_serializer = ProductCartSerializer(data = Cart)
        if Cart_serializer.is_valid():
            Cart_serializer.save()
            return JsonResponse("Added Successfully", safe=False)
        else:
            return JsonResponse("Adding Failed", safe=False)
    elif request.method == "PUT":
        Cart = JSONParser().parse(request)
        Cart_data = ProductCart.objects.get(CartId = Cart['CartId'])
        Cart_serializer = ProductCartSerializer(Cart_data ,data = Cart)
        if Cart_serializer.is_valid():
            Cart_serializer.save()
            return JsonResponse("Updated Successfully", safe=False)
        else:
            return JsonResponse("Updating Failed", safe=False)







