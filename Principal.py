#! /usr/bin/env python
# -*- coding: utf-8 -*-
import pilasengine
import time

pilas = pilasengine.iniciar()

mapa = pilas.actores.MapaTiled('plataformas.tmx', densidad=0,
            restitucion=0, friccion=0, amortiguacion=0)


class SaltarUnaVez(pilas.comportamientos.Comportamiento):

    def iniciar(self, receptor, velocidad_inicial=10, cuando_termina=None):
        super(SaltarUnaVez, self).iniciar(receptor)
        self.velocidad_inicial = velocidad_inicial
        self.cuando_termina = cuando_termina
        self.sonido_saltar = self.pilas.sonidos.cargar("audio/saltar.wav")
        self.suelo = int(self.receptor.y)
        self.velocidad = self.velocidad_inicial
        self.sonido_saltar.reproducir()
        self.velocidad_aux = self.velocidad_inicial
        self.receptor.saltando = False

    def actualizar(self):
        self.receptor.y += self.velocidad
        self.velocidad -= 0.3

        if self.receptor.y <= self.suelo:
            self.velocidad_aux /= 3.5
            self.velocidad = self.velocidad_aux

            if self.velocidad_aux <= 1:
                # Si toca el suelo
                self.receptor.y = self.suelo
                if self.cuando_termina:
                    self.cuando_termina()
                self.receptor.saltando = False
                return True
                     
#Esta clase es la del enemigo
class Enemigo(pilasengine.actores.Actor):
    def iniciar(self):
        self.imagen ="Dios.jpg"
        self.direccion=-1
        self.espejado=True
    def actualizar(self):
        #Funcion que permite el movimiento de el enemigo
        if self.x <= -300:
            self.direccion=1
            self.espejado = False
        if self.x >= 300:
            self.direccion=-1
            self.espejado = True
        self.x+=self.direccion * 5  
    def largar(self):
        lanzador.disparar()
        
        
#Esta clase crea al Actor   
class Principal(pilasengine.actores.Actor):
    def iniciar(self):
        self.imagen = "Dos.png"
        self.figura = pilas.fisica.Rectangulo(self.x, self.y, 40, 80, friccion=0, restitucion=0)
        self.figura.sin_rotacion = True
        self.figura.escala_de_gravedad = 2
        self.sensor_pies = pilas.fisica.Rectangulo(self.x, self.y, 2, 5, sensor=True, dinamica=False)
        self.saltando = False
        
        
    def actualizar(self):
        velocidad = 10
        salto = 10
        self.x = self.figura.x
        self.y = self.figura.y
        if pilas.control.izquierda:
            self.figura.x -= 5

        if pilas.control.derecha:
            self.figura.x += 5
            
        if pilas.control.arriba:
            self.figura.y +=7
            if not self.saltando:
                self.hacer("SaltarUnaVez")
    
def victoria(personaje, lanzador):
    intro = pilas.musica.cargar("hola.mp3")
    intro.reproducir(repetir=True)
    


lanzador= Enemigo(pilas)
lanzador.escala_x= .7
lanzador.escala_y= .7
lanzador.y=50
lanzador.x=150
    
personaje = Principal(pilas)
personaje.escala_x = .3
personaje.escala_y = .3

pilas.colisiones.agregar(personaje, lanzador, victoria)

lanzador.aprender("Disparar")

def tirar():
    lanzador.disparar()
    return True

pilas.tareas.agregar(0.5,tirar)

lanzador.aprender("Disparar", municion="Bala")

pilas.comportamientos.vincular(SaltarUnaVez)

pilas.ejecutar()