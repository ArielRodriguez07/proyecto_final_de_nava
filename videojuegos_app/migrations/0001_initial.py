# Generated by Django 5.1 on 2024-12-02 14:57

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Videojuegos',
            fields=[
                ('id_videojuego', models.IntegerField(primary_key=True, serialize=False)),
                ('titulo', models.CharField(max_length=100)),
                ('genero', models.CharField(max_length=100)),
                ('plataforma', models.CharField(max_length=100)),
                ('precio', models.IntegerField()),
                ('stock', models.IntegerField()),
                ('fecha_lanzamiento', models.DateField()),
            ],
        ),
    ]