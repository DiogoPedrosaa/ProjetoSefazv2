# Generated by Django 5.0 on 2024-03-07 10:48

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app_cad_serv', '0052_servidor_tarefas_alter_servidor_setor'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='servidor',
            name='tarefas',
        ),
    ]
