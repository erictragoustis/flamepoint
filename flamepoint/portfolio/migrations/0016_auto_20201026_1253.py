# Generated by Django 3.1.2 on 2020-10-26 10:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0015_auto_20201026_1146'),
    ]

    operations = [
        migrations.AddField(
            model_name='portfolio',
            name='front_image',
            field=models.ImageField(blank=True, null=True, upload_to='portfolio/images/'),
        ),
        migrations.AlterField(
            model_name='portfolio',
            name='feat_image',
            field=models.ImageField(blank=True, null=True, upload_to='portfolio/images/'),
        ),
    ]
