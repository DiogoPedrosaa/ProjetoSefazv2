from datetime import datetime
from django.shortcuts import render, redirect, get_object_or_404
from .models import Servidor, Pessoa, Usuario, TarefaRealizada
from .forms import ServidorForm, TarefaRealizadaForm, SignUpForm, PessoaForm
from django.http import FileResponse
from io import BytesIO
from reportlab.lib import colors
from reportlab.platypus import SimpleDocTemplate, Table, TableStyle
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.lib.pagesizes import letter, landscape
from reportlab.platypus import Paragraph
import locale, logging
from django.contrib.auth import login, authenticate
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.views import LogoutView
from django.http import JsonResponse, HttpResponse
from reportlab.pdfgen import canvas


logger = logging.getLogger(__name__)

@login_required
def home(request):
    user = request.user
    return render(request, 'servidores/home.html', {'user': user})

@login_required
def cadastrar(request):
    setor_value = None
    mes_referencia_value = None

    if request.method == 'POST':
        form = ServidorForm(request.POST)
        if form.is_valid():
            servidor = form.save(commit=False)
            servidor.user = request.user 

            pontos, gratificacao = calcular_pontos(
                form.cleaned_data['pontualidade'],
                form.cleaned_data['assiduidade'],
                form.cleaned_data['execucao_tarefas'],
                form.cleaned_data['iniciativa'],
                form.cleaned_data['atendimento_servicos']
            )
            servidor.total_pontos = pontos  
            servidor.gratificacao_pontos = gratificacao
            
            servidor.save()
            messages.success(request, 'Lançamento Realizado com Sucesso!')

            setor_value = form.cleaned_data['setor']
            mes_referencia_value = form.cleaned_data['mes_referencia']
            

            setor_value = str(setor_value)
            mes_referencia_value = str(mes_referencia_value)


            form.cleaned_data['Nome'] = ''
            form.cleaned_data['Matricula'] = ''


            messages.success(request, 'Formulário enviado com sucesso!')

    else:
        form = ServidorForm()

    return render(request, 'servidores/cadastrar.html', {'form': form, 'setor_value': setor_value, 'mes_referencia_value': mes_referencia_value})



def dados_servidor(request):
    allowed_groups = {'CTIT', 'RH', 'CAF', 'Diretoria ADM', 'ASCOM', 'Orçamento', 'Gab Orçamento',
                      'DTM', 'Subsec Rec Mun', 'Diret Rec Mun', 'Coord Geral da rec', 'Diret Atend Contri',
                      'Arrecadação', 'ITBI', 'Digitalização CTIT', 'Cont e convênios', 'Superintendência',
                      'UGOCC', 'Inteligência fiscal', 'Auto de Infração', 'Catraca', 'Cadastro Mercantil',
                      'Triagem', 'Cadastro Imobiliário', 'Geoprocessamento', 'Apoio Atendimento'}

    user_group = None
    if request.user.groups.exists():
        user_group = request.user.groups.first().name

    if user_group and user_group in allowed_groups:
        servidores = Servidor.objects.filter(setor=user_group)
    else:
        servidores = Servidor.objects.filter(user=request.user)

    return render(request, 'servidores/dados_servidor.html', {'servidores': servidores, 'user_group': user_group})

@login_required
def cadastro_sucesso(request):
    return render(request, 'servidores/cadastro_sucesso.html')




def calcular_pontos(pontualidade, assiduidade, execucao_tarefas, iniciativa, atendimento_servicos):
    criterios = {
        "10": 10,
        "08": 8,
        "04": 4,
        "02": 2,
        "30": 30,
        "20": 20,
        "15": 15,
        "10": 10,
        "05": 5
    }

    pontos = criterios.get(pontualidade, 0) + \
             criterios.get(assiduidade, 0) + \
             criterios.get(execucao_tarefas, 0) + \
             criterios.get(iniciativa, 0) + \
             criterios.get(atendimento_servicos, 0)

    gratificacao = pontos * 50

    return pontos, gratificacao


@login_required
def relatorio_servidor(request, servidor_id):
    
    servidor = Servidor.objects.get(pk=servidor_id)
    print(servidor)  
    return render(request, 'servidores/relatorio_servidor.html', {'servidor': servidor})
    



def calcular_pontos_pontualidade(pontualidade):

    pontualidade = pontualidade.lower()

    if pontualidade == "sem justificativa":
        return 10
    elif pontualidade == "2 justificativas":
        return 8
    elif pontualidade == "3 justificativas":
        return 4
    elif pontualidade == "5 justificativas":
        return 2
    else:
        return 0
    



def calcular_pontos_assiduidade(assiduidade):

    assiduidade = assiduidade.lower()

    if assiduidade == "sem faltas":
        return 10
    elif assiduidade == "1 falta":
        return 8
    elif assiduidade == "2 faltas":
        return 4
    elif assiduidade == "3 faltas":
        return 2
    else:
        return 0
    


def calcular_pontos_exec_tarefas(execucao_tarefas):

    execucao_tarefas = execucao_tarefas.lower()

    if execucao_tarefas == "excelente":
        return 30
    elif execucao_tarefas == "otimo":
        return 20
    elif execucao_tarefas == "bom":
        return 15
    elif execucao_tarefas == "regular":
        return 10
    else:
        return 0
    

def calcular_pontos_iniciativa(iniciativa):

    iniciativa = iniciativa.lower()

    if iniciativa == "excelente":
        return 20
    elif iniciativa == "otimo":
        return 15
    elif iniciativa == "bom":
        return 10
    elif iniciativa == "regular":
        return 5
    else:
        return 0
    
    


def calcular_pontos_atendimento_servicos(atendimento_servicos):

    atendimento_servicos = atendimento_servicos.lower()

    if atendimento_servicos == "excelente":
        return 30
    elif atendimento_servicos == "otimo":
        return 20
    elif atendimento_servicos == "bom":
        return 15
    elif atendimento_servicos == "regular":
        return 10
    else:
        return 0
    
    
@login_required
def relatorio_servidor(request, servidor_id):
    servidor = Servidor.objects.get(pk=servidor_id)
    return render(request, 'servidores/relatorio_servidor.html', {'servidor': servidor})



    
@login_required
def preencher_tarefas(request, servidor_id):
    servidor = Servidor.objects.get(pk=servidor_id)

    if request.method == 'POST':
        form = TarefaRealizadaForm(request.POST)
        if form.is_valid():
            tarefa = form.save(commit=False)
            tarefa.servidor = servidor  
            tarefa.diretor_coordenador = request.user.get_full_name()
            tarefa.save()
            messages.success(request, 'Tarefas Enviadas com Sucesso!')
            return redirect('preencher_tarefas', servidor_id=servidor_id)

    else:
        form = TarefaRealizadaForm(initial={'colaborador': servidor.nome, 'diretor_coordenador': request.user.get_full_name()})

    tarefas_servidor = TarefaRealizada.objects.filter(servidor=servidor, data=servidor.mes_referencia)

    return render(request, 'servidores/preencher_tarefas.html', {'form': form, 'servidor': servidor, 'servidor_id': servidor_id, 'tarefas_servidor': tarefas_servidor})


@login_required
def visualizar_tarefas_servidor(request, servidor_id):
    servidor = get_object_or_404(Servidor, pk=servidor_id)
    tarefas = TarefaRealizada.objects.filter(servidor=servidor)
    tarefas_servidor = TarefaRealizada.objects.filter(data=servidor.mes_referencia)
    return render(request, 'servidores/visualizar_tarefas_servidor.html', {'servidor': servidor, 'tarefas': tarefas, 'matricula': servidor.matricula, 'tarefas_servidor': tarefas_servidor})


@login_required
def generate_pdf(request):
   
    allowed_groups = {'CTIT', 'RH', 'CAF', 'Diretoria ADM', 'ASCOM', 'Orçamento', 'Gab Orçamento',
                      'DTM', 'Subsec Rec Mun', 'Diret Rec Mun', 'Coord Geral da rec', 'Diret Atend Contri',
                      'Arrecadação', 'ITBI', 'Digitalização CTIT', 'Cont e convênios', 'Superintendência',
                      'UGOCC', 'Inteligência fiscal', 'Auto de Infração', 'Catraca', 'Cadastro Mercantil',
                      'Triagem', 'Cadastro Imobiliário', 'Geoprocessamento', 'Apoio Atendimento'}

    user_group = None
    if request.user.groups.exists():
        user_group = request.user.groups.first().name

    if user_group and user_group in allowed_groups:
        servidores = Servidor.objects.filter(setor=user_group)
    else:
        servidores = Servidor.objects.filter(user=request.user)
        

    buffer = BytesIO()

    
    custom_page_size = landscape(letter)

    doc = SimpleDocTemplate(buffer, pagesize=custom_page_size, rightMargin=50, leftMargin=20)
    elements = []

    secretaria_name = "SECRETARIA MUNICIPAL DA ECONOMIA - SEFAZ"
    secretaria_style = getSampleStyleSheet()['Title']
    secretaria_paragraph = Paragraph(secretaria_name, style=secretaria_style)

    elements.append(secretaria_paragraph)


    col_widths = [200, 50, 50, 70, 70, 80, 70, 90, 60, 60, 70]


    data = []
    data.append(["Nome do Servidor", "Escala", "Mat.", "Pontualidade", "Assiduidade", "Exec. Tarefas", "Iniciativa", "At. Serviços", "Total Pontos",])

    for servidor in servidores:
        data.append([servidor.nome, servidor.escala, servidor.matricula, servidor.pontualidade, servidor.assiduidade, servidor.execucao_tarefas, servidor.iniciativa, servidor.atendimento_servicos, servidor.total_pontos])

    
    table = Table(data, colWidths=col_widths)


    style = TableStyle([
        ('BACKGROUND', (0, 0), (-1, 0), colors.grey),
        ('TEXTCOLOR', (0, 0), (-1, 0), colors.whitesmoke),
        ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
        ('FONTNAME', (0, 0), (-1, 0), 'Helvetica'),
        ('BOTTOMPADDING', (0, 0), (-1, 0), 12),
        ('BACKGROUND', (0, 1), (-1, -1), colors.beige),
        ('GRID', (0, 0), (-1, -1), 1, colors.black),
    ])



  
    style.add('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold')
    style.add('ALIGN', (0, 0), (-1, -1), 'CENTER')
    style.add('TEXTCOLOR', (0, 1), (-1, -1), colors.black)
    style.add('BACKGROUND', (0, 1), (-1, -1), colors.white)
    style.add('GRID', (0, 0), (-1, -1), 1, colors.black)
    style.add('FONTSIZE', (0, 1), (-1, -1), 8)  
    style.add('BOTTOMPADDING', (0, 1), (-1, -1), 3) 


    style.add('LEADING', (0, 1), (-1, -1), 10)

    
    table.setStyle(style)

    
    elements.append(table)
    doc.build(elements)

    
    buffer.seek(0)


    response = FileResponse(buffer, as_attachment=True, filename='Dados_Servidores.pdf')



    return response





@login_required
def generate_pdf_geral(request):
 
    allowed_groups = {'CTIT', 'RH', 'CAF', 'Diretoria ADM', 'ASCOM', 'Orçamento', 'Gab Orçamento',
                      'DTM', 'Subsec Rec Mun', 'Diret Rec Mun', 'Coord Geral da rec', 'Diret Atend Contri',
                      'Arrecadação', 'ITBI', 'Digitalização CTIT', 'Cont e convênios', 'Superintendência',
                      'UGOCC', 'Inteligência fiscal', 'Auto de Infração', 'Catraca', 'Cadastro Mercantil',
                      'Triagem', 'Cadastro Imobiliário', 'Geoprocessamento', 'Apoio Atendimento'}

    user_group = None
    if request.user.groups.exists():
        user_group = request.user.groups.first().name

    if user_group and user_group in allowed_groups:
        servidores = Servidor.objects.filter(setor=user_group)
    else:
        servidores = Servidor.objects.filter(user=request.user)
        
    buffer = BytesIO()

    custom_page_size = landscape(letter)
    doc = SimpleDocTemplate(buffer, pagesize=custom_page_size, rightMargin=50, leftMargin=20)
    elements = []

    info_table_data = [
        ["PREFEITURA MUNICIPAL DE MACEIÓ"],
        ["SECRETARIA MUNICIPAL DA FAZENDA"],
        ["SETOR: COORD, GERAL DE ATENDIMENTO AO CONTRIBUINTE"],
        ["COORDENADOR:" f"{request.user.first_name} {request.user.last_name}"],
        ["MÊS REFERÊNCIA - teste"]
    ]
    info_table = Table(info_table_data, colWidths=[200])

    info_table.setStyle(TableStyle([
        ('LEFTPADDING', (0, 0), (-1, -1), -265),
    ]))

    elements.append(info_table)

    secretaria_name = "SECRETARIA MUNICIPAL DA ECONOMIA - SEFAZ"
    secretaria_style = getSampleStyleSheet()['Title']
    secretaria_paragraph = Paragraph(secretaria_name, style=secretaria_style)
    elements.append(secretaria_paragraph)

    col_widths = [170, 50, 70, 70, 70, 60, 70, 90, 60]

    data = [
        ["Nome do Servidor", "Mat.", "Gratificação", "Administ", "Observação", "Escala", "V.P ATUAL", "Total Pontos", "Nº SERV"]
    ]

    for servidor in servidores:
        data.append([
            servidor.nome,
            servidor.matricula,
            servidor.gratificacao_formatada(),  
            servidor.tipo_escala,
            servidor.tipo_modalidade,
            servidor.escala,
            servidor.calcular_valor_escala(), 
            servidor.total_pontos,
            servidor.id
        ])

    table = Table(data, colWidths=col_widths)

    style = TableStyle([
        ('BACKGROUND', (0, 0), (-1, 0), colors.grey),
        ('TEXTCOLOR', (0, 0), (-1, 0), colors.whitesmoke),
        ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
        ('FONTNAME', (0, 0), (-1, 0), 'Helvetica'),
        ('BOTTOMPADDING', (0, 0), (-1, 0), 12),
        ('BACKGROUND', (0, 1), (-1, -1), colors.beige),
        ('GRID', (0, 0), (-1, -1), 1, colors.black),
    ])

    style.add('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold')
    style.add('ALIGN', (0, 0), (-1, -1), 'CENTER')
    style.add('TEXTCOLOR', (0, 1), (-1, -1), colors.black)
    style.add('BACKGROUND', (0, 1), (-1, -1), colors.white)
    style.add('GRID', (0, 0), (-1, -1), 1, colors.black)
    style.add('FONTSIZE', (0, 1), (-1, -1), 8)
    style.add('BOTTOMPADDING', (0, 1), (-1, -1), 3)
    style.add('LEADING', (0, 1), (-1, -1), 10)

    table.setStyle(style)
    elements.append(table)
    doc.build(elements)

    buffer.seek(0)

    response = FileResponse(buffer, as_attachment=True, filename='Dados_Servidores_Geral.pdf')
    return response


def formatar_mes_referencia():
    
    locale.setlocale(locale.LC_TIME, 'pt_BR.UTF-8')
    
    mes_referencia = datetime.now().strftime('%B %Y')
    
    mes, ano = mes_referencia.split()
    
    mes = mes.capitalize()
    
    return f"{mes} de {ano}"


@login_required
def excluir_servidor(request, servidor_id):
    servidor = get_object_or_404(Servidor, pk=servidor_id)
    servidor.delete()
    return redirect('dados_servidor')



@login_required
def dados_servidor_geral(request):
    allowed_groups = {'CTIT', 'RH', 'CAF', 'Diretoria ADM', 'ASCOM', 'Orçamento', 'Gab Orçamento',
                      'DTM', 'Subsec Rec Mun', 'Diret Rec Mun', 'Coord Geral da rec', 'Diret Atend Contri',
                      'Arrecadação', 'ITBI', 'Digitalização CTIT', 'Cont e convênios', 'Superintendência',
                      'UGOCC', 'Inteligência fiscal', 'Auto de Infração', 'Catraca', 'Cadastro Mercantil',
                      'Triagem', 'Cadastro Imobiliário', 'Geoprocessamento', 'Apoio Atendimento'}

    user_group = None
    if request.user.groups.exists():
        user_group = request.user.groups.first().name

    if user_group and user_group in allowed_groups:
        servidores = Servidor.objects.filter(setor=user_group)
    else:
        servidores = Servidor.objects.filter(user=request.user)

    return render(request, 'servidores/dados_servidor_geral.html', {'servidores': servidores, 'user_group': user_group})



def login_page(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            
            
            logger.debug(f'Username: {username}')
            logger.debug(f'Password: {password}')

            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('home')
            else:
                messages.error(request, 'Credenciais inválidas. Por favor, tente novamente.')
        else:
            
            logger.error(f'Formulário inválido: {form.errors}')
    else:
        form = AuthenticationForm()

    return render(request, 'servidores/login.html', {'form': form})




@login_required
def cadastrar_usuario(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            if User.objects.filter(username=username).exists():
                messages.error(request, 'Nome de usuário já em uso. Escolha outro.')
                return render(request, 'servidores/cadastrar_usuario.html', {'form': form})

            user = form.save()
            return redirect('cadastro_sucesso')
    else:
        form = SignUpForm()

    return render(request, 'servidores/cadastrar_usuario.html', {'form': form})



class CustomLogoutView(LogoutView):
    def dispatch(self, request, *args, **kwargs):
        response = super().dispatch(request, *args, **kwargs)
        
        return redirect('home') 


    
def cadastrar_pessoa(request):
    if request.method == 'POST':
        form = PessoaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('cadastrar_pessoa') 
    else:
        form = PessoaForm()

    return render(request, 'servidores/cadastrar_pessoa.html', {'form': form})


def api_pessoas(request):
    pessoas = Pessoa.objects.values('nome', 'pessoa_mat')
    print(pessoas)  
    return JsonResponse(list(pessoas), safe=False)


def dashboard(request):
    total_pessoas = Pessoa.objects.count()
    total_servidores = Servidor.objects.count()
    total_tarefas = TarefaRealizada.objects.count()
    total_usuarios = Usuario.objects.count()
    
    num_servidores_ti = Servidor.objects.filter(setor='CTIT').count()
    num_servidores_rh = Servidor.objects.filter(setor='RH').count()

    context = {
        'total_pessoas': total_pessoas,
        'total_servidores': total_servidores,
        'total_tarefas': total_tarefas,
        'num_servidores_ti': num_servidores_ti,
        'num_servidores_rh': num_servidores_rh,
        'total_usuarios': total_usuarios,
    }

    return render(request, 'servidores/dashboard.html', context)



@login_required
def excluir_tarefa(request, tarefa_id):
    tarefa = get_object_or_404(TarefaRealizada, pk=tarefa_id)
    try:
        tarefa.delete()
    except Exception as e:
        messages.error(request, f'Ocorreu um erro ao excluir a tarefa: {str(e)}')

    return redirect('visualizar_tarefas_servidor', servidor_id=tarefa.servidor.id)



@login_required
def generate_pdf_setores(request):
   
    servidores = Servidor.objects.all()
    

    buffer = BytesIO()

    
    custom_page_size = landscape(letter)

    doc = SimpleDocTemplate(buffer, pagesize=custom_page_size, rightMargin=50, leftMargin=20)
    elements = []

    secretaria_name = "SECRETARIA MUNICIPAL DA ECONOMIA - SEFAZ"
    secretaria_style = getSampleStyleSheet()['Title']
    secretaria_paragraph = Paragraph(secretaria_name, style=secretaria_style)

    elements.append(secretaria_paragraph)


    col_widths = [200, 50, 50, 70, 70, 80, 70, 90, 60, 60, 70]


    data = []
    data.append(["Nome do Servidor", "Escala", "Mat.", "Pontualidade", "Assiduidade", "Exec. Tarefas", "Iniciativa", "At. Serviços", "Total Pontos",])

    for servidor in servidores:
        data.append([servidor.nome, servidor.escala, servidor.matricula, servidor.pontualidade, servidor.assiduidade, servidor.execucao_tarefas, servidor.iniciativa, servidor.atendimento_servicos, servidor.total_pontos])

    
    table = Table(data, colWidths=col_widths)


    style = TableStyle([
        ('BACKGROUND', (0, 0), (-1, 0), colors.grey),
        ('TEXTCOLOR', (0, 0), (-1, 0), colors.whitesmoke),
        ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
        ('FONTNAME', (0, 0), (-1, 0), 'Helvetica'),
        ('BOTTOMPADDING', (0, 0), (-1, 0), 12),
        ('BACKGROUND', (0, 1), (-1, -1), colors.beige),
        ('GRID', (0, 0), (-1, -1), 1, colors.black),
    ])



  
    style.add('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold')
    style.add('ALIGN', (0, 0), (-1, -1), 'CENTER')
    style.add('TEXTCOLOR', (0, 1), (-1, -1), colors.black)
    style.add('BACKGROUND', (0, 1), (-1, -1), colors.white)
    style.add('GRID', (0, 0), (-1, -1), 1, colors.black)
    style.add('FONTSIZE', (0, 1), (-1, -1), 8)  
    style.add('BOTTOMPADDING', (0, 1), (-1, -1), 3) 


    style.add('LEADING', (0, 1), (-1, -1), 10)

    
    table.setStyle(style)

    
    elements.append(table)
    doc.build(elements)

    
    buffer.seek(0)


    response = FileResponse(buffer, as_attachment=True, filename='Dados_Servidores_Setores.pdf')



    return response




@login_required
def generate_pdf_setores_geral(request):
 
    servidores = Servidor.objects.all()
    
    buffer = BytesIO()

    custom_page_size = landscape(letter)
    doc = SimpleDocTemplate(buffer, pagesize=custom_page_size, rightMargin=50, leftMargin=20)
    elements = []

    info_table_data = [
        ["PREFEITURA MUNICIPAL DE MACEIÓ"],
        ["SECRETARIA MUNICIPAL DA FAZENDA"],
        ["SETOR: COORD, GERAL DE ATENDIMENTO AO CONTRIBUINTE"],
        ["COORDENADOR:" f"{request.user.first_name} {request.user.last_name}"],
        ["MÊS REFERÊNCIA - teste"]
    ]
    info_table = Table(info_table_data, colWidths=[200])

    info_table.setStyle(TableStyle([
        ('LEFTPADDING', (0, 0), (-1, -1), -265),
    ]))

    elements.append(info_table)

    secretaria_name = "SECRETARIA MUNICIPAL DA ECONOMIA - SEFAZ"
    secretaria_style = getSampleStyleSheet()['Title']
    secretaria_paragraph = Paragraph(secretaria_name, style=secretaria_style)
    elements.append(secretaria_paragraph)

    col_widths = [170, 50, 70, 70, 70, 60, 70, 90, 60]

    data = [
        ["Nome do Servidor", "Mat.", "Gratificação", "Administ", "Observação", "Escala", "V.P ATUAL", "Total Pontos", "Nº SERV"]
    ]

    for servidor in servidores:
        data.append([
            servidor.nome,
            servidor.matricula,
            servidor.gratificacao_formatada(),  
            servidor.tipo_escala,
            servidor.tipo_modalidade,
            servidor.escala,
            servidor.calcular_valor_escala(), 
            servidor.total_pontos,
            servidor.id
        ])

    table = Table(data, colWidths=col_widths)

    style = TableStyle([
        ('BACKGROUND', (0, 0), (-1, 0), colors.grey),
        ('TEXTCOLOR', (0, 0), (-1, 0), colors.whitesmoke),
        ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
        ('FONTNAME', (0, 0), (-1, 0), 'Helvetica'),
        ('BOTTOMPADDING', (0, 0), (-1, 0), 12),
        ('BACKGROUND', (0, 1), (-1, -1), colors.beige),
        ('GRID', (0, 0), (-1, -1), 1, colors.black),
    ])

    style.add('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold')
    style.add('ALIGN', (0, 0), (-1, -1), 'CENTER')
    style.add('TEXTCOLOR', (0, 1), (-1, -1), colors.black)
    style.add('BACKGROUND', (0, 1), (-1, -1), colors.white)
    style.add('GRID', (0, 0), (-1, -1), 1, colors.black)
    style.add('FONTSIZE', (0, 1), (-1, -1), 8)
    style.add('BOTTOMPADDING', (0, 1), (-1, -1), 3)
    style.add('LEADING', (0, 1), (-1, -1), 10)

    table.setStyle(style)
    elements.append(table)
    doc.build(elements)

    buffer.seek(0)

    response = FileResponse(buffer, as_attachment=True, filename='Dados_Servidores_Geral_Setores.pdf')
    return response




def generate_pdf_servidor(request, servidor_id):
        servidor = get_object_or_404(Servidor, id=servidor_id)
        
        data_referencia = servidor.mes_referencia
        
        data_formatada = data_referencia.strftime("%d/%m/%Y")

        buffer = BytesIO()
        custom_page_size = landscape(letter)
        doc = SimpleDocTemplate(buffer, pagesize=custom_page_size, rightMargin=10, leftMargin=10)
        elements = []

        secretaria_name = "SECRETARIA MUNICIPAL DA ECONOMIA - SEFAZ"
        secretaria_style = getSampleStyleSheet()['Title']
        secretaria_paragraph = Paragraph(secretaria_name, style=secretaria_style)
        elements.append(secretaria_paragraph)

        col_widths = [180, 50, 40, 40, 70, 70, 70, 50, 60, 70, 80]

        data = [
            ["Nome do Servidor", "Setor", "Escala", "Mat.", "Pontualidade", "Assiduidade", "Exec. Tarefas", "Iniciativa", "At. Serviços", "Total Pontos", "Data Referente"]
        ]

        data.append([
            servidor.nome,
            servidor.setor,
            servidor.escala,  
            servidor.matricula,
            servidor.pontualidade,
            servidor.assiduidade,
            servidor.execucao_tarefas, 
            servidor.iniciativa,
            servidor.atendimento_servicos,
            servidor.total_pontos,
            data_formatada
        ])

        table = Table(data, colWidths=col_widths)  

        style = TableStyle([
        ('BACKGROUND', (0, 0), (-1, 0), colors.grey),
        ('TEXTCOLOR', (0, 0), (-1, 0), colors.whitesmoke),
        ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
        ('FONTNAME', (0, 0), (-1, 0), 'Helvetica'),
        ('BOTTOMPADDING', (0, 0), (-1, 0), 12),
        ('BACKGROUND', (0, 1), (-1, -1), colors.beige),
        ('GRID', (0, 0), (-1, -1), 1, colors.black),
    ])

        style.add('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold')
        style.add('ALIGN', (0, 0), (-1, -1), 'CENTER')
        style.add('TEXTCOLOR', (0, 1), (-1, -1), colors.black)
        style.add('BACKGROUND', (0, 1), (-1, -1), colors.white)
        style.add('GRID', (0, 0), (-1, -1), 1, colors.black)
        style.add('FONTSIZE', (0, 1), (-1, -1), 8)  
        style.add('BOTTOMPADDING', (0, 1), (-1, -1), 3) 
        
        style.add('LEADING', (0, 1), (-1, -1), 10)

        table.setStyle(style)
        
        elements.append(table)

        doc.build(elements)
        buffer.seek(0)

        response = HttpResponse(content_type='application/pdf')
        response['Content-Disposition'] = f'attachment; filename="Servidor_{servidor.id}_dados.pdf"'
        response.write(buffer.getvalue())
        return response
    
    


