from django.urls import path
from . import views
from django.contrib import admin
from django.contrib.auth import views as auth_views
from django.conf.urls import handler404
from django.shortcuts import render

urlpatterns = [
    path('', views.home, name='home'),
    path('cadastrar/', views.cadastrar, name='cadastrar'),
    path('dados_servidor/', views.dados_servidor, name='dados_servidor'),
    path('cadastrar/cadastro_sucesso.html', views.cadastro_sucesso, name='cadastro_sucesso'),
    path('relatorio_servidor/<int:servidor_id>/', views.relatorio_servidor, name='relatorio_servidor'),
    path('preencher-tarefas/<int:servidor_id>/', views.preencher_tarefas, name='preencher_tarefas'),
    path('visualizar-tarefas/<int:servidor_id>/', views.visualizar_tarefas_servidor, name='visualizar_tarefas_servidor'),
    path('download_pdf/', views.generate_pdf, name='download_pdf'),
    path('excluir_servidor/<int:servidor_id>/', views.excluir_servidor, name='excluir_servidor'),
    path('dados_servidor_geral/', views.dados_servidor_geral, name='dados_servidor_geral'),
    path('login/', views.login_page, name='login'),
    path('download_pdf_geral/', views.generate_pdf_geral, name='download_pdf_geral'),
    path('admin/', admin.site.urls, name='admin'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('cadastrar_pessoa/', views.cadastrar_pessoa, name='cadastrar_pessoa'),
    path('api/api-pessoas/', views.api_pessoas, name='api_pessoas'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('excluir-tarefa/<int:servidor_id>/', views.excluir_tarefa, name='excluir_tarefa'),
    path('download_pdf_setores/', views.generate_pdf_setores, name='download_pdf_setores'),
    path('download_pdf_setores_geral/', views.generate_pdf_setores_geral, name='download_pdf_setores_geral'),
    path('download_pdf_servidor/<int:servidor_id>/', views.generate_pdf_servidor, name='download_pdf_servidor'),
    path('repositorio/', views.index_repositorio, name='index-repositorio'),
    path('repositorio-formularios/', views.formularios_repositorio, name='formularios-repositorio'),
    path('repositorio-instaladores/', views.instaladores_repositorio, name='instaladores-repositorio'),
    path('repositorio-fluxogramas/', views.fluxogramas_repositorio, name='fluxogramas-repositorio'),
    path('repositorio-documentos-admnistrativos/', views.documentosadmin_repositorio, name='documentosadmin-repositorio'),
    path('repositorio-ramais/', views.ramais_repositorio, name='ramais-repositorio'),
    path('index/', views.homepage, name='index-site'),
]

def custom_404_view(request, exception):
    return render(request, 'servidores/404.html', status=404)    
