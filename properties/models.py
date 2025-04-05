from django.db import models

class Property(models.Model):
    PROPERTY_TYPES = [
        ('apartment', 'Apartment'),
        ('house', 'House'),
        ('office', 'Office'),
        ('land', 'Land'),
    ]

    title = models.CharField(max_length=255)
    description = models.TextField()
    property_type = models.CharField(max_length=20, choices=PROPERTY_TYPES)
    location = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    is_available = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

class Tenant(models.Model):
    name = models.CharField(max_length=255)
    email = models.EmailField(unique=True)
    phone = models.CharField(max_length=20, unique=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

class Lease(models.Model):
    tenant = models.ForeignKey(Tenant, on_delete=models.CASCADE)
    property = models.ForeignKey('Property', on_delete=models.CASCADE)
    start_date = models.DateField()
    end_date = models.DateField()
    rent_amount = models.DecimalField(max_digits=10, decimal_places=2)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return f"{self.tenant.name} - {self.property.title}"
    
class RentPayment(models.Model):
    tenant = models.ForeignKey(Tenant, on_delete=models.CASCADE)
    lease = models.ForeignKey(Lease, on_delete=models.CASCADE)
    amount_paid = models.DecimalField(max_digits=10, decimal_places=2)
    payment_date = models.DateTimeField(auto_now_add=True)
    payment_method = models.CharField(max_length=100, choices=[
        ('cash', 'Cash'),
        ('mpesa', 'M-Pesa'),
        ('bank_transfer', 'Bank Transfer'),
    ])
    receipt_number = models.CharField(max_length=50, unique=True)

    def __str__(self):
        return f"Payment by {self.tenant.name} - {self.amount_paid}"

