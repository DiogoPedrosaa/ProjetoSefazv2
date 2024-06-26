# Generated by Django 5.0 on 2024-06-07 12:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_cad_serv', '0056_servidor_teste_tarefas'),
    ]

    operations = [
        migrations.AlterField(
            model_name='servidor',
            name='setor',
            field=models.CharField(choices=[('', ''), ('Apoio Atendimento', 'Apoio Atendimento'), ('Arrecadação', 'Arrecadação'), ('ASCOM', 'ASCOM'), ('Cadastro Imobiliário', 'Cadastro Imobiliário'), ('Cadastro Mercantil', 'Cadastro Mercantil'), ('Coord. Geral da Receita Municipal', 'Coord. Geral da Receita Municipal'), ('Coord. Geral de Auditoria Fiscal', 'Coord. Geral de Auditoria Fiscal'), ('Coord. de Gestão de Pessoas', 'Coord. de Gestão de Pessoas'), ('Coord. De Tec. da Informação e Telecomunicações', 'Coord. De Tec. da Informação e Telecomunicações'), ('Digitalização CTIT', 'Digitalização CTIT'), ('Diretoria Administrativa', 'Diretoria Administrativa'), ('Diretoria da Receita Municipal', 'Diretoria da Receita Municipal'), ('Diretoria de Gestão de Contatros e Contratações', 'Diretoria de Gestão de Contatros e Contratações'), ('Diretoria do Atendimento ao Contribuinte', 'Diretoria do Atendimento ao Contribuinte'), ('DTM', 'DTM'), ('Gab Orçamento', 'Gabinete Orçamento'), ('Geoprocessamento', 'Geoprocessamento'), ('Inteligência fiscal', 'Inteligência fiscal'), ('ITBI', 'ITBI'), ('Orçamento', 'Orçamento'), ('Subsecretaria da Receita Municipal', 'Subsecretaria da Receita Municipal'), ('Superintendência', 'Superintendência'), ('UGOCC', 'UGOCC')], default='', max_length=100),
        ),
    ]
