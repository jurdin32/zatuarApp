# Generated by Django 3.0.8 on 2020-07-24 14:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Home', '0006_beneficios_descarga_galeria_proceso_identidad_personalizaion_poducto_proceso'),
    ]

    operations = [
        migrations.CreateModel(
            name='Detalles',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titulo', models.CharField(blank=True, max_length=30, null=True)),
                ('image1', models.FileField(blank=True, null=True, upload_to='detalles')),
                ('image2', models.FileField(blank=True, null=True, upload_to='detalles')),
                ('image3', models.FileField(blank=True, null=True, upload_to='detalles')),
            ],
            options={
                'verbose_name_plural': '8. Detalles',
            },
        ),
        migrations.AlterModelOptions(
            name='descarga',
            options={'verbose_name_plural': '9. Descarga'},
        ),
    ]