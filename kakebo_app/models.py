from django.db import models

CURRENCY_CHOICES = [
    ('EUR', 'Euro'),
    ('USD', 'US Dollar'),
    ('PLN', 'Polish Zloty'),
    ('GBP', 'British Pound'),
    ('JPY', 'Japanese Yen'),
    ('CNY', 'Chinese Yuan'),
    ('CAD', 'Canadian Dollar'),
    ('AUD', 'Australian Dollar'),
    ('NZD', 'New Zealand Dollar'),
    ('CHF', 'Swiss Franc'),
    ('SEK', 'Swedish Krona'),
    ('NOK', 'Norwegian Krone'),
    ('DKK', 'Danish Krone'),
    ('MXN', 'Mexican Peso'),
    ('SGD', 'Singapore Dollar'),
    ('HKD', 'Hong Kong Dollar'),
    ('KRW', 'South Korean Won'),
    ('TRY', 'Turkish Lira'),
    ('RUB', 'Russian Ruble'),
    ('INR', 'Indian Rupee'),
]


class Expense(models.Model):
    CATEGORY_CHOICES = [
        ('BN', 'Basic Needs'),
        ('RF', 'Recreation and Fun'),
        ('CE', 'Culture and Extras'),
        ('EX', 'Extras')
    ]

    category = models.CharField(max_length=2)
    vendor = models.CharField(max_length=100)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    currency = models.CharField(max_length=3, choices=CURRENCY_CHOICES, default='EUR')
    date = models.DateField()


    def __str__(self):
        return f'{self.get_category_display()} Expense'
