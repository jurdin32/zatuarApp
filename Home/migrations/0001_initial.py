# Generated by Django 3.0.8 on 2020-07-24 01:41

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Casas',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('color', models.CharField(max_length=40)),
                ('duenio', models.CharField(max_length=40)),
            ],
        ),
    ]
