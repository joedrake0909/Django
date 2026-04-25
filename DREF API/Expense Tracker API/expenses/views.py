from rest_framework.generics import ListCreateAPIView
from rest_framework.viewsets import ModelViewSet
from .models import Transaction, Category
from .serializers import TransactionSerializer, CategorySerializer
from datetime import datetime
from rest_framework.exceptions import ValidationError

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

        month_param = self.request.query_params.get('month')
        if month_param:
            try:
                year_month = datetime.strptime(month_param, '%Y-%m')
                month = year_month.month
                year = year_month.year

                queryset = queryset.filter(date__year=year, date__month=month)

            except ValueError:
                return queryset.none()
            
        
        # If month_param fails 
        year_param = self.request.query_params.get('year')
        month_num = self.request.query_params.get('month_num')

        if year_param and month_num:
            try:
                year = int(year_param)
                month = int(month_num)

                if 1 <= month <=12:
                    queryset = queryset.filter(date_year=year, date_month=month)
                else:
                    return queryset.none()
            except ValueError:
                raise ValidationError({"month": "Invalid month format. Use YYYY-MM."})
            
        return queryset

    

class CategoryModelViewSet(ModelViewSet):
    queryset = Category.objects.all().order_by('name')
    serializer_class = CategorySerializer