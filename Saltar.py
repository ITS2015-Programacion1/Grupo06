# -*- encoding: utf-8 -*-

from pilasengine import comportamientos

class Subir(comportamientos.Comportamiento):
    def iniciar(self, receptor, velocidad_inicial=10, cuando_termina=None):
        super(Subir, self).iniciar(receptor)
        self.velocidad_inicial = velocidad_inicial
        self.cuando_termina = cuando_termina
        self.sonido_saltar = self.pilas.sonidos.cargar("audio/saltar.wav")
        self.suelo = int(self.receptor.y)
        self.velocidad = self.velocidad_inicial
        self.sonido_saltar.reproducir()
        self.velocidad_aux = self.velocidad_inicial
        self.receptor.saltando=True

    def actualizar(self):
        self.receptor.y += self.velocidad
        self.velocidad -= 0.3
        if self.receptor.y <= self.suelo:
            self.velocidad_aux /= 2.0
            self.velocidad = self.velocidad_aux
            if self.velocidad_aux <= 1:
                self.receptor.y = self.suelo
                if self.cuando_termina:
                    self.cuando_termina()
                    self.receptor.saltando=False
                return True

                
    def actualizar(self):
        self.receptor.y += self.velocidad
        self.velocidad -= 0.3
        if self.receptor.y <= self.suelo:
            self.velocidad_aux /= 2.0
            self.velocidad = self.velocidad_aux
            if self.velocidad_aux <= 1:
                # Si toca el suelo
                self.receptor.y = self.suelo
                if self.cuando_termina:
                    self.cuando_termina()
            return True