# Generated by Django 3.0.5 on 2020-05-22 19:02

import ckeditor.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('persona', '0005_empleado_hoja_vida'),
    ]

    operations = [
        migrations.AlterField(
            model_name='empleado',
            name='hoja_vida',
            field=ckeditor.fields.RichTextField(blank=True, verbose_name='Coloque descripción'),
        ),
        migrations.AlterField(
            model_name='empleado',
            name='job',
            field=models.CharField(choices=[('contador', 'Contador'), ('1', 'Administrador'), ('2', 'Economista'), ('3', 'Otro')], max_length=50, verbose_name='Trabajo'),
        ),
    ]
