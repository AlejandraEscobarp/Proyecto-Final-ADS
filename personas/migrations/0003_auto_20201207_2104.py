# Generated by Django 3.1.3 on 2020-12-08 03:04

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('personas', '0002_estudiante_seccion'),
    ]

    operations = [
        migrations.RenameField(
            model_name='familia',
            old_name='Estudiante',
            new_name='estudiante',
        ),
    ]