from rest_framework.generics import ListCreateAPIView
from .models import Transaction
from .serializers import TransactionSerializer

class TransactionListCreateAPIView(ListCreateAPIView):
    queryset = Transaction.objects.all().order_by('-date')
    serializer_class = TransactionSerializer
    