from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.models import User 
from django.contrib import messages
from django.contrib.messages import constants
from django.contrib import auth

# Create your views here.
def cadastro(request):

    if request.method == "GET":
        return render (request, 'cadastro.html')
    
    if request.method == "POST":
        username = request.POST.get('username')
        senha = request.POST.get('senha')
        confirmar_senha = request.POST.get('confirmar_senha')
        
        if not senha == confirmar_senha:
            messages.add_message(request, constants.ERROR, 'A senha não são iguais')
            return redirect('cadastro')
        
        if len(senha) < 6:
            messages.add_message(request, constants.ERROR, 'A senha precisa ter pelo menos 6 digitos')
            return redirect('cadastro')
        
        users = User.objects.filter(username=username)
        if users.exists():
            messages.add_message(request, constants.ERROR, 'Usuario já cadastrado')
            return redirect('cadastro')
    
        user = User.objects.create_user(
            username=username,
            password=senha,
        )
        
        return redirect (request, 'logar')
    
def logar(request):
    if request.method == "GET":
        return render(request, 'logar.html')
    if request.method == "POST":
        username = request.POST.get('username')
        senha = request.POST.get('senha')

        user = auth.authenticate(request, username=username, password=senha)
        if user:
            auth.login(request, user)
            return redirect('cadastrar_empresa')
        messages.add_message(request, constants.ERROR, 'Usuario ou senha inválido')
        return redirect ('logar')