# Generated by Django 3.1.2 on 2020-10-23 16:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0011_portfolio_is_featured'),
    ]

    operations = [
        migrations.AlterField(
            model_name='portfolio',
            name='tags',
            field=models.ManyToManyField(blank=True, to='portfolio.Tag'),
        ),
        migrations.AlterField(
            model_name='portfolio',
            name='technologies',
            field=models.ManyToManyField(blank=True, to='portfolio.Technology'),
        ),
    ]
