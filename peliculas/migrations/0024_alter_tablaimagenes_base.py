# Generated by Django 4.1.3 on 2023-01-23 16:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('peliculas', '0023_alter_tablapersona_sueldo_mensual'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tablaimagenes',
            name='base',
            field=models.BinaryField(),
        ),
    ]
