from django import forms
from .models import Expense
from .constants import CURRENCY_CODES

class CurrencyConversionForm(forms.Form):
    amount = forms.FloatField()
    base_currency = forms.ChoiceField(choices=[(code, code) for code in CURRENCY_CODES])
    target_currency = forms.ChoiceField(choices=[(code, code) for code in CURRENCY_CODES])

class ExpenseForm(forms.ModelForm):
    class Meta:
        model = Expense
        fields = ['category', 'vendor', 'amount', 'currency', 'date']

