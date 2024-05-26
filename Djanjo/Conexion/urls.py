from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('jugadores/', views.jugadores, name='jugadores'),
    path('estadios/', views.estadios, name='estadios'),
    path('estadisticas/', views.estadisticas, name='estadisticas'),
    path('jugadores/agregar/', views.agregar_jugador, name='agregar_jugador'),
    path('estadios/agregar/', views.agregar_estadio, name='agregar_estadio'),
    path('estadisticas/agregar/', views.agregar_estadistica, name='agregar_estadistica'),
]
