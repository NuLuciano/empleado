# Generated by Django 3.0.5 on 2020-05-22 19:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('persona', '0006_auto_20200522_1602'),
    ]

    operations = [
        migrations.AlterField(
            model_name='empleado',
            name='job',
            field=models.CharField(choices=[('contador', 'Contador'), ('administrador', 'Administrador'), ('economista', 'Economista'), ('otro', 'Otro')], max_length=50, verbose_name='Trabajo'),
        ),
    ]
