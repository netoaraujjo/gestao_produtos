from django.shortcuts import render, redirect
from django.contrib.auth import logout

# Create your views here.
def index(request):
    return render(request, 'core/index.html')


def sair(request):
    logout(request)
    return redirect('core:index')