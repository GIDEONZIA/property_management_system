from django.db import models
from django.contrib.auth import get_user_model
from properties.models import Property  # Assuming you have a Property model

class Transaction(models.Model):
    user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    property = models.ForeignKey(Property, on_delete=models.CASCADE, null=True, blank=True)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    transaction_type = models.CharField(max_length=100)  # 'Rent', 'Sale', etc.
    status = models.CharField(max_length=50, choices= [
        ('pending', 'Pending'),
        ('completed', 'Completed'),
        ('failed', 'Failed'),
        ('refunded', 'Refunded'),
        ])
    date_created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Transaction {self.id} - {self.transaction_type} - {self.status}"
