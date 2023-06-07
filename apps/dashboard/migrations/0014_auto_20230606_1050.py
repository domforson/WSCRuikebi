# Generated by Django 3.2.16 on 2023-06-06 10:50

from decimal import Decimal
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0013_auto_20230606_0654'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='price',
            name='high_time_price',
        ),
        migrations.RemoveField(
            model_name='price',
            name='low_time_price',
        ),
        migrations.RemoveField(
            model_name='price',
            name='separation_timing',
        ),
        migrations.AddField(
            model_name='price',
            name='normal_hourly_price',
            field=models.DecimalField(decimal_places=2, default=Decimal('0'), max_digits=12),
        ),
        migrations.AddField(
            model_name='price',
            name='peek_hourly_price',
            field=models.DecimalField(decimal_places=2, default=Decimal('0'), max_digits=12, null=True),
        ),
        migrations.AddField(
            model_name='price',
            name='peek_time_from',
            field=models.TimeField(null=True),
        ),
        migrations.AddField(
            model_name='price',
            name='peek_time_to',
            field=models.TimeField(null=True),
        ),
    ]