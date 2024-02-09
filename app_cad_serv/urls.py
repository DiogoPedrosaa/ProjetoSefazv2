from django.urls import path
from . import views
from django.contrib import admin
from django.contrib.auth import views as auth_views

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
    path('excluir-tarefa/<int:tarefa_id>/', views.excluir_tarefa, name='excluir_tarefa'),
]