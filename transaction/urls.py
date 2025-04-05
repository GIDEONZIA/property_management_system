from django.urls import path
from .views import TransactionListView  # Ensure correct import

urlpatterns = [
    path('transactions/', TransactionListView.as_view(), name='transaction_list'),  # Use .as_view()
]
