#! /usr/bin/env python
# -*- coding: utf-8 -*-
import pilasengine
import time

a=3
pilas = pilasengine.iniciar()

fondo = pilas.actores.MapaTiled('PROGRAMA.tmx')
pilas.fisica.eliminar_techo()
pilas.fisica.eliminar_suelo()
pilas.fisica.eliminar_paredes()

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
 

#Esta clase crea al Actor   
class Principal(pilasengine.actores.Actor):
    def iniciar(self):
        self.x=-3574
        self.y=-119
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
            self.figura.y +=6
            if not self.saltando:
                self.hacer("SaltarUnaVez")
 
        pilas.camara.x=self.x

"""
class Golpe(pilasengine.actores.Actor):
	def iniciar(self):
		self.imagen="espada.png"
		personaje.hide()
"""

#Esta clase es la del enemigo
class Enemigo(pilasengine.actores.Actor):
    def iniciar(self):
        self.imagen ="primer_enemigo.png"
        self.x = -1035
        self.y = -110
        self.direccion=-1
        self.espejado=True
    
    """def actualizar(self):
        #Funcion que permite el movimiento de el enemigo
        if self.x <= -300:
            self.direccion=1
            self.espejado = False
        if self.x >= 300:
            self.direccion=-1
            self.espejado = True
        self.x+=self.direccion * 5  
        """
class MiMunicion(pilasengine.actores.Actor):
    def iniciar(self):
        self.imagen= "espada.png"
        self.espejado=True


class Toxico1(pilasengine.actores.Actor):
	def iniciar(self):
		self.imagen = "Enemigo.png"
		self.x = -2770
		self.y = -260

class Toxico2(pilasengine.actores.Actor):
	def iniciar(self):
		self.imagen="Pelota.png"
		self.x =-2030
		self.y =-220

class Toxico3(pilasengine.actores.Actor):
	def iniciar(self):
		self.imagen="basura.jpg"
		self.x = -1657
		self.y = -215

class Toxico4(pilasengine.actores.Actor):
	def iniciar(self):
		self.imagen="Bala.png"
		self.x = -1488
		self.y = -215

class Toxico5(pilasengine.actores.Actor):
	def iniciar(self):
		self.imagen="Dios.jpg"
		self.x = -1332
		self.y = -230

class Toxico6(pilasengine.actores.Actor):
	def iniciar(self):
		self.imagen="index.jpeg"
		self.x = -1125
		self.y = -230

class Toxico7(pilasengine.actores.Actor):
	def iniciar(self):
		self.imagen="espada.png"
		self.x = -945
		self.y = -230

class Lava1(pilasengine.actores.Actor):
	def iniciar(self):
		self.imagen="Cara.jpg"
		self.x = 224
		self.y = -228

class Lava2(pilasengine.actores.Actor):
	def iniciar(self):
		self.imagen="logo.jpg"
		self.x = 481
		self.y = -216

class Lava3(pilasengine.actores.Actor):
	def iniciar(self):
		self.imagen="hola.jpg"
		self.x = 690
		self.y = -216

class Lava4(pilasengine.actores.Actor):
	def iniciar(self):
		self.imagen="pingu.png"
		self.x = 1050
		self.y = -216

class Lava5(pilasengine.actores.Actor):
	def iniciar(self):
		self.imagen="imagen.png"
		self.x = 1935
		self.y = -178

def volver1():
	global personaje
	print "Hola"

def volver2():
	global personaje
	print "Chau"


def volver3():
	global personaje
	print "Anime"

def volver4():
	global personaje
	print "Funciona"

def volver5():
	global personaje
	print "Vamos Bien"

def volver6():
	global personaje
	print "Segui Asi"


def volver7():
	global personaje
	print "AAAAAAAAAAAA"

def volver8():
	global personaje
	print "Don Bosco"

def volver9():
	global personaje
	print "Vicio"


def volver10():
	global personaje
	print "HP"


def volver11():
	global personaje
	print "Chotovo"

def volver12():
	global personaje
	print "NIGGA"

def victoria(personaje, lanzador):
    intro = pilas.musica.cargar("Hola.mp3")
    intro.reproducir(repetir=True)
    
def Muere_enemigo(bonus, lanzador):
	lanzador.eliminar()
	bonus.eliminar()

def tirar():
    lanzador.disparar()
    return True

def perder():
    global personaje
    global a
    a = a - 1
    if a!=0:
        if a==1:
            pilas.avisar("Te queda "+str(a)+" vida. ENCONTRA UNA OFERTA RAPIDO")
        else:
            pilas.avisar("Te quedan "+str(a)+" vidas")
    if (a == 0):
        personaje.eliminar()
        pilas.avisar("Perdiste")

pilas.actores.vincular(MiMunicion)
pilas.actores.vincular(Principal)
pilas.actores.vincular(Enemigo)
"""
bonus = Golpe(pilas)
"""
personaje = pilas.actores.Principal()
personaje.escala_x = .3
personaje.escala_y = .3
personaje.radio_de_colision = personaje.escala*50
personaje.aprender("PuedeExplotar")

lanzador= pilas.actores.Enemigo()
lanzador.escala_x= .3
lanzador.escala_y= .3

# Todas estas clases pertenecen a los obstaculos del mapa
toxico = Toxico1(pilas)
toxico.escala_x = .0
toxico.escala_y = .0
rectangulo = pilas.fisica.Rectangulo(0, 0, 290, 75, sensor=True, dinamica=False)
toxico.figura_de_colision = rectangulo

toxico2 = Toxico2(pilas)
toxico2.escala_x = .0
toxico2.escala_y = .0
rectangulo = pilas.fisica.Rectangulo(0, 0, 220, 50, sensor=True, dinamica=False)
toxico2.figura_de_colision = rectangulo

toxico3 = Toxico3(pilas)
toxico3.escala_x = .0
toxico3.escala_y = .0
rectangulo = pilas.fisica.Rectangulo(0, 0, 150, 50, sensor=True, dinamica=False)
toxico3.figura_de_colision = rectangulo

toxico4 = Toxico4(pilas)
toxico4.escala_x = .0
toxico4.escala_y = .0
rectangulo = pilas.fisica.Rectangulo(0, 0, 105, 50, sensor=True, dinamica=False)
toxico4.figura_de_colision = rectangulo

toxico5 = Toxico5(pilas)
toxico5.escala_x = .0
toxico5.escala_y = .0
rectangulo = pilas.fisica.Rectangulo(0, 0, 100, 15, sensor=True, dinamica=False)
toxico5.figura_de_colision = rectangulo

toxico6 = Toxico6(pilas)
toxico6.escala_x = .0
toxico6.escala_y = .0
rectangulo = pilas.fisica.Rectangulo(0, 0, 135, 15, sensor=True, dinamica=False)
toxico6.figura_de_colision = rectangulo

toxico7 = Toxico7(pilas)
toxico7.escala_x = .0
toxico7.escala_y = .0
rectangulo = pilas.fisica.Rectangulo(0, 0, 170, 17, sensor=True, dinamica=False)
toxico7.figura_de_colision = rectangulo

lava1= Lava1(pilas)
lava1.escala_x = .0
lava1.escala_y = .0
rectangulo = pilas.fisica.Rectangulo(0, 0, 185, 70, sensor=True, dinamica=False)
lava1.figura_de_colision = rectangulo

lava2= Lava2(pilas)
lava2.escala_x = .0
lava2.escala_y = .0
rectangulo = pilas.fisica.Rectangulo(0, 0, 62, 44, sensor=True, dinamica=False)
lava2.figura_de_colision = rectangulo

lava3= Lava3(pilas)
lava3.escala_x = .0
lava3.escala_y = .0
rectangulo = pilas.fisica.Rectangulo(0, 0, 96, 44, sensor=True, dinamica=False)
lava3.figura_de_colision = rectangulo

lava4 = Lava4(pilas)
lava4.escala_x = .0
lava4.escala_y = .0
rectangulo = pilas.fisica.Rectangulo(0, 0, 200, 44, sensor=True, dinamica=False)
lava4.figura_de_colision = rectangulo

lava5 = Lava5(pilas)
lava5.escala_x = .0
lava5.escala_y = .0
rectangulo = pilas.fisica.Rectangulo(0, 0, 100, 100, sensor=True, dinamica=False)
lava5.figura_de_colision = rectangulo

lanzador.aprender("Disparar", municion="MiMunicion", angulo_salida_disparo = 180 ,grupo_enemigos = personaje, cuando_elimina_enemigo = perder)

pilas.tareas.agregar(1.2,tirar)

pilas.colisiones.agregar(personaje, lanzador, victoria)

pilas.colisiones.agregar(personaje, toxico, volver1)

pilas.colisiones.agregar(personaje, toxico2, volver2)

pilas.colisiones.agregar(personaje, toxico3, volver3)

pilas.colisiones.agregar(personaje, toxico4, volver4)

pilas.colisiones.agregar(personaje, toxico5, volver5)

pilas.colisiones.agregar(personaje, toxico6, volver6)

pilas.colisiones.agregar(personaje, toxico7, volver7)

pilas.colisiones.agregar(personaje, lava1, volver8)

pilas.colisiones.agregar(personaje, lava2, volver9)

pilas.colisiones.agregar(personaje, lava3, volver10)

pilas.colisiones.agregar(personaje, lava4, volver11)

pilas.colisiones.agregar(personaje, lava5, volver12)

"""
pilas.colisiones.agregar(bonus, lanzador,Muere_enemigo)
"""
pilas.comportamientos.vincular(SaltarUnaVez)

pilas.ejecutar()