from django.urls import path
from .views import PropertyListCreateView, PropertyRetrieveUpdateDestroyView

urlpatterns = [
    path('properties/', PropertyListCreateView.as_view(), name='property-list'),
    path('properties/<int:pk>/', PropertyRetrieveUpdateDestroyView.as_view(), name='property-detail'),
]

from django.contrib import admin
from django.urls import path, include
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('properties.urls')),  # Property API routes

    # Authentication API endpoints
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),  # Login
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),  # Refresh token
]

from django.urls import path
from .views import PropertyListCreateView, PropertyRetrieveUpdateDestroyView

urlpatterns = [
    path('properties/', PropertyListCreateView.as_view(), name='property-list'),
    path('properties/<int:pk>/', PropertyRetrieveUpdateDestroyView.as_view(), name='property-detail'),
]
 
from django.urls import path
from .views import (
    PropertyListCreateView, PropertyRetrieveUpdateDestroyView,
    TenantListCreateView, TenantRetrieveUpdateDestroyView,
    LeaseListCreateView, LeaseRetrieveUpdateDestroyView
)

urlpatterns = [
    path('properties/', PropertyListCreateView.as_view(), name='property-list'),
    path('properties/<int:pk>/', PropertyRetrieveUpdateDestroyView.as_view(), name='property-detail'),
    
    path('tenants/', TenantListCreateView.as_view(), name='tenant-list'),
    path('tenants/<int:pk>/', TenantRetrieveUpdateDestroyView.as_view(), name='tenant-detail'),

    path('leases/', LeaseListCreateView.as_view(), name='lease-list'),
    path('leases/<int:pk>/', LeaseRetrieveUpdateDestroyView.as_view(), name='lease-detail'),
]

from django.urls import path
from .views import RentPaymentListCreateView, RentPaymentRetrieveView  # ✅ Ensure this is imported

urlpatterns = [
    path('rent-payments/', RentPaymentListCreateView.as_view(), name='rent-payment-list'),
    path('rent-payments/<int:pk>/', RentPaymentRetrieveView.as_view(), name='rent-payment-detail'),  # ✅ Add this
]

from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
]
