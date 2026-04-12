from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User
from .managers import ItemManager
from django.utils import timezone

# Create your models here.
class Item(models.Model):

    class Meta:
        indexes = [
            models.Index(fields=['item_name', 'item_price']),
        ]

    def delete(self, using=None, keep_parents=False):
        self.is_deleted = True
        self.deleted_at = timezone.now()
        self.save()

    user_name = models.ForeignKey(User, on_delete=models.CASCADE, default=1)
    item_name = models.CharField(max_length=200, db_index=True)
    item_desc = models.TextField()
    item_price = models.DecimalField(max_digits=6, decimal_places=2, db_index=True)
    item_image = models.URLField(max_length=500, default='https://neon-factory.com/cdn/shop/products/eat-512-Culinary_-eat_-food_-holiday_-tourism_-travel_-vacation_e99d9a61-53f7-4f9c-95fc-c974cccc1445_1200x1200.png?v=1575239933')
    is_available = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)

    is_deleted = models.BooleanField(default=False)
    deleted_at = models.DateTimeField(null=True, blank=True)


    def __str__(self):
        return self.item_name

    def get_absolute_url(self):
        return reverse("myapp:index")

    objects = ItemManager()
    all_objects = models.Manager()