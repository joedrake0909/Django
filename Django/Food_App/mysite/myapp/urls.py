from django.urls import path
from . import views

app_name = 'myapp'

urlpatterns = [
    path('', views.index, name='index'),
    path('results/', views.results),
    path('<int:id>/', views.detail, name='detail'),
    path('update/<int:id>/', views.update_item, name='update_item'),
    path('delete/<int:id>/', views.delete_item, name='delete_item'),
    path('add/', views.create_item, name='create_item'),
]

