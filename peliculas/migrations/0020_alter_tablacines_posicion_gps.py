# Generated by Django 4.1.3 on 2023-01-22 19:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('peliculas', '0019_tablacines'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tablacines',
            name='posicion_gps',
            field=models.DecimalField(decimal_places=14, max_digits=400),
        ),
    ]
