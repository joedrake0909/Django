from django.contrib import admin
from .models import Transaction, Category

@admin.register(Transaction)
class TransactionAdmin(admin.ModelAdmin):
    list_display = ('id', 'type', 'amount', 'date', 'category', 'description', 'created_at', 'updated_at')
    list_filter  = ('type', 'category', 'date')
    search_fields = ('description',)
    raw_id_fields = ('category',)

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_dispaly = ('name', 'type')
    list_filter = ('type',)
    search_fields = ('name',)

