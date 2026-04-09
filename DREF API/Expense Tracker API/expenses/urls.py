from django.urls import path
from .views import TransactionListCreateAPIView

urlpatterns = [
    path('transactions/', TransactionListCreateAPIView.as_view(), name='transaction-list-create'),
]