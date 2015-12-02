#! /usr/bin/env python
# -*- coding: utf-8 -*-
import pilasengine
import time
import Saltar


pilas = pilasengine.iniciar()
pilas.comportamientos.vincular(Saltar.Subir)

#Esta clase crea al Actor   
class Principal(pilasengine.actores.Actor):
    def iniciar(self):
        self.imagen = "basura.jpg"
        self.figura = pilas.fisica.Rectangulo(self.x, self.y, 40,
            friccion=0, restitucion=0)
        self.figura.sin_rotacion = True
        self.figura.escala_de_gravedad = 2
        self.sensor_pies = pilas.fisica.Rectangulo(self.x, self.y, 2, 5, sensor=True, dinamica=False)

    def actualizar(self):
        velocidad = 10
        salto = 15
        self.x = self.figura.x
        self.y = self.figura.y
        if self.pilas.control.derecha:
            self.figura.velocidad_x = velocidad
        elif self.pilas.control.izquierda:
            self.figura.velocidad_x = -velocidad
        else:
            self.figura.velocidad_x = 0

        if self.esta_pisando_el_suelo():
            if self.pilas.control.arriba and int(self.figura.velocidad_y) <= 0:
                self.figura.impulsar(0, 5)
        if pilas.control.abajo:
            self.y -= 5
        
        self.sensor_pies.x = self.x
        self.sensor_pies.y = self.y - 20
        
    def esta_pisando_el_suelo(self):
        return len(self.sensor_pies.figuras_en_contacto) > 0
    
mapa = pilas.actores.MapaTiled('plataformas.tmx', densidad=0,
            restitucion=0, friccion=0, amortiguacion=0)
        
personaje = Principal(pilas)
pilas.ejecutar()