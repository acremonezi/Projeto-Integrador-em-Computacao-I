# Generated by Django 3.2.8 on 2021-10-16 20:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('course', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='course',
            name='url',
            field=models.URLField(default=1),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='course',
            name='thumb',
            field=models.ImageField(upload_to='courses_images'),
        ),
    ]