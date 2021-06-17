import re
from django.db.models import manager
from django.shortcuts import render
from django.urls import reverse
from django.http import HttpResponse, HttpResponseNotAllowed, response
from .models import Producto
from django.contrib.auth.mixins import PermissionRequiredMixin
from django.views.generic import ListView, DetailView, UpdateView, View
from django.contrib.auth.decorators import login_required, permission_required
# Create your views here.

class ListarView(ListView):
    permission_required='productos.view_producto'
    model = Producto
    template_name = 'productos/listar.html'

class ProductoDetailView(DetailView):
    context_object_name = 'producto'
    queryset = Producto.objects.all()
    template_name = 'productos/editar.html'

class ProductoUpdateView(UpdateView):
    model = Producto
    fields = ['nombre', 'sku']
    template_name = 'productos/editar.html'
    success_url = '/'


class IndexView(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'productos/index.html', {})

@login_required
@permission_required('productos.add_producto', raise_exception=True)
def crear(request):

    if request.method == "GET":
        return render(request, "productos/crear.html", {})
    elif request.method == "POST":
        request_post = request.POST

        producto = Producto()
        producto.nombre = request_post["nombre"]
        producto.sku = request_post["sku"]

        producto.save()

        return render(request, 'productos/crear.html', {
            "post": producto
        })
    else:
        return HttpResponseNotAllowed(["POST","GET"])

def index(request):
    titulo = ["askdcjsdvkdfjkhf","segundo titulo", "tercer titulo"]
    es_verdadero = True
    return render(request, 'productos/index.html', {
        "titulos": titulo,
        "es_verdadero": es_verdadero,
        "titulo_pagina": "TITULO DESDE CONTEXTO"
    })

from django.views.decorators.csrf import csrf_exempt
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .serializers import ProductoSerializer

@csrf_exempt
@api_view(["GET", "POST"])
def lista_productos(request):
    if request.method == 'GET':
        prodcuto = Producto.objects.all()
        serializer = ProductoSerializer(prodcuto, many=True)
        return Response(serializer.data)
