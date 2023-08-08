# Generated by Django 3.2.16 on 2023-08-08 09:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0026_stadiumimage'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='user_nick_name',
            field=models.CharField(default='', max_length=255),
        ),
        migrations.AlterField(
            model_name='order',
            name='status',
            field=models.CharField(choices=[('Pending Payment', 'Pending Payment'), ('Pending Confirmation', 'Pending Confirmation'), ('Accepted', 'Accepted'), ('Rejected', 'Rejected'), ('Cancelled', 'Cancelled')], default='Pending Payment', max_length=255),
        ),
    ]