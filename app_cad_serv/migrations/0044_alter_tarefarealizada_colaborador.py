# Generated by Django 5.0 on 2024-02-08 12:03

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_cad_serv', '0043_remove_tarefarealizada_servidor'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tarefarealizada',
            name='colaborador',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app_cad_serv.servidor'),
        ),
    ]
