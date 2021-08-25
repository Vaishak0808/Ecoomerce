from django.conf.urls import url
from Administrator.views import *

urlpatterns = [
        # View Customer
        url(r'^ViewCustomer/$',ViewCustomerDetails), 
        # View Approved Seller
        url(r'^ViewApprovedSellerDetails/$',ViewApprovedSellerDetails),
        # view Seller to Approve
        url(r'^ViewSellerToApproveDetails/$',ViewSellerToApproveDetails),
        url(r'^ViewSellerToApproveDetails/([0-9]+)$',ViewSellerToApproveDetails)
]