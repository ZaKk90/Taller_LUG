from django.shortcuts import render, redirect
from .models import Jugador, Estadio, Estadistica
from .forms import JugadorForm, EstadioForm, EstadisticaForm


def home(request):
    return render(request, 'Conexion/home.html')


def jugadores(request):
    jugadores = Jugador.objects.all()
    return render(request, 'Conexion/jugadores.html', {'jugadores': jugadores})


def estadios(request):
    estadios = Estadio.objects.all()
    return render(request, 'Conexion/estadios.html', {'estadios': estadios})


def estadisticas(request):
    estadisticas = Estadistica.objects.all()
    return render(request, 'Conexion/estadisticas.html', {'estadisticas': estadisticas})


def agregar_jugador(request):
    if request.method == 'POST':
        form = JugadorForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('jugadores')
    else:
        form = JugadorForm()
    return render(request, 'Conexion/agregar_jugador.html', {'form': form})


def agregar_estadio(request):
    if request.method == 'POST':
        form = EstadioForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('estadios')  
    else:
        form = EstadioForm()
    return render(request, 'Conexion/agregar_estadio.html', {'form': form})


def agregar_estadistica(request):
    if request.method == 'POST':
        form = EstadisticaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('estadisticas')
    else:
        form = EstadisticaForm()
    return render(request, 'Conexion/agregar_estadistica.html', {'form': form})
