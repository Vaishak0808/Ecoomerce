from django.conf.urls import url
from django.urls import path

from Administrator.views import *

urlpatterns = [
        # View Customer
        url(r'^ViewCustomer/$',ViewCustomerDetails), 
        # View Approved Seller
        url(r'^ViewApprovedSellerDetails/$',ViewApprovedSellerDetails),
        # view Seller to Approve
        url(r'^ViewSellerToApproveDetails/$',ViewSellerToApproveDetails),
        url('ViewSellerToApproveDetails/<int:id>/',ViewSellerToApproveDetails),
        path('rejectrequestedseller/<str:id>/',rejectrequestedseller)
        
]