
from django.urls import path, include
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from app_cad_serv import urls as app_cad_serv_urls
from django.conf.urls import handler404
from app_cad_serv.urls import custom_404_view


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
    path('', include(app_cad_serv_urls)),
    path('swagger<format>/', schema_view.without_ui(cache_timeout=0), name='schema-json'),
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),

]

handler404 = custom_404_view


