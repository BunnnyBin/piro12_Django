# Generated by Django 2.2.9 on 2020-01-21 08:04

import askcompany.utils
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0004_post_photo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='photo',
            field=models.ImageField(blank=True, upload_to=askcompany.utils.uuid_upload_to),
        ),
    ]
