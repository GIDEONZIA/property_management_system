from django.db import models
from django.utils import timezone
from django.contrib.auth import get_user_model
from properties.models import Property  # Assuming properties are in a separate app
from transaction.models import Transaction # Import Transaction Model
User = get_user_model()

class Bill(models.Model):
    STATUS_CHOICES = [
        ('pending', 'Pending'),
        ('paid', 'Paid'),
        ('overdue', 'Overdue'),
    ]

    CATEGORY_CHOICES = [
        ('electricity', 'Electricity'),
        ('water', 'Water'),
        ('internet', 'Internet'),
        ('garbage', 'Garbage'),
        ('other', 'Other'),
    ]

    name = models.CharField(max_length=255, help_text="Name of the bill (e.g., Water Bill)")
    tenant = models.ForeignKey(User, on_delete=models.CASCADE, related_name="bills", help_text="The tenant responsible for the bill")
    property = models.ForeignKey(Property, on_delete=models.CASCADE, related_name="bills", help_text="The property linked to the bill")
    amount_due = models.DecimalField(max_digits=10, decimal_places=2, help_text="Total amount due for the bill")
    due_date = models.DateField(help_text="The due date for bill payment")
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='pending', help_text="Payment status of the bill")
    category = models.CharField(max_length=20, choices=CATEGORY_CHOICES, help_text="Category of the bill")
    transaction = models.OneToOneField(Transaction, on_delete=models.CASCADE, null=True, blank=True, related_name="bill", help_text="The transaction related to the bill")
    created_at = models.DateTimeField(auto_now_add=True, help_text="Date and time the bill was created")
    updated_at = models.DateTimeField(auto_now=True, help_text="Date and time the bill was last updated")

    def __str__(self):
        return f"{self.name} - {self.tenant} - {self.status}"

class Receipt(models.Model):
    transaction = models.OneToOneField(Transaction, on_delete=models.CASCADE)
    receipt_number = models.CharField(max_length=255, unique=True)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    date_issued = models.DateTimeField(default=timezone.now)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    
    def __str__(self):
        return f"Receipt {self.receipt_number} - {self.user.username}"
    
    def generate_receipt_number(self):
        # Generate a unique receipt number (you can implement your own logic here)
        self.receipt_number = f"REC-{self.transaction.id}-{self.date_issued.strftime('%Y%m%d%H%M%S')}"
        
    def save(self, *args, **kwargs):
        if not self.receipt_number:
            self.generate_receipt_number()
        super().save(*args, **kwargs)