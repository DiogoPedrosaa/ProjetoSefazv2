# Generated by Django 5.0 on 2024-02-08 12:14

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app_cad_serv', '0046_auto_20240208_0912'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='tarefarealizada',
            name='colaborador',
        ),
    ]
