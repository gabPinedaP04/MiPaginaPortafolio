# Generated by Django 5.0.2 on 2024-03-17 02:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('photoVlogApp', '0007_rename_esthumb_publicacion_esthumblugares_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='publicacion',
            name='categoria',
            field=models.CharField(default='photo', max_length=25),
            preserve_default=False,
        ),
    ]
