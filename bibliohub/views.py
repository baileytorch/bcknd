from django.shortcuts import render
from rest_framework import viewsets
from . import models
from . import serializer

def bienvenida(request):
    return render(request, 'bibliohub/bienvenida.html')

class PaisViewSet(viewsets.ModelViewSet):
            queryset = models.Pais.objects.all()
            serializer_class = serializer.PaisSerializer

class RegionViewSet(viewsets.ModelViewSet):
            queryset = models.Region.objects.all()
            serializer_class = serializer.RegionSerializer

class ProvinciaViewSet(viewsets.ModelViewSet):
            queryset = models.Provincia.objects.all()
            serializer_class = serializer.ProvinciaSerializer

class ComunaViewSet(viewsets.ModelViewSet):
            queryset = models.Comuna.objects.all()
            serializer_class = serializer.ComunaSerializer

class DireccionViewSet(viewsets.ModelViewSet):
            queryset = models.Direccion.objects.all()
            serializer_class = serializer.DireccionSerializer

class BibliotecaViewSet(viewsets.ModelViewSet):
            queryset = models.Biblioteca.objects.all()
            serializer_class = serializer.BibliotecaSerializer

class AutorViewSet(viewsets.ModelViewSet):
            queryset = models.Autor.objects.all()
            serializer_class = serializer.AutorSerializer

class GeneroViewSet(viewsets.ModelViewSet):
            queryset = models.Genero.objects.all()
            serializer_class = serializer.GeneroSerializer

class SubGeneroViewSet(viewsets.ModelViewSet):
            queryset = models.SubGenero.objects.all()
            serializer_class = serializer.SubGeneroSerializer

class EditorialViewSet(viewsets.ModelViewSet):
            queryset = models.Editorial.objects.all()
            serializer_class = serializer.EditorialSerializer

class IdiomaViewSet(viewsets.ModelViewSet):
            queryset = models.Idioma.objects.all()
            serializer_class = serializer.IdiomaSerializer

class EdicionViewSet(viewsets.ModelViewSet):
            queryset = models.Edicion.objects.all()
            serializer_class = serializer.EdicionSerializer

class LibroViewSet(viewsets.ModelViewSet):
            queryset = models.Libro.objects.all()
            serializer_class = serializer.LibroSerializer

class EstadoViewSet(viewsets.ModelViewSet):
            queryset = models.Estado.objects.all()
            serializer_class = serializer.EstadoSerializer

class UbicacionViewSet(viewsets.ModelViewSet):
            queryset = models.Ubicacion.objects.all()
            serializer_class = serializer.UbicacionSerializer

class InventarioViewSet(viewsets.ModelViewSet):
            queryset = models.Inventario.objects.all()
            serializer_class = serializer.InventarioSerializer

class UsuarioViewSet(viewsets.ModelViewSet):
            queryset = models.Usuario.objects.all()
            serializer_class = serializer.UsuarioSerializer

class PrestamoViewSet(viewsets.ModelViewSet):
            queryset = models.Prestamo.objects.all()
            serializer_class = serializer.PrestamoSerializer