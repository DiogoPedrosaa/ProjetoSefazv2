# Generated by Django 5.0 on 2024-02-08 12:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_cad_serv', '0047_remove_tarefarealizada_colaborador'),
    ]

    operations = [
        migrations.AddField(
            model_name='tarefarealizada',
            name='colaborador',
            field=models.CharField(default=1, max_length=150),
            preserve_default=False,
        ),
    ]
