# Generated by Django 5.0 on 2023-12-19 12:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_cad_serv', '0017_servidor_tipo_modalidade'),
    ]

    operations = [
        migrations.AddField(
            model_name='servidor',
            name='mes_referencia',
            field=models.CharField(default='', max_length=20),
        ),
    ]
