# Generated by Django 5.0.1 on 2024-02-29 06:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('photoVlogApp', '0005_publicacion_descripcion_publicacion_fecha_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='publicacion',
            name='esThumb',
            field=models.BooleanField(default=False),
        ),
    ]