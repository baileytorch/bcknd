from django.urls import path,include
from rest_framework import routers
from bibliohub import views

enrutador = routers.DefaultRouter()

enrutador.register(r'paises', views.PaisViewSet)
enrutador.register(r'regiones', views.RegionViewSet)
enrutador.register(r'provincias', views.ProvinciaViewSet)
enrutador.register(r'comunas', views.ComunaViewSet)
enrutador.register(r'direcciones', views.DireccionViewSet)
enrutador.register(r'biblioteca', views.BibliotecaViewSet)
enrutador.register(r'autores', views.AutorViewSet)
enrutador.register(r'generos', views.GeneroViewSet)
enrutador.register(r'subgeneros', views.SubGeneroViewSet)
enrutador.register(r'editoriales', views.EditorialViewSet)
enrutador.register(r'idiomas', views.IdiomaViewSet)
enrutador.register(r'ediciones', views.EdicionViewSet)
enrutador.register(r'libros', views.LibroViewSet)
enrutador.register(r'estados', views.EstadoViewSet)
enrutador.register(r'ubicaciones', views.UbicacionViewSet)
enrutador.register(r'inventarios', views.InventarioViewSet)
enrutador.register(r'usuarios', views.UsuarioViewSet)
enrutador.register(r'prestamos', views.PrestamoViewSet)

urlpatterns = [
    path('', include(enrutador.urls)),
    path('paises/listado_libros', views.LibroListView.as_view(), name='listado_libros'),
    path('paises/detalle_libro/<int:pk>/', views.LibroDetailView.as_view(), name='detalle_libro'),
    path('paises/crear_libro/', views.LibroCreateView.as_view(), name='crear_libro'),
    path('paises/editar_libro/<int:pk>/', views.LibroUpdateView.as_view(), name='editar_libro'),
    path('paises/eliminar_libro/<int:pk>/', views.LibroDeleteView.as_view(), name='eliminar_libro'),
]