# Generated by Django 3.2.9 on 2021-11-17 14:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0005_auto_20211117_1528'),
    ]

    operations = [
        migrations.AlterField(
            model_name='orders',
            name='billing_firstname',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='orders',
            name='billing_lastname',
            field=models.CharField(max_length=50, null=True),
        ),
    ]
