from django.urls import path
from .views import bill_list, bill_detail, create_bill, update_bill, delete_bill

urlpatterns = [
    path('bills/', bill_list, name='bill-list'),
    path('bills/<int:bill_id>/', bill_detail, name='bill-detail'),
    path('bills/create/', create_bill, name='bill-create'),
    path('bills/update/<int:bill_id>/', update_bill, name='bill-update'),
    path('bills/delete/<int:bill_id>/', delete_bill, name='bill-delete'),
]
