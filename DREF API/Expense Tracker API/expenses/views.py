from rest_framework.generics import ListCreateAPIView
from rest_framework.viewsets import ModelViewSet
from .models import Transaction, Category
from .serializers import TransactionSerializer, CategorySerializer

class TransactionListCreateAPIView(ListCreateAPIView):
    queryset = Transaction.objects.all().order_by('-date')
    serializer_class = TransactionSerializer

    def get_queryset(self):
        queryset = Transaction.objects.all().order_by('-date')

        transaction_type = self.request.query_params.get('type')

        if transaction_type :
            if transaction_type  in ['income', 'expense']:
                queryset = queryset.filter(type=transaction_type)

            else:
                queryset = queryset.none()

        return queryset
    

class CategoryModelViewSet(ModelViewSet):
    queryset = Category.objects.all().order_by('name')
    serializer_class = CategorySerializer