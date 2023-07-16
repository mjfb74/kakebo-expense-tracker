from django.shortcuts import render, redirect, get_object_or_404
from .forms import ExpenseForm
from .models import Expense
from django.db.models import Sum
from django.utils import timezone
from django.db.models.functions import TruncMonth
from django.db.models import DateTimeField
from datetime import datetime
from calendar import month_name


def enter_expense(request):
    if request.method == 'POST':
        form = ExpenseForm(request.POST)    # A form bound to the POST data
        if form.is_valid():                 # All validation rules pass
            form.save()                 # Save the data
            return redirect('enter_expense')  # Redirect after POST
    else:
        form = ExpenseForm()            # An unbound form
    return render(request, 'enter_expense.html', {'form': form})        


def get_sums(request):
    if request.method == 'POST':
        date = request.POST.get('date')
        year, month = map(int, date.split('-'))  # split the date string into year and month
        sums = Expense.objects.filter(date__year=year, date__month=month).values('category').annotate(total=Sum('amount'))
        category_names = {
            'BN': 'Basic Needs',
            'RF': 'Recreation and Fun',
            'CE': 'Culture and Extras',
            'EX': 'Extras',
        }
        for item in sums:
            item['category_name'] = category_names.get(item['category'], 'Unknown')

        # Convert 'month_year' to a datetime object
        month_year = datetime(year=year, month=month, day=1)
        
        return render(request, 'sums.html', {'sums': sums, 'month_year': month_year})
    else:
        # Get all unique months for which expenses have been recorded.
        unique_dates = Expense.objects.annotate(month=TruncMonth('date')).values('month').distinct()
        return render(request, 'get_sums.html', {'dates': unique_dates})


def category_detail(request, category, year, month):
    category_names = {
        'BN': 'Basic Needs',
        'RF': 'Recreation and Fun',
        'CE': 'Culture and Extras',
        'EX': 'Extras',
    }
    category_name = category_names.get(category, 'Unknown')
    month_number = list(month_name).index(month)
    expenses = Expense.objects.filter(category=category, date__year=year, date__month=month_number).order_by('date')
    for expense in expenses:
        expense.category_name = category_name

    context = {
        'expenses': expenses,
        'month_year': f"{month} {year}",
        'category_name': category_name
    }
    return render(request, 'category_detail.html', context)




