# Generated by Django 3.2.9 on 2021-11-21 01:30

import certificate.utils
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('certificate', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='certificate',
            name='authentication_key',
            field=models.CharField(blank=True, default=certificate.utils.create_authentication_key, editable=False, max_length=100, unique=True),
        ),
    ]
