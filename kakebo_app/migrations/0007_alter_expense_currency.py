# Generated by Django 4.2.3 on 2023-07-20 19:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("kakebo_app", "0006_alter_expense_currency"),
    ]

    operations = [
        migrations.AlterField(
            model_name="expense",
            name="currency",
            field=models.CharField(
                choices=[
                    ("EUR", "Euro"),
                    ("USD", "US Dollar"),
                    ("GBP", "British Pound"),
                    ("JPY", "Japanese Yen"),
                    ("CNY", "Chinese Yuan"),
                    ("CAD", "Canadian Dollar"),
                    ("CHF", "Swiss Franc"),
                    ("SEK", "Swedish Krona"),
                    ("NOK", "Norwegian Krone"),
                    ("DKK", "Danish Krone"),
                    ("MXN", "Mexican Peso"),
                    ("SGD", "Singapore Dollar"),
                    ("HKD", "Hong Kong Dollar"),
                    ("KRW", "South Korean Won"),
                    ("TRY", "Turkish Lira"),
                    ("RUB", "Russian Ruble"),
                    ("INR", "Indian Rupee"),
                    ("PLN", "Polish Zloty"),
                ],
                default="EUR",
                max_length=3,
            ),
        ),
    ]
