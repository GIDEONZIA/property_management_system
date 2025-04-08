from django.views.generic import CreateView, ListView
from django.shortcuts import render
from django.urls import reverse_lazy

from django.http import HttpResponse

def home(request):
    return HttpResponse("Welcome to the Home Page!")


from .models import Property, RentPayment, Lease
from .forms import (
    PropertyForm, HouseForm, HotelForm, ApartmentForm, RestaurantForm, BeachLandForm,
    OfficeForm, ResortForm, CommercialForm, IndustrialForm, AgriculturalForm,
    VacationForm, RetailForm, WarehouseForm, MixedUseForm
)

# === Mixin to dynamically choose form class based on property_type ===
class PropertyTypeFormMixin:
    property_type_form_map = {
        'house': HouseForm,
        'hotel': HotelForm,
        'apartment': ApartmentForm,
        'restaurant': RestaurantForm,
        'beachland': BeachLandForm,
        'office': OfficeForm,
        'resort': ResortForm,
        'commercial': CommercialForm,
        'industrial': IndustrialForm,
        'agricultural': AgriculturalForm,
        'vacation': VacationForm,
        'retail': RetailForm,
        'warehouse': WarehouseForm,
        'mixeduse': MixedUseForm,
    }

    def get_dimension_form_class(self, property_type):
        return self.property_type_form_map.get(property_type.lower())

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        property_type = self.request.POST.get('property_type') or self.request.GET.get('property_type')
        dimension_form_class = self.get_dimension_form_class(property_type)

        if self.request.method == 'POST':
            context['dimension_form'] = dimension_form_class(self.request.POST) if dimension_form_class else None
        else:
            context['dimension_form'] = dimension_form_class() if dimension_form_class else None

        return context

# === View for Creating Property ===
class PropertyListCreateView(PropertyTypeFormMixin, ListView, CreateView):
    model = Property
    form_class = PropertyForm
    template_name = 'properties/property_form.html'
    success_url = reverse_lazy('property_list')  # Update this as needed

    def form_valid(self, form):
        response = super().form_valid(form)

        property_type = form.cleaned_data.get('property_type')
        dimension_form_class = self.get_dimension_form_class(property_type)

        if dimension_form_class:
            dimension_form = dimension_form_class(self.request.POST)
            if dimension_form.is_valid():
                instance = dimension_form.save(commit=False)
                instance.property = self.object
                instance.save()
            else:
                return self.render_to_response(self.get_context_data(form=form, dimension_form=dimension_form))

        return response

from rest_framework import generics
from .models import Property
from .serializers import PropertySerializer, RentPaymentSerializer, LeaseSerializer

class PropertyRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Property.objects.all()
    serializer_class = PropertySerializer
    lookup_field = 'id'  # or 'pk' based on your URL configuration

from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from .models import Tenant
from .serializers import TenantSerializer

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

# properties/views.py
from django.shortcuts import render
from .forms import PropertyForm

def create_property(request):
    if request.method == 'POST':
        form = PropertyForm(request.POST)
        if form.is_valid():
            form.save()
    else:
        form = PropertyForm()
    return render(request, 'create_property.html', {'form': form})
