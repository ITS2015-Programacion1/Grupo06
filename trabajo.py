#! /usr/bin/env python
# -*- coding: utf-8 -*-
import pilasengine

pilas = pilasengine.iniciar()

#Esta clase crea al Actor   
class Enemigo(pilasengine.actores.Actor):
    def iniciar(self):
        self.imagen = "Dios.jpg"
    #Esta funcion se encarga del movimiento del actor         
    def actualizar(self):       
        if pilas.control.izquierda:
            self.x -= 5
            self.espejado = True
        if pilas.control.derecha:
            self.x += 5
            self.espejado = False

#Muncion creada            
class MiMunicion(pilasengine.actores.Actor):
    def iniciar(self):
        self.imagen = "oferta.png"
        self.rotacion = [360]
        self.escala_y=0.1
        self.escala_x=0.1
        
        

pilas.actores.vincular(MiMunicion)

        
lanzador = Enemigo(pilas)
lanzador.aprender("Disparar", municion="MiMunicion")
lanzador.aprender("LimitadoABordesDePantalla")

pilas.ejecutar()
    
