from django.contrib import admin
from .models import Bill

@admin.register(Bill)
class BillAdmin(admin.ModelAdmin):
    list_display = ('name', 'tenant', 'property', 'amount_due', 'due_date', 'status', 'category')
    list_filter = ('status', 'category', 'due_date')
    search_fields = ('name', 'tenant__username', 'property__name')
    ordering = ('due_date',)

