from django.shortcuts import render
from django.views.generic import View
from django.contrib.auth import authenticate, logout,login

# Create your views here.


class LoginView(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'user/login.html', {})

    def post(self, request, *args, **kwargs):

        username = request.POST["username"]
        password = request.POST.get("password")
        user = authenticate(username=username, password=password)
        if user:
            login(request, user)
        return render(request, 'user/login.html', {
            "username": username,
            "password": password
        })


class Logout(View):
    def get(self, request, *args, **kwargs):
        logout(request)
        return render(request, 'user/logout.html', {})



class Perfil(View):
    def get(self, request, *args, **kwargs):
        user = request.user
        permisos = user.has_perm("productos.delete_producto")
        return render(request, 'user/perfil.html', {
            "usuario": user,
            "permisos": permisos
        })