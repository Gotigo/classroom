from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotAllowed
from .models import Producto
from django.views.generic import ListView, DetailView, UpdateView
# Create your views here.

class ListarView(ListView):
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