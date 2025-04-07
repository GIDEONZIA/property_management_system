from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from .models import Property, Tenant, Lease, RentPayment
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
class RentPaymentListCreateView(generics.ListCreateAPIView):
    queryset = RentPayment.objects.all()
    serializer_class = RentPaymentSerializer
    permission_classes = [IsAuthenticated]

class RentPaymentRetrieveView(generics.RetrieveAPIView):
    queryset = RentPayment.objects.all()
    serializer_class = RentPaymentSerializer
    permission_classes = [IsAuthenticated]

# Home view for testing purposes
from django.shortcuts import render
def home(request):
    return render(request, 'index.html')
