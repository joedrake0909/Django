from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Item
from .forms import ItemForm
from django.contrib.auth.decorators import login_required
from django.views.generic import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy

# Create your views here.


class IndexClassView(ListView):
    model = Item
    template_name = "myapp/index.html"
    context_object_name = "item_list"

def results(request):
    return HttpResponse("This is a results ")

#def detail(request, id):
    item = Item.objects.get(id=id)
    context = {
        'item': item,
    }
    return render(request, "myapp/detail.html", context)


class FoodDetailView(DetailView):
    model = Item
    template_name = "myapp/detail.html"
    context_object_name = "item"

#def create_item(request):
    #form = ItemForm(request.POST or None)
   # if request.method == "POST":
   #     if form.is_valid():
 #           form.save()
 #           return redirect('myapp:index')
 #   context = {
  #      'form' : form,
#    }
 #   return render(request, "myapp/item-form.html", context)

class FoodCreateView(CreateView):
    model = Item
    fields = ['item_name', 'item_desc', 'item_price', 'item_image']
    


#def update_item(request, id):
   # item = Item.objects.get(id=id)
   # form = ItemForm(request.POST or None,instance=item)
   # if form.is_valid():
   #     form.save()
  #      return redirect('myapp:index')

 #   context = {
 #       'form': form,
 #   }
    #return render(request, "myapp/item-form.html", context)


class ItemUpdateView(UpdateView):
    model = Item
    fields = ['item_name', 'item_desc', 'item_price', 'item_image']
    template_name_suffix = "_update_form"



#def delete_item(request, id):
    # Load the item that may be deleted.
   # item = Item.objects.get(id=id)
    # Only delete after the user confirms via POST.
   # if request.method=="POST":
        # Remove the item from the database.
       # item.delete()
        # Go back to the list page after deletion.
       # return redirect('myapp:index')
    
    # Show the confirmation page for non-POST requests.
    #return render(request, 'myapp/item-delete.html')



class ItemDelete(DeleteView):
    model = Item
    success_url = reverse_lazy('myapp:index')
   