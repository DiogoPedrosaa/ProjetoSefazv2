# Generated by Django 5.0 on 2024-01-16 12:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_cad_serv', '0028_pessoa_alter_servidor_setor'),
    ]

    operations = [
        migrations.AddField(
            model_name='pessoa',
            name='pessoa_mat',
            field=models.CharField(default='', max_length=20),
        ),
    ]
