from django.db import models
from django.conf import settings
from datetime import datetime
from django.utils import timezone
from properties.models import Property

class Property(models.Model):
    name = models.CharField(max_length=255)
    address = models.TextField()
    description = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.name


class Tenant(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    property = models.ForeignKey(Property, related_name='tenants', on_delete=models.CASCADE)
    phone = models.CharField(max_length=15)
    email = models.EmailField()

    def __str__(self):
        return f"{self.user.username} - {self.property.name}"


class Transaction(models.Model):
    PAYMENT = 'Payment'
    CHARGE = 'Charge'
    REFUND = 'Refund'

    TRANSACTION_TYPES = [
        (PAYMENT, 'Payment'),
        (CHARGE, 'Charge'),
        (REFUND, 'Refund'),
    ]

    PENDING = 'Pending'
    COMPLETED = 'Completed'
    CANCELLED = 'Cancelled'

    STATUS_CHOICES = [
        (PENDING, 'Pending'),
        (COMPLETED, 'Completed'),
        (CANCELLED, 'Cancelled'),
    ]

    transaction_type = models.CharField(
        max_length=20,
        choices=TRANSACTION_TYPES,
        default=PAYMENT
    )
    tenant = models.ForeignKey(Tenant, related_name='transactions', on_delete=models.CASCADE, null=True, blank=True)
    property = models.ForeignKey(Property, related_name='transactions', on_delete=models.CASCADE, null=True, blank=True)
    date = models.DateTimeField(default=timezone.now)
    status = models.CharField(
        max_length=20,
        choices=STATUS_CHOICES,
        default=PENDING
    )
    description = models.TextField(blank=True, null=True)

    def __str__(self):
        return f"{self.transaction_type} - {self.amount} - {self.status}"

    class Meta:
        ordering = ['-id']  # orders by newest transaction first

