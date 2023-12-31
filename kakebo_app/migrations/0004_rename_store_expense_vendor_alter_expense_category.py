# Generated by Django 4.2.3 on 2023-07-16 18:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("kakebo_app", "0003_expense_store"),
    ]

    operations = [
        migrations.RenameField(
            model_name="expense",
            old_name="store",
            new_name="vendor",
        ),
        migrations.AlterField(
            model_name="expense",
            name="category",
            field=models.CharField(
                choices=[
                    ("BN", "Basic Needs"),
                    ("RF", "Recreation and Fun"),
                    ("CE", "Culture and Extras"),
                    ("EX", "Extras"),
                ],
                max_length=2,
            ),
        ),
    ]
