from django.db import models
from django.core.exceptions import ValidationError
from django.utils.translation import gettext as _
import locale
from django.contrib.auth.models import AbstractUser, Group, Permission, User
import datetime


class Servidor(models.Model):


    def validar_nome(value):
        if any(char.isdigit() for char in value):
            raise ValidationError('O nome não pode conter números.')

    def validar_matricula(value):
        if not all(char.isdigit() or char == '-' for char in value):
         raise ValidationError('A matrícula deve conter apenas números ou traço.')

    ESCALA_CHOICES = [
        ('', ''),
        ('A', 'A'),
        ('B', 'B'),
        ('C', 'C'),
        ('D', 'D'),
    ]
    
    PONTUALIDADE_CHOICES = [
        ('', ''),
        ('10', '10'),
        ('08', '08'),
        ('04', '04'),
        ('02', '02'),
    ]

    ASSIDUIDADE_CHOICES = [
        ('', ''),
        ('10', '10'),
        ('08', '08'),
        ('04', '04'),
        ('02', '02'),
    ]

    EXECUCAO_TAREFAS_CHOICES = [
        ('', ''),
        ('30', '30'),
        ('20', '20'),
        ('15', '15'),
        ('10', '10'),
    ]

    INICIATIVA_CHOICES = [
        ('', ''),
        ('20', '20'),
        ('15', '15'),
        ('10', '10'),
        ('05', '05'),
    ]

    ATENDIMENTO_SERVICOS_CHOICES = [
        ('', ''),
        ('20', '20'),
        ('15', '15'),
        ('10', '10'),
        ('05', '05'),
    ]

    TIPO_ESCALA_CHOICES = [
        ('', ''),
        ('DIRETA', 'Direta'),
        ('INDIRETA', 'Indireta'),
    ]

    TIPO_MODALIDADE_CHOICES = [
        ('', ''),
        ('PRESENCIAL', 'Presencial'),
        ('REMOTO', 'Remoto'),
    ]


    MES_REFERENCIA_CHOICES = [
        ('1', 'Janeiro'),
        ('2', 'Fevereiro'),
        ('3', 'Março'),
        ('4', 'Abril'),
        ('5', 'Maio'),
        ('6', 'Junho'),
        ('7', 'Julho'),
        ('8', 'Agosto'),
        ('9', 'Setembro'),
        ('10', 'Outubro'),
        ('11', 'Novembro'),
        ('12', 'Dezembro'),
    ]
    
    SETOR_CHOICES = [
    ('', ''),
    ('Apoio Atendimento', 'Apoio Atendimento'),
    ('Arrecadação', 'Arrecadação'),
    ('ASCOM', 'ASCOM'),
    ('Cadastro Imobiliário', 'Cadastro Imobiliário'),
    ('Cadastro Mercantil', 'Cadastro Mercantil'),
    ('Coord. Geral da Receita Municipal', 'Coord. Geral da Receita Municipal'),
    ('Coord. Geral de Auditoria Fiscal', 'Coord. Geral de Auditoria Fiscal'),
    ('Coord. de Gestão de Pessoas', 'Coord. de Gestão de Pessoas'),
    ('Coord. De Tec. da Informação e Telecomunicações', 'Coord. De Tec. da Informação e Telecomunicações'),
    ('Digitalização CTIT', 'Digitalização CTIT'),
    ('Diretoria Administrativa', 'Diretoria Administrativa'),
    ('Diretoria da Receita Municipal', 'Diretoria da Receita Municipal'),
    ('Diretoria de Gestão de Contatros e Contratações', 'Diretoria de Gestão de Contatros e Contratações'),
    ('Diretoria do Atendimento ao Contribuinte', 'Diretoria do Atendimento ao Contribuinte'),
    ('DTM', 'DTM'),
    ('Gab Orçamento', 'Gabinete Orçamento'),
    ('Geoprocessamento', 'Geoprocessamento'),
    ('Inteligência fiscal', 'Inteligência fiscal'),
    ('ITBI', 'ITBI'),
    ('Orçamento', 'Orçamento'),
    ('Subsecretaria da Receita Municipal', 'Subsecretaria da Receita Municipal'),
    ('Superintendência', 'Superintendência'),
    ('UGOCC', 'UGOCC'),
]
    
    
    def calcular_valor_escala(self):
        valores_escala_direta = {'A': 16.71, 'B': 24.98, 'C': 36.56, 'D': 50.65}
        valores_escala_indireta = {'A': 11.02, 'B': 16.71, 'C': 24.98, 'D': 36.46}

        if self.tipo_escala == 'DIRETA':
            return valores_escala_direta.get(self.escala, 0)
        elif self.tipo_escala == 'INDIRETA':
            return valores_escala_indireta.get(self.escala, 0)
        else:
            return 0
        


    def calcular_gratificacao(self):
        
        valor_escala = self.calcular_valor_escala()
        gratificacao = valor_escala * self.total_pontos
        return round(gratificacao, 2)

    def gratificacao_formatada(self):
        gratificacao = self.calcular_gratificacao()

        locale.setlocale(locale.LC_ALL, 'pt_BR.utf-8')
        formatted_gratificacao = locale.currency(gratificacao, grouping=True, symbol=None)
        return formatted_gratificacao
    
    
    nome = models.CharField(max_length=100, null=False, default='', validators=[validar_nome])
    escala = models.CharField(max_length=10, choices=ESCALA_CHOICES, default='blank')
    tipo_escala = models.CharField(max_length=10, choices=TIPO_ESCALA_CHOICES, default='')
    matricula = models.CharField(max_length=10, null=False, default='', validators=[validar_matricula], blank=True)  
    pontualidade = models.CharField(max_length=50, choices=PONTUALIDADE_CHOICES, default='1')
    assiduidade = models.CharField(max_length=10, choices=ASSIDUIDADE_CHOICES, default='1')
    execucao_tarefas = models.CharField(max_length=10, choices=EXECUCAO_TAREFAS_CHOICES, default='1')
    iniciativa = models.CharField(max_length=10, choices=INICIATIVA_CHOICES, default='1')
    atendimento_servicos = models.CharField(max_length=10, choices=ATENDIMENTO_SERVICOS_CHOICES, default='1')
    total_pontos = models.IntegerField(default=0)
    gratificacao_pontos = models.IntegerField(default=0)
    tipo_modalidade = models.CharField(max_length=10,choices=TIPO_MODALIDADE_CHOICES, default='1')
    mes_referencia = models.DateField(default=datetime.date.today)
    setor = models.CharField(max_length=100, null=False, default='', choices=SETOR_CHOICES)
    user = models.ForeignKey(User, on_delete=models.CASCADE, default=1)
    teste_tarefas = models.TextField(blank=True, null=True)



     
class TarefaRealizada(models.Model):
    servidor = models.ForeignKey(Servidor, on_delete=models.CASCADE, null=True)
    diretor_coordenador = models.CharField(max_length=100, null= False)
    tarefas = models.TextField()
    data = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.servidor.nome
    
    



class Usuario(AbstractUser):
    is_superusuario = models.BooleanField(default=False)

    groups = models.ManyToManyField(
        Group,
        verbose_name=_('groups'),
        blank=True,
        help_text=_(
            'The groups this user belongs to. A user will get all permissions '
            'granted to each of their groups.'
        ),
        related_name='usuarios',  
        related_query_name='usuario',
    )
    user_permissions = models.ManyToManyField(
        Permission,
        verbose_name=_('user permissions'),
        blank=True,
        help_text=_('Specific permissions for this user.'),
        related_name='usuarios', 
        related_query_name='usuario',
    )

class Pessoa(models.Model):
    nome = models.CharField(max_length=100, null=False, default='', unique=True)
    pessoa_mat = models.CharField(max_length=20, null=False, default='', blank=True) 

    def __str__(self):
        return self.nome

    

    
    




