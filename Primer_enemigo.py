# -*- encoding: utf-8 -*-
import pilasengine

pilas = pilasengine.iniciar()

class enemigo(pilasengine.actores.Actor):
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
         
            
lanzador= enemigo(pilas)
lanzador.escala_x= .4
lanzador.escala_y= .4

pilas.ejecutar()
    
