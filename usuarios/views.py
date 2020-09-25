from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import auth


# Create your views here.
def cadastro(request):
    if request.method == "POST":
        nome = request.POST["nome"]
        email = request.POST["email"]
        password = request.POST["password"]
        password2 = request.POST["password2"]

        if not nome.strip():
            print("Nome em branco")
            return redirect("cadastro")

        if not email.strip():
            print("Email em branco")
            return redirect("cadastro")

        if password != password2:
            print("Senhas diferentes")
            return redirect("cadastro")

        if User.objects.filter(email=email).exists():
            print("Usuário ja cadastrado")
            return redirect("cadastro")

        user = User.objects.create_user(username=nome, email=email, password=password)
        user.save()
        print("Usuario cadastrado")

        return redirect("login")
    else:
        return render(request, "usuarios/cadastro.html")


def login(request):
    if request.method == "POST":
        email = request.POST["email"]
        password = request.POST["password"]

        if email == "" or password == "":
            return redirect("login")

        if User.objects.filter(email=email).exists():
            nome = User.objects.filter(email=email).values_list("username", flat=True).get()
            user = auth.authenticate(request, password=password, username=nome)
            if user is not None:
                auth.login(request, user)
            else:
                return redirect("login")

        return redirect("dashboard")

    return render(request, "usuarios/login.html")


def logout(request):
    pass


def dashboard(request):
    return render(request, "usuarios/dashboard.html")
