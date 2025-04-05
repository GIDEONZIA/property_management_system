# property_mgmt/admin.py
from django.contrib import admin

admin.site.site_header = "Property Management System"
admin.site.site_title = "PMS Admin"
admin.site.index_title = "Welcome to Property Management System"

from django.contrib import admin
from .models import Property, Tenant, Lease

# Register models only if they are not already registered
models = [Property, Tenant, Lease]

for model in models:
    if model not in admin.site._registry:
        admin.site.register(model)

from .models import RentPayment

admin.site.register(RentPayment)


