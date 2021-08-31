from django.db import models
from Seller.models import *

# class ProductCart(models.Model):
#     CartId = models.AutoField(primary_key=True)
#     id = models.ForeignKey( to = 'Seller.RegistrationDataTable',on_delete=models.CASCADE,default='0000')
#     Quantity = models.BigIntegerField()
#     CDate = models.DateTimeField(auto_now_add=True)
#     ProductId = models.ForeignKey( to = 'Seller.SellerProductDetails',on_delete=models.CASCADE)






# class ProductFeedback(models.Model):
#     FeedbackId = models.AutoField(primary_key=True)
#     AddFeedback = models.TextField(max_length=1000)
#     ProductId = models.ForeignKey( to = 'Seller.SellerProductDetails', on_delete = models.CASCADE)
#     CustomerId = models.ForeignKey( to = 'Seller.RegistrationDataTable', on_delete = models.CASCADE)
#     Rating = models.BigIntegerField()




# ,related_name='CustomerId'

# ,related_name='PId'
 


