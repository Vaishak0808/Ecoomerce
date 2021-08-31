from django.db import models
from django.contrib.auth.models import AbstractUser

class RegistrationDataTable(AbstractUser):
    Address = models.CharField(max_length=500)
    PhoneNumber = models.BigIntegerField()
    Pincode = models.BigIntegerField()
    Updated_on = models.DateTimeField(auto_now=True)
    UserType = models.CharField(max_length=200,default="Customer")
    

class SellerRegistration(models.Model):
    CompanyId = models.AutoField(primary_key=True)
    CompanyName = models.CharField(max_length=200)
    CompanyAddress = models.TextField(max_length=200)
    CompanyPhonenumber = models.BigIntegerField()
    CompanyPin = models.BigIntegerField()
    Proof = models.FileField(upload_to='SellerProofs/',default=True,null=True)
    CompanyWebsite = models.CharField(max_length=200,null=True)
    CompanyEmail = models.CharField(max_length=200,null=True)
    Status = models.BooleanField(default=False)
    id=models.ForeignKey(RegistrationDataTable,  related_name='userid', on_delete=models.CASCADE)
 
class SellerProductDetails(models.Model):
    ProductId = models.AutoField(primary_key=True)
    PCategory = models.CharField(max_length=200)
    PName = models.CharField(max_length=200)
    PDescription = models.TextField(max_length=2000)
    PPrice = models.CharField(max_length=100)
    PPhoto = models.FileField(upload_to='ProductImages/')
    sellername = models.CharField(max_length=200,null=False,default=False)
    CompanyId = models.ForeignKey(SellerRegistration,related_name='sellerid',on_delete = models.CASCADE)

class ProductOrderDetails(models.Model):
    OrderId = models.AutoField(primary_key=True)
    Address = models.CharField(max_length=1000,null=True)
    ProductId = models.ForeignKey( to = SellerProductDetails,related_name="itemId",on_delete = models.CASCADE)
    Quantity = models.CharField(max_length=200)
    CustomerId = models.ForeignKey( to = RegistrationDataTable,related_name="CId",on_delete = models.CASCADE,null=False,default=False)
    OrderDate = models.DateField(auto_now_add=True)
    TotalPrice = models.CharField(max_length=100,default=False)
    OrderStatus = models.CharField(max_length=200,default="Ordered")
    Phonenumber = models.CharField(max_length=100, null = True)
    PinCode = models.CharField(max_length=100,null=True)

# CUSTOMER-------------------------------------------------------------------------------------------------------------------------------


class ProductCart(models.Model):
    CartId = models.AutoField(primary_key=True)
    id = models.ForeignKey( to =RegistrationDataTable, related_name='CustomerId',on_delete=models.CASCADE,default='0000')
    Quantity = models.BigIntegerField()
    CDate = models.DateTimeField(auto_now_add=True)
    ProductId = models.ForeignKey( to =SellerProductDetails, related_name='PId',on_delete=models.CASCADE)

class ProductFeedback(models.Model):
    FeedbackId = models.AutoField(primary_key=True)
    AddFeedback = models.TextField(max_length=1000)
    ProductId = models.ForeignKey( to = SellerProductDetails, on_delete = models.CASCADE)
    CustomerId = models.ForeignKey( to = RegistrationDataTable, on_delete = models.CASCADE)
    Rating = models.BigIntegerField()

