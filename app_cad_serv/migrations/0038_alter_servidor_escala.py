# Generated by Django 5.0 on 2024-02-01 12:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_cad_serv', '0037_alter_servidor_matricula'),
    ]

    operations = [
        migrations.AlterField(
            model_name='servidor',
            name='escala',
            field=models.CharField(choices=[('A', 'A'), ('B', 'B'), ('C', 'C'), ('D', 'D')], default='', max_length=10),
        ),
    ]
