from django.shortcuts import redirect
from functools import wraps

def tecnico_required(view_func):
    @wraps(view_func)
    def _wrapped_view(request, *args, **kwargs):
        if request.user.rol != 'tecnico':
            return redirect('dashboard')
        return view_func(request, *args, **kwargs)
    return _wrapped_view

def empleado_required(view_func):
    @wraps(view_func)
    def _wrapped_view(request, *args, **kwargs):
        if request.user.rol != 'empleado':
            return redirect('dashboard')
        return view_func(request, *args, **kwargs)
    return _wrapped_view
