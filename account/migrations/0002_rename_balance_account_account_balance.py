# Generated by Django 5.0.6 on 2024-06-13 11:48

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='account',
            old_name='balance',
            new_name='account_balance',
        ),
    ]
