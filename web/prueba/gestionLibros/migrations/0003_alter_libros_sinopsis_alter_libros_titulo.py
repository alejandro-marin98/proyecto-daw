# Generated by Django 4.1.7 on 2023-04-15 17:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gestionLibros', '0002_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='libros',
            name='sinopsis',
            field=models.CharField(blank=True, max_length=10000, null=True),
        ),
        migrations.AlterField(
            model_name='libros',
            name='titulo',
            field=models.CharField(max_length=150, unique=True),
        ),
    ]
