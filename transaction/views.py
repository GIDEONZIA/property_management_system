from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Transaction
from .serializers import TransactionSerializer

class TransactionCreateView(APIView):
    def post(self, request):
        # Create a new transaction
        serializer = TransactionSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()  # Save the transaction to the database
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class TransactionListView(APIView):
    def get(self, request):
        # List all transactions
        transactions = Transaction.objects.all()
        serializer = TransactionSerializer(transactions, many=True)
        return Response(serializer.data)
