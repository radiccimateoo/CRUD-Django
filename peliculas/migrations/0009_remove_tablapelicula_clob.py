# Generated by Django 4.1.3 on 2022-12-14 16:36

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('peliculas', '0008_alter_tablapelicula_clob'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='tablapelicula',
            name='clob',
        ),
    ]