# Generated by Django 2.2.28 on 2023-08-22 17:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rango', '0002_auto_20230822_1611'),
    ]

    operations = [
        migrations.AddField(
            model_name='category',
            name='likes',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='category',
            name='view',
            field=models.IntegerField(default=0),
        ),
    ]
