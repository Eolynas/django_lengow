# Generated by Django 3.2.9 on 2021-11-17 10:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0003_auto_20211117_1126'),
    ]

    operations = [
        migrations.AlterField(
            model_name='orders',
            name='order_id',
            field=models.CharField(max_length=200, unique=True),
        ),
    ]
