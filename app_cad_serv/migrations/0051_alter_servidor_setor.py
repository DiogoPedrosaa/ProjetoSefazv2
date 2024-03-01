# Generated by Django 5.0 on 2024-02-27 13:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_cad_serv', '0050_alter_servidor_setor'),
    ]

    operations = [
        migrations.AlterField(
            model_name='servidor',
            name='setor',
            field=models.CharField(choices=[('', ''), ('Apoio Atendimento', 'Apoio Atendimento'), ('Arrecadação', 'Arrecadação'), ('ASCOM', 'ASCOM'), ('Cadastro Imobiliário', 'Cadastro Imobiliário'), ('Cadastro Mercantil', 'Cadastro Mercantil'), ('CAF', 'CAF'), ('Catraca', 'Catraca'), ('Cont e convênios', 'Cont e convênios'), ('Coord Geral da rec', 'Coord Geral da rec'), ('CTIT', 'CTIT'), ('Digitalização-CTIT', 'Digitalização-CTIT'), ('Diret Atend Contri', 'Diret Atend Contri'), ('Diret Rec Mun', 'Diret Rec Mun'), ('Diretoria ADM', 'Diretoria ADM'), ('DTM', 'DTM'), ('Gab Orçamento', 'Gab Orçamento'), ('Geoprocessamento', 'Geoprocessamento'), ('Inteligência fiscal', 'Inteligência fiscal'), ('ITBI', 'ITBI'), ('Orçamento', 'Orçamento'), ('RH', 'RH'), ('Subsec Rec Mun', 'Subsec Rec Mun'), ('Superintendência', 'Superintendência'), ('Triagem', 'Triagem'), ('UGOCC', 'UGOCC')], default='', max_length=100),
        ),
    ]
