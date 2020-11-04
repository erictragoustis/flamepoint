# Generated by Django 3.1.3 on 2020-11-02 11:18

from django.db import migrations
import image_optimizer.fields


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0018_auto_20201027_1103'),
    ]

    operations = [
        migrations.AlterField(
            model_name='portfolio',
            name='feat_image',
            field=image_optimizer.fields.OptimizedImageField(blank=True, null=True, upload_to='portfolio/images/'),
        ),
        migrations.AlterField(
            model_name='portfolio',
            name='front_image',
            field=image_optimizer.fields.OptimizedImageField(blank=True, null=True, upload_to='portfolio/images/'),
        ),
    ]