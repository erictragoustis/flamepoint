# Generated by Django 3.1.2 on 2020-10-22 10:55

import autoslug.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0004_remove_portfolio_slug'),
    ]

    operations = [
        migrations.AddField(
            model_name='portfolio',
            name='slug',
            field=autoslug.fields.AutoSlugField(default=10, editable=False, populate_from='title', unique=True, verbose_name='Portfolio Title'),
        ),
    ]