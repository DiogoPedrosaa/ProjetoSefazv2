from django.contrib import admin
from .models import Servidor, TarefaRealizada, Pessoa

admin.site.site_header = 'ADMINISTRAÇÃO SEFAZ'
admin.site.site_title = 'ADMIN'
admin.site.index_title = 'ADMIN'


admin.site.register(Servidor)
admin.site.register(TarefaRealizada)
admin.site.register(Pessoa)