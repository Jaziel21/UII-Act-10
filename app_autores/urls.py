from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('autores/<int:autor_id>/', views.ver_autor, name='ver_autor'),
    path('autores/agregar/', views.agregar_autor, name='agregar_autor'),
    path('autores/editar/<int:autor_id>/', views.editar_autor, name='editar_autor'),
    path('autores/eliminar/<int:autor_id>/', views.eliminar_autor, name='eliminar_autor'),
]