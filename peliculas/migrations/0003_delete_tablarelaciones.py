# Generated by Django 4.1.3 on 2022-11-30 15:25

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('peliculas', '0002_rename_nombre_premio_tablapremio_premio_ganador'),
    ]

    operations = [
        migrations.DeleteModel(
            name='tablaRelaciones',
        ),
    ]
