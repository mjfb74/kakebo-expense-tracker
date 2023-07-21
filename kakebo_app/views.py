from django.shortcuts import render, redirect, get_object_or_404
from .forms import ExpenseForm, CurrencyConversionForm
from .models import Expense
from django.db.models import Sum
from django.utils import timezone
from django.db.models.functions import TruncMonth
from django.db.models import DateTimeField, Q, Sum
from datetime import datetime
from calendar import month_name
import requests
from .constants import CURRENCY_CODES


def home(request):
    return render(request, 'home.html')


def enter_expense(request):
    if request.method == 'POST':
        form = ExpenseForm(request.POST)    
        if form.is_valid():                 
            form.save()             
            return redirect('enter_expense') 
    else:
        form = ExpenseForm()          
    return render(request, 'enter_expense.html', {'form': form})        


def expenses_list(request):
    expenses = Expense.objects.all()

    category = request.GET.get('category', '')
    vendor = request.GET.get('vendor', '')
    date = request.GET.get('date', '')
    min_amount = request.GET.get('min_amount', '')
    max_amount = request.GET.get('max_amount', '')

    if category:
        expenses = expenses.filter(category=category)
    if vendor:
        expenses = expenses.filter(vendor__icontains=vendor)
    if date:
        expenses = expenses.filter(date__year=date.split('-')[0], date__month=date.split('-')[1])
    if min_amount:
        expenses = expenses.filter(amount__gte=min_amount)
    if max_amount:
        expenses = expenses.filter(amount__lte=max_amount)

    expenses = expenses.order_by('date')

    # Summarize expenses by category
    category_sums = expenses.values('category').annotate(total=Sum('amount'))

    category_names = {
        'BN': 'Basic Needs',
        'RF': 'Recreation and Fun',
        'CE': 'Culture and Extras',
        'EX': 'Extras',
    }

    category_data = [{'category': category_names.get(item['category'], 'Unknown'), 'total': item['total']} for item in category_sums]

    category_codes = Expense.objects.values_list('category', flat=True).distinct()
    categories = [(code, category_names.get(code, 'Unknown')) for code in category_codes]

    for expense in expenses:
        if expense.currency != 'EUR':
            exchange_rate = get_exchange_rate(expense.currency, 'EUR')
            if exchange_rate is not None:
                expense.amount = round(expense.amount * exchange_rate, 2)

    return render(request, 'expenses_list.html', {'expenses': expenses, 'categories': categories, 'category_data': category_data})
    

def edit_expense(request, expense_id):
    expense = Expense.objects.get(id=expense_id)
    if request.method == 'POST':
        form = ExpenseForm(request.POST, instance=expense)
        if form.is_valid():
            form.save()
            return redirect('expenses_list')
    else:
        form = ExpenseForm(instance=expense)
    return render(request, 'edit_expense.html', {'form': form})


def delete_expense(request, expense_id):
    expense = get_object_or_404(Expense, id=expense_id)
    if request.method == 'POST':
        expense.delete()
        return redirect('expenses_list')
    else:
        return render(request, 'confirm_delete.html', {'expense': expense})


def get_sums(request):
    if request.method == 'POST':
        date = request.POST.get('date')
        year, month = map(int, date.split('-')) 
        sums = Expense.objects.filter(date__year=year, date__month=month).values('category').annotate(total=Sum('amount'))
        category_names = {
            'BN': 'Basic Needs',
            'RF': 'Recreation and Fun',
            'CE': 'Culture and Extras',
            'EX': 'Extras',
        }
        for item in sums:
            item['category_name'] = category_names.get(item['category'], 'Unknown')

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


def get_exchange_rate(base_currency, target_currency):
    response = requests.get(f'https://api.exchangeratesapi.io/latest?base={base_currency}')
    rates = response.json().get('rates', {})
    return rates.get(target_currency, 1)  # This should return a single numeric value


def currency_conversion(request):
    form = CurrencyConversionForm()
    context = {'form': form}

    if request.method == 'POST':
        form = CurrencyConversionForm(request.POST)
        if form.is_valid():
            amount = form.cleaned_data['amount']
            base_currency = form.cleaned_data['base_currency']
            target_currency = form.cleaned_data['target_currency']

            api_key = "5f31b205544b5f29fe4fb271919152c7"
            response = requests.get(f"http://api.exchangeratesapi.io/v1/latest?access_key={api_key}")
            data = response.json()

            base_rate = data['rates'][base_currency]
            conversion_rate = data['rates'][target_currency]
            converted_amount = round(amount * conversion_rate / base_rate, 2)

            context = {
                'form': form,
                'base_currency': base_currency,
                'target_currency': target_currency,
                'amount': amount,
                'converted_amount': converted_amount
            }

    return render(request, 'currency_conversion.html', context)


def set_currency(request):
    if request.method == 'POST':
        selected_currency = request.POST.get('currency')
        if selected_currency in CURRENCY_CODES:
            request.session['currency'] = selected_currency
        return redirect('enter_expense')
    else:
        # Show the form with the list of currencies
        return render(request, 'set_currency.html', {'currencies': CURRENCY_CODES})


