from django.contrib.auth.decorators import user_passes_test
from django.contrib.auth.models import Group
from django.http import HttpResponseForbidden

def group_required(group_name):
    def decorator(view_func):
        def wrapper(request, *args, **kwargs):
            if request.user.groups.filter(name=group_name).exists():
                return view_func(request, *args, **kwargs)
            else:
                
                return HttpResponseForbidden("Você não tem permissão para acessar esta página, entre em contato com o CTIT para duvidas.")
        return wrapper
    return decorator