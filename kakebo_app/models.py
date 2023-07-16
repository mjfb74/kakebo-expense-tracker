from django.db import models

class Expense(models.Model):
    CATEGORY_CHOICES = [
        ('BN', 'Basic Needs'),
        ('RF', 'Recreation and Fun'),
        ('CE', 'Culture and Extras'),
        ('EX', 'Extras')
    ]

    category = models.CharField(max_length=2, choices=CATEGORY_CHOICES)
    amount = models.DecimalField(max_digits=7, decimal_places=2)
    date = models.DateField()
    vendor = models.CharField(max_length=50, default='')
    description = models.TextField(default='')


    def __str__(self):
        return f'{self.get_category_display()} Expense'
