# Generated by Django 5.1.4 on 2024-12-28 00:04

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gestion', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='transaccion',
            name='nombre',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='gestion.usuario'),
        ),
    ]
