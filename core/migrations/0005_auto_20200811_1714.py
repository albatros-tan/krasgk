# Generated by Django 2.2.10 on 2020-08-11 10:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0004_auto_20200811_1659'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pages',
            name='slug',
            field=models.SlugField(unique=True, verbose_name='URL'),
        ),
    ]
