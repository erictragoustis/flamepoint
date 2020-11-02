# Generated by Django 3.1.3 on 2020-11-02 11:07

from django.db import migrations, models
import image_optimizer.fields


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_auto_20201026_1830'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='comp_image',
            field=image_optimizer.fields.OptimizedImageField(blank=True, null=True, upload_to='blog/images/comp'),
        ),
        migrations.AlterField(
            model_name='post',
            name='feat_image',
            field=models.ImageField(upload_to='blog/images/comp'),
        ),
    ]
