# serializers.py
from rest_framework import serializers
from . import models

class PaisSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Pais
        fields = ('nombre','nacionalidad','iso_2','iso_3','habilitado','created_at','updated_at')

class RegionSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Region
        fields = ('codigo','region','habilitado','created_at','updated_at')

class ProvinciaSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Provincia
        fields = ('codigo','provincia','region','habilitado','created_at','updated_at')

class ComunaSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Comuna
        fields = ('codigo','comuna','provincia','habilitado','created_at','updated_at')

class DireccionSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Direccion
        fields = ('comuna','calle','numero','departamento','habilitado','created_at','updated_at')

class BibliotecaSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Biblioteca
        fields = ('nombre','web','correo','telefono','direccion','habilitado','created_at','updated_at')

class AutorSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Autor
        fields = ('nombre','pseudonimo','nacionalidad','fecha_nacimiento','fecha_defuncion','biografia','habilitado','created_at','updated_at')

class GeneroSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Autor
        fields = ('nombre','pseudonimo','nacionalidad','fecha_nacimiento','fecha_defuncion','biografia','habilitado','created_at','updated_at')

class SubGeneroSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.SubGenero
        fields = ('subgenero','descripcion','genero','habilitado','created_at','updated_at')

class EditorialSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Editorial
        fields = ('nombre','web','correo','telefono','direccion','habilitado','created_at','updated_at')

class IdiomaSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Idioma
        fields = ('idioma','habilitado','created_at','updated_at')

class EdicionSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Edicion
        fields = ('fecha_edicion','editorial','idioma','habilitado','created_at','updated_at')

class LibroSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Libro
        fields = ('titulo','paginas','autor','subgenero','edicion','biblioteca','habilitado','created_at','updated_at')

class EstadoSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Estado
        fields = ('estado','descripcion','habilitado','created_at','updated_at')

class UbicacionSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Ubicacion
        fields = ('codigo','ubicacion','descripcion','habilitado','created_at','updated_at')

class InventarioSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Inventario
        fields = ('libro','estado','ubicacion','gtin','habilitado','created_at','updated_at')

class UsuarioSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Usuario
        fields = ('nombre','rut','correo','telefono','nacionalidad','fecha_nacimiento','contrasenia','direccion','biblioteca','habilitado','created_at','updated_at')

class PrestamoSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Prestamo
        fields = ('libro','lector','fecha_prestamo','fecha_devolucion','fecha_retorno')