# Generated by Django 3.1.3 on 2020-11-02 11:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0004_auto_20201102_1307'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='feat_image',
            field=models.ImageField(upload_to='blog/images'),
        ),
    ]
