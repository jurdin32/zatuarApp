# Generated by Django 3.0.8 on 2020-07-24 18:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Clientes', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='cliente',
            name='client',
        ),
        migrations.AlterField(
            model_name='cliente',
            name='slug',
            field=models.SlugField(blank=True, unique=True),
        ),
    ]
