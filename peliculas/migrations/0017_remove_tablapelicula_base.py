# Generated by Django 4.1.3 on 2023-01-20 18:24

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('peliculas', '0016_remove_tablaimagenes_imagen_remove_tablapremio_base_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='tablapelicula',
            name='base',
        ),
    ]