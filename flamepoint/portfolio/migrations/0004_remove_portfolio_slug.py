# Generated by Django 3.1.2 on 2020-10-22 10:54

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0003_portfolio_slug'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='portfolio',
            name='slug',
        ),
    ]
