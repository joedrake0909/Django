from django.shortcuts import render
from django.http import HttpResponse
from .models import Item

# Create your views here.

def index(request):
    # Get all items from the database
    item_list = Item.objects.all()
    # Pass the item list to the template context
    context = {
        'item_list' : item_list,
    }
    # Render the template with the context data
    return render(request, "myapp/index.html", context)

def results(request):
    return HttpResponse("This is a results ")


