from django.shortcuts import render, get_object_or_404
from .models import Receipt
from transaction.models import Transaction
from django.http import HttpResponse
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.core.serializers import serialize


import json

from .models import Bill

def bill_list(request):
    """List all bills"""
    bills = Bill.objects.all()
    data = serialize('json', bills)
    return JsonResponse(data, safe=False)

def bill_detail(request, bill_id):
    """Retrieve a single bill"""
    bill = get_object_or_404(Bill, id=bill_id)
    data = {
        "id": bill.id,
        "name": bill.name,
        "tenant": bill.tenant.username,
        "property": bill.property.name,
        "amount_due": str(bill.amount_due),
        "due_date": bill.due_date.strftime("%Y-%m-%d"),
        "status": bill.status,
        "category": bill.category,
    }
    return JsonResponse(data)

@csrf_exempt
def create_bill(request):
    """Create a new bill"""
    if request.method == "POST":
        data = json.loads(request.body)
        bill = Bill.objects.create(
            name=data['name'],
            tenant_id=data['tenant'],
            property_id=data['property'],
            amount_due=data['amount_due'],
            due_date=data['due_date'],
            status=data.get('status', 'pending'),
            category=data['category']
        )
        return JsonResponse({"message": "Bill created successfully", "bill_id": bill.id})

@csrf_exempt
def update_bill(request, bill_id):
    """Update an existing bill"""
    bill = get_object_or_404(Bill, id=bill_id)
    if request.method == "PUT":
        data = json.loads(request.body)
        bill.name = data.get('name', bill.name)
        bill.amount_due = data.get('amount_due', bill.amount_due)
        bill.due_date = data.get('due_date', bill.due_date)
        bill.status = data.get('status', bill.status)
        bill.category = data.get('category', bill.category)
        bill.save()
        return JsonResponse({"message": "Bill updated successfully"})

@csrf_exempt
def delete_bill(request, bill_id):
    """Delete a bill"""
    bill = get_object_or_404(Bill, id=bill_id)
    if request.method == "DELETE":
        bill.delete()
        return JsonResponse({"message": "Bill deleted successfully"})

from transaction.models import Transaction  # Import the Transaction model

@csrf_exempt
def update_bill(request, bill_id):
    """Update an existing bill and create a transaction if marked as paid"""
    bill = get_object_or_404(Bill, id=bill_id)
    if request.method == "PUT":
        data = json.loads(request.body)
        previous_status = bill.status  # Store previous status
        
        bill.name = data.get('name', bill.name)
        bill.amount_due = data.get('amount_due', bill.amount_due)
        bill.due_date = data.get('due_date', bill.due_date)
        bill.status = data.get('status', bill.status)
        bill.category = data.get('category', bill.category)
        bill.save()

        # If the bill was marked as 'Paid' and it was previously 'Pending' or 'Overdue', create a transaction
        if bill.status == 'paid' and previous_status != 'paid':
            transaction = Transaction.objects.create(
                user=bill.tenant,
                property=bill.property,
                amount=bill.amount_due,
                description=f"Payment for {bill.name}",
                status="completed"
            )
            bill.transaction = transaction  # Link bill to the transaction
            bill.save()

        return JsonResponse({"message": "Bill updated successfully"})

def generate_receipt(request, transaction_id):
    #Get the transaction by ID
    transaction = get_object_or_404(Transaction, id=transaction_id)
    
    # Create a receipt for transaction if it doesn't exist
    receipt, created = Receipt.objects.get_or_create(transaction=transaction, user=request.user)
    
    # If thi is a new receipt, you can set up necessary logic here
    if created:
        receipt.amount = transaction.amount  # Assume transaction has an amount field
        receipt.save()
        
    # Render receipt template with the receipt data
    return render(request, 'bills/receipt_pdf.html', {'receipt': receipt})