# Generated by Django 3.1.2 on 2020-10-22 11:46

import ckeditor_uploader.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0006_auto_20201022_1355'),
    ]

    operations = [
        migrations.AddField(
            model_name='portfolio',
            name='description',
            field=ckeditor_uploader.fields.RichTextUploadingField(blank=True, null=True),
        ),
    ]
