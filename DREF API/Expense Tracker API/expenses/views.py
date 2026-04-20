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

        category_param = self.request.query_params.get('category')
        if category_param:
            if category_param.isdigit():
                queryset = queryset.filter(category_id=category_param)
            else:
                queryset = queryset.filter(category__name__iexact=category_param)
            
        return queryset

    

class CategoryModelViewSet(ModelViewSet):
    queryset = Category.objects.all().order_by('name')
    serializer_class = CategorySerializer