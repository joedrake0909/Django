from django.db import models
from django.core.validators import MinValueValidator

class Transaction(models.Model):

    TYPE_INCOME = 'income'
    TYPE_EXPENSE = 'expense'

    TYPE_CHOICES = [
        (TYPE_INCOME, 'Income'),
        (TYPE_EXPENSE, 'Expense'),
    ]

    amount = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        validators=[MinValueValidator(0.01)],
    )

    category = models.ForeignKey(
        'Category',
        on_delete=models.SET_NULL, 
        null=True, blank=True, 
        related_name='transactions'
    )

    type = models.CharField(max_length=7, choices=TYPE_CHOICES)
    date = models.DateField(auto_now_add=False)
    description = models.TextField(blank=True, default='')

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.type.title()} - {self.amount} on {self.date}"
    

    

class Category(models.Model):
    TYPE_INCOME = 'income'
    TYPE_EXPENSE = 'expense'

    TYPE_CHOICES = [
        (TYPE_INCOME, 'Income'),
        (TYPE_EXPENSE, 'Expense'),
    ]

    name = models.CharField(max_length=100, unique=True)
    type = models.CharField(max_length=7, choices=TYPE_CHOICES)

    class Meta:
        verbose_name_plural = "Categories"

    def __str__(self):
        return f"{self.name} ({self.get_type_display()})"
    
