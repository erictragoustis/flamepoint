# Generated by Django 3.1.2 on 2020-10-23 17:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0012_auto_20201023_1917'),
    ]

    operations = [
        migrations.AddField(
            model_name='portfolio',
            name='social_url',
            field=models.URLField(blank=True, null=True),
        ),
    ]
