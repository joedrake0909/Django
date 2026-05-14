from django.shortcuts import render, redirect
from .forms import ExpenseForm
from .models import Expense
from django.db.models import Sum
import datetime
# Create your views here.
def index(request):
    if request.method == 'POST':
        expense = ExpenseForm(request.POST)
        if expense.is_valid():
            expense.save()
    
    # Get request 
    expenses = Expense.objects.all()
    total_expenses = expenses.aggregate(Sum("amount"))['amount__sum']
    expense_form = ExpenseForm()

    # Logic to get expense from last 365 days
    last_year = datetime.date.today() - datetime.timedelta(days=365)
    data = Expense.objects.filter(date__gt=last_year)
    print('last_year', last_year)
    yearly_sum = data.aggregate(Sum("amount"))['amount__sum']
    print('yearly_sum', yearly_sum)

    #logic to get expense from last 30 days
    last_month = datetime.date.today() - datetime.timedelta(days=30)
    data = Expense.objects.filter(date__gt=last_month)
    monthly_sum = data.aggregate(Sum("amount"))['amount__sum']
    print('monthly_sum', monthly_sum)

    # Logic to get expense from last 7 days
    last_week = datetime.date.today() - datetime.timedelta(days=7)
    data = Expense.objects.filter(date__gt=last_week)
    weekly_sum = data.aggregate(Sum("amount"))['amount__sum']
    print('weekly_sum', weekly_sum)

    # Logic to get daily expense
    daily_sum = Expense.objects.filter().values('date').order_by('date').annotate(sum=Sum('amount'))
    print('daily_sum', daily_sum)

    # logic to get category sum
    categorical_sum = Expense.objects.filter().values('category').annotate(sum=Sum('amount'))

    return render(request, 'myapp/index.html', {'expense_form': expense_form, 'expenses': expenses, 'total_expenses': total_expenses, 'yearly_sum': yearly_sum, 'monthly_sum': monthly_sum, 'weekly_sum': weekly_sum, 'daily_sum': daily_sum, 'categorical_sum': categorical_sum})


def edit(request, id):
    expense = Expense.objects.get(id=id)
    expense_form = ExpenseForm(instance=expense)

    if request.method == 'POST':
        form = ExpenseForm(request.POST, instance=expense)
        if form.is_valid():
            form.save()
            return redirect('index')
    return render(request, 'myapp/edit.html', {'expense_form': expense_form})

def delete(request, id):
    expense = Expense.objects.get(id=id)
    if request.method == 'POST':
        expense.delete()
    return redirect('index')
    
