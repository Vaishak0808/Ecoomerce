from django.db.models.query import prefetch_related_objects
from django.shortcuts import render
from django.contrib.auth.models import Permission


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
from django.http import Http404





##########################################################

#Seller Registration,Update,delete
# global USER_TOKEN 
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
            product_serializer = SellerProductDetailsSerializer(product,many=True)
            return Response(product_serializer.data)
        else:
            return Response("No DATA")
    parser_class = (FileUploadParser,)
    def post(self,request,*args,**kwarg):
        
        product_serializer = SellerProductDetailsSerializer(data = request.data)  
        if product_serializer.is_valid(): 
            product_serializer.save()
            return Response(product_serializer.data,status=status.HTTP_201_CREATED)
        else:
            
            return Response( status=status.HTTP_400_BAD_REQUEST) 
 
@csrf_exempt
def GetSingleProduct(request,id):
    # print("id",id)
    if request.method == "GET":
        product = SellerProductDetails.objects.get(ProductId = id) 
        # print(product)
        content = {}
        if product:
            getSingleSerialiset = SellerSingleProductDetailsSerializer(product,many = False)
            
            return JsonResponse(getSingleSerialiset.data,safe=False)
        else:
            return JsonResponse("No DATA") 




# CUSTOMER-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

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
        global USER_TOKEN
        USER_TOKEN = request.user.id 
        # print("WELCOME USERID++++++++++++++++++++++++++++",USER_TOKEN)
        if request.user.UserType == 'Seller':
        # userobj = RegistrationDataTable.objects.get(id=request.user.id)
            sellerobj = SellerRegistration.objects.get(id=request.user.id).CompanyId
        # print('===============================================================================',userobj)
            # print('----------------------------------------------------------',sellerobj)
            if sellerobj:
                content ={'user':str(request.user),'userid':str(request.user.id),'UserType':str(request.user.UserType),'CompanyId':sellerobj}
                return Response(content)
        else:
            content ={'user':str(request.user),'userid':str(request.user.id),'UserType':str(request.user.UserType)}
            return Response(content)

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
class viewCartProduct(APIView):
    def get(self,request): 
        id = USER_TOKEN
        # print("IAM IN VIEW CART")
        # print("IN CART USERID",id)
        Cart = ProductCart.objects.all().filter(id = id) 
        # print("CART+++++++++++++++",Cart)
        # print("CARTlength++++++++++++",len(Cart))

        if(len(Cart) > 0):
            print("INSIDE IF")
            cart_serializer = GETProductCartSerializer(Cart ,many = True)
            # print("CART -SERIALIZER",cart_serializer.data)
            return Response(cart_serializer.data) 
        else:
            return Response('')
        
            
    def post(self,request,*args,**kwarg):
        Cart_serializer = POSTProductCartSerializer(data = request.data)
        if Cart_serializer.is_valid():
            Cart_serializer.save()
            return Response("Added Successfully")
        else:
            return Response("Adding Failed")
@csrf_exempt
def deleteCartProduct(request,id):
    if request.method == "DELETE":
        cart = ProductCart.objects.get(CartId = id)
        cart.delete()
        return JsonResponse("Deleted Succeffuly",safe=False)
    return JsonResponse("Not removed",safe=False)
class PlaceOrder(APIView):
    def get(self,request):
        # print("inside PLaceOrder+++")
        user_id = USER_TOKEN
        Company = SellerRegistration.objects.get(id = user_id)
        products = SellerProductDetails.objects.all().filter(CompanyId = Company.CompanyId)
        content = []
        details = []
        for items in products:
            Orders = ProductOrderDetails.objects.all().filter(ProductId = items.ProductId)
            if Orders:
                details.append(Orders)
        # print("\n\ndetails::::::::::::::::::::::::::::::::::::::::::::::::::::",details) 
        # return Response(order_Serializers.data)
        for data in details:
            print("\nDAATAATATATAT",data)
            for i in data:
                # print("\nINSIDE IF--------------------------------------------------------------",i.Address)
                order_Serializers = ProductOrderDetailsDetailsSerializer(i , many =False)
                content.append(order_Serializers.data)
        # print("\n\nCONTENT ______________",order_Serializers.data) 
        return Response(content)
            
    def post(self,request,*args,**kwarg):
        print("INSIDE POST-=================------------------------------",request.data)

        order_serializer = PostOrderDetailsSerializer(data = request.data)
        print('serializer-----------------------------',order_serializer)
        if order_serializer.is_valid():
            print('valid-----------------------------------')
            order_serializer.save()
            return Response("Added Successfully")
        else:
            return Response("Adding Failed")

class getUserAndProduct(APIView):
    def get(self,request,id):
        user_id =   USER_TOKEN
        product = SellerProductDetails.objects.get(ProductId = id)
        user_details = RegistrationDataTable.objects.get(id = user_id) 
        content = {}
        if product:
            getSingleSerializer = SellerSingleProductDetailsSerializer(product,many = False)
            getUserSerializer = CustomerRegistrationSerializer(user_details,many = False)
            content['product'] = getSingleSerializer.data
            content['userdetails'] = getUserSerializer.data
            
            return Response(content)
        else:
            return  Response("No DATA")
    
class myOrders(APIView):
    def get(self,request):
        o_status= "Canceled"
        user_id =  USER_TOKEN
        # CustomerId = user_id
        order = ProductOrderDetails.objects.all().filter(  CustomerId = user_id ).filter(  OrderStatus = "Ordered" or "Processing" or "Out for Delivery" or "Delivered")
        if(order):
            order_serializer = ProductOrderDetailsDetailsSerializer(order , many=True)
            return Response(order_serializer.data)
        return Response('')


@csrf_exempt
def updateOderdStatus(request):
    if request.method == "PUT":
        OrderData = JSONParser().parse(request)
        Order_details = ProductOrderDetails.objects.get(OrderId = OrderData['OrderId'])
        Order_Serializer = UpdateProductStatusSerializer(Order_details,data = OrderData)
        # print("\nORDER SERIALIZER\n",Order_Serializer)
        # print("\nORDER SERIALISER DATA\n",Order_Serializer.initial_data)
        if Order_Serializer.is_valid(): 
            Order_Serializer.save()
            return JsonResponse("Status Changed", safe=False)
        return JsonResponse('failed to change',safe=False)
@csrf_exempt       
def DeleteProductOrder(request,id):
    if request.method == 'DELETE':
        Order_details = ProductOrderDetails.objects.get(OrderId = id)
        Order_details.delete()
        return JsonResponse("Deleted Successfully",safe=False)



















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
# @csrf_exempt
# def AddProducts(request,id=0):
    # if request.method == "GET":
    #     Product = SellerProductDetails.objects.all()
    #     Product_serializer = SellerProductDetailsSerializer(Product, many=True)
    #     return JsonResponse(Product_serializer.data, safe=False)
    # elif request.method == "POST":
    #     Seller_data = JSONParser().parse(request)
    #     Product_serializer = SellerProductDetailsSerializer(data = Seller_data)
    #     if Product_serializer.is_valid():
    #        Product_serializer.save()
    #        return JsonResponse("Added Successfully", safe=False)
    #     else:
    #         return JsonResponse("Adding Failed" ,safe=False)
    # elif request.method == "PUT":
    #     Product_data = JSONParser().parse(request)
    #     Product = SellerProductDetails.objects.get(ProductId = Product_data['ProductId'])
    #     Product_serializer = SellerProductDetailsSerializer(Product ,data = Product_data)
    #     if Product_serializer.is_valid():
    #         Product_serializer.save()
    #         return JsonResponse("Updated Successfully", safe=False)
    #     else:
    #         return JsonResponse("Updating Failed", safe=False)
    # elif request.method == "DELETE":
    #     Customer =SellerRegistration.objects.get(CId = id)
    #     Customer.delete()
    #     return JsonResponse("Deleted Successfully", safe=True)


# Customer Registration  ###########################################  
# @csrf_exempt
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