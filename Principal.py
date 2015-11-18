#! /usr/bin/env python
# -*- coding: utf-8 -*-
import pilasengine
import time

a=3
pilas = pilasengine.iniciar()

fondo = pilas.actores.MapaTiled('PROGRAMA.tmx')

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
        
class MiMunicion(pilasengine.actores.Actor):
    def iniciar(self):
        self.imagen= "Bala.png"
        self.espejado=True
        
        
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
 
        pilas.camara.x=self.x

def victoria(personaje, lanzador):
    intro = pilas.musica.cargar("Hola.mp3")
    intro.reproducir(repetir=True)
    

def tirar():
    lanzador.disparar()
    return True

def Perder():
    global personaje
    global a
    a = a - 1
    if a!=0:
        if a==1:
            pilas.avisar("Te queda "+str(a)+" vida. Ponete las pilas papa")
        else:
            pilas.avisar("Te quedan "+str(a)+" vidas")
    if (a == 0):
        personaje.eliminar()
        pilas.avisar("Perdiste")
        
pilas.actores.vincular(MiMunicion)
pilas.actores.vincular(Principal)
pilas.actores.vincular(Enemigo)

lanzador= pilas.actores.Enemigo()
lanzador.escala_x= .7
lanzador.escala_y= .7
lanzador.y=50
lanzador.x=150
    
personaje = pilas.actores.Principal()
personaje.escala_x = .3
personaje.escala_y = .3
personaje.radio_de_colision = personaje.escala*50
personaje.aprender("PuedeExplotar")

pilas.colisiones.agregar(personaje, lanzador, victoria)  

lanzador.aprender("Disparar", municion="MiMunicion")

pilas.tareas.agregar(0.5,tirar)

pilas.colisiones.agregar(lanzador, personaje, Perder)

pilas.comportamientos.vincular(SaltarUnaVez)

pilas.ejecutar()
