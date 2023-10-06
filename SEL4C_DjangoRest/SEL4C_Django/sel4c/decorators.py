from functools import wraps
from django.shortcuts import redirect
from django.contrib import messages

def staff_required(view_func):
    @wraps(view_func)
    def _wrapped_view(request, *args, **kwargs):
        if request.user.is_authenticated and request.user.is_staff:
            return view_func(request, *args, **kwargs)
        else:
            messages.success(request, ("Necesita Iniciar Sesión"))
            return redirect('login')
    return _wrapped_view

def superuser_required(view_func):
    @wraps(view_func)
    def _wrapped_view(request, *args, **kwargs):
        if request.user.is_authenticated and request.user.is_superuser:
            return view_func(request, *args, **kwargs)
        else:
            messages.success(request, ("Necesita Iniciar Sesión como un superusuario"))
            return redirect('login')
    return _wrapped_view
