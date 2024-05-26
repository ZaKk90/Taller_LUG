from django.db import models

class Estadio(models.Model):
    nombre = models.CharField(max_length=20)
    ciudad = models.CharField(max_length=20)
    capacidad = models.PositiveIntegerField()
    equipo_id = models.PositiveIntegerField()

class Estadistica(models.Model):
    equipo = models.CharField(max_length=40)
    partidos_jugados = models.PositiveIntegerField()
    partidos_ganados = models.PositiveIntegerField()
    partidos_perdidos = models.PositiveIntegerField()
    partidos_empatados = models.PositiveIntegerField()
    goles = models.PositiveIntegerField()
    asistencias = models.PositiveIntegerField()

class Jugador(models.Model):
    nombre = models.CharField(max_length=20)
    apellido = models.CharField(max_length=20)
    nacionalidad = models.CharField(max_length=20)
    posicion = models.CharField(max_length=20)
    numero_camiseta = models.PositiveIntegerField()
