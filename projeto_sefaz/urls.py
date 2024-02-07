
from django.urls import path, re_path
from app_cad_serv import views
from django.contrib import admin
from django.contrib.auth import views as auth_views
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi


schema_view = get_schema_view(
   openapi.Info(
      title="API Sugestão de Nomes",
      default_version='v1',
      description="API para ajuda com a sugestão de nomes no sistema de lançamento.",
   ),
   public=True,
   permission_classes=(permissions.AllowAny,),
)

urlpatterns = [
    path('', views.home, name = 'home'),
    path('cadastrar/', views.cadastrar, name = 'cadastrar'),
    path('dados_servidor/', views.dados_servidor, name='dados_servidor'),
    path('cadastrar/cadastro_sucesso.html', views.cadastro_sucesso, name = 'cadastro_sucesso'),
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
    path('swagger<format>/', schema_view.without_ui(cache_timeout=0), name='schema-json'),
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
    path('cadastrar_pessoa/', views.cadastrar_pessoa, name='cadastrar_pessoa'),
    path('api/api-pessoas/', views.api_pessoas, name='api_pessoas'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('excluir-tarefa/<int:tarefa_id>/', views.excluir_tarefa, name='excluir_tarefa'),
]
