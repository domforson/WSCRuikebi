# Generated by Django 3.2.16 on 2023-06-01 06:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0005_alter_freeze_court_type'),
    ]

    operations = [
        migrations.AlterField(
            model_name='freeze',
            name='court_type',
            field=models.CharField(blank=True, choices=[('FULL', 'Full'), ('HALF', 'Half'), ('QUARTER', 'Quarter')], default=None, max_length=255, null=True),
        ),
    ]
