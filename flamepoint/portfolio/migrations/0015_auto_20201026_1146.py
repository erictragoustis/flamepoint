# Generated by Django 3.1.2 on 2020-10-26 09:46

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0014_auto_20201026_1141'),
    ]

    operations = [
        migrations.RenameField(
            model_name='portfolio',
            old_name='video_url',
            new_name='video_id',
        ),
    ]
