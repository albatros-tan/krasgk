# Generated by Django 2.2.10 on 2020-08-11 08:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Pages',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('priority', models.PositiveSmallIntegerField(default=1)),
                ('title', models.CharField(max_length=255)),
                ('header', models.CharField(max_length=255)),
                ('url', models.CharField(max_length=255)),
                ('slug', models.SlugField(max_length=255)),
            ],
            options={
                'verbose_name': 'Страница',
                'verbose_name_plural': 'Страницы',
                'ordering': ['priority'],
            },
        ),
        migrations.AlterModelOptions(
            name='servicetable',
            options={'verbose_name': 'Сервисная таблица', 'verbose_name_plural': 'Сервисных записей'},
        ),
    ]
