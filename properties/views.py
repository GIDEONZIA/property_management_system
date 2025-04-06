from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from django.shortcuts import get_object_or_404
from .models import Property, Tenant, Lease, RentPayment  # Add RentPayment here
from .serializers import PropertySerializer, RentPaymentSerializer

# List all properties or create a new one
class PropertyListCreateView(generics.ListCreateAPIView):
    queryset = Property.objects.all()
    serializer_class = PropertySerializer

# Retrieve, update, or delete a specific property
class PropertyRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Property.objects.all()
    serializer_class = PropertySerializer

from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from .models import Property, Tenant, Lease
from .serializers import PropertySerializer, TenantSerializer, LeaseSerializer, RentPaymentSerializer

# Property views
class PropertyListCreateView(generics.ListCreateAPIView):
    queryset = Property.objects.all()
    serializer_class = PropertySerializer
    permission_classes = [IsAuthenticated]

class PropertyRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Property.objects.all()
    serializer_class = PropertySerializer
    permission_classes = [IsAuthenticated]

# Tenant views
class TenantListCreateView(generics.ListCreateAPIView):
    queryset = Tenant.objects.all()
    serializer_class = TenantSerializer
    permission_classes = [IsAuthenticated]

class TenantRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Tenant.objects.all()
    serializer_class = TenantSerializer
    permission_classes = [IsAuthenticated]

# Lease views
class LeaseListCreateView(generics.ListCreateAPIView):
    queryset = Lease.objects.all()
    serializer_class = LeaseSerializer
    permission_classes = [IsAuthenticated]

class LeaseRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Lease.objects.all()
    serializer_class = LeaseSerializer
    permission_classes = [IsAuthenticated]
    
# RentPayment views
from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from .models import RentPayment
from .serializers import RentPaymentSerializer

class RentPaymentListCreateView(generics.ListCreateAPIView):
    queryset = RentPayment.objects.all() # type: ignore
    serializer_class = RentPaymentSerializer # type: ignore
    permission_classes = [IsAuthenticated]

class RentPaymentRetrieveView(generics.RetrieveAPIView):
    queryset = RentPayment.objects.all() # type: ignore
    serializer_class = RentPaymentSerializer # type: ignore
    permission_classes = [IsAuthenticated]

from django.shortcuts import render

def home(request):
    return render(request, 'index.html')
