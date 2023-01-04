# Generated by Django 4.1.5 on 2023-01-04 17:25

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Departamentos',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=50, verbose_name='Nombre')),
                ('nombre_corto', models.CharField(max_length=20, verbose_name='Nombre corto')),
                ('activo', models.BooleanField(default=True, verbose_name='Activo')),
            ],
        ),
    ]
