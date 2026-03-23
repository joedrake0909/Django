from django.db import models
from django.urls import reverse

# Create your models here.
class Item(models.Model):
    item_name = models.CharField(max_length=200)
    item_desc = models.TextField()
    item_price = models.IntegerField()
    item_image = models.CharField(max_length=500, default='https://neon-factory.com/cdn/shop/products/eat-512-Culinary_-eat_-food_-holiday_-tourism_-travel_-vacation_e99d9a61-53f7-4f9c-95fc-c974cccc1445_1200x1200.png?v=1575239933')


    def __str__(self):
        return self.item_name

    def get_absolute_url(self):
        return reverse("myapp:index")

