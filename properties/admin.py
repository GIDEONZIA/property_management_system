# property_mgmt/admin.py
from django.contrib import admin
from .models import Property, Tenant, Lease, RentPayment,House, Hotel, Restaurant, Apartment, BeachLand, Office, Resort, Land, Commercial, Industrial, Agricultural, Vacation, Retail, Warehouse, MixedUse, Other 

admin.site.site_header = "Property Management System"
admin.site.site_title = "PMS Admin"
admin.site.index_title = "Welcome to Zia Property Management System"

models = [Property, Tenant, Lease, RentPayment, House, Hotel, Restaurant, Apartment, BeachLand, Office, Resort, Land, Commercial, Industrial, Agricultural, Vacation, Retail, Warehouse, MixedUse, Other ]

for model in models:
	admin.site.register(model)



