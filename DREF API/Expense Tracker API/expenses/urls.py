from django.urls import path, include
from .views import TransactionListCreateAPIView, CategoryModelViewSet
from rest_framework.routers import DefaultRouter 


router = DefaultRouter()
router.register(r'categories', CategoryModelViewSet, basename='category')

urlpatterns = [
    path('transactions/', TransactionListCreateAPIView.as_view(), name='transaction-list-create'),
    path('', include(router.urls)),
]