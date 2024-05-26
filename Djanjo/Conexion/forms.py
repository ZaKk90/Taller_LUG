from django import forms
from .models import Jugador, Estadio, Estadistica

class JugadorForm(forms.ModelForm):
    class Meta:
        model = Jugador
        fields = ['nombre', 'apellido', 'nacionalidad', 'posicion', 'numero_camiseta']

class EstadioForm(forms.ModelForm):
    class Meta:
        model = Estadio
        fields = ['nombre', 'ciudad', 'capacidad', 'equipo_id']

class EstadisticaForm(forms.ModelForm):
    class Meta:
        model = Estadistica
        fields = ['equipo', 'partidos_jugados', 'partidos_ganados', 'partidos_perdidos', 'partidos_empatados', 'goles', 'asistencias']
