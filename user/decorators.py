from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import redirect, reverse

def unauthenticated(view_func):
    def wrapper_func(request, *args, **kwargs):
        if request.user.is_authenticated:
            return HttpResponseRedirect(reverse('user:dashboard'))
        else:
            return view_func(request, *args, **kwargs)
    return wrapper_func