import pygame


class Estadisticas ():

    def __init__(self):
        
        self.game_active = False
        self.vidas_limite = 3
        self.puntos = 0
        self.ultimo_puntaje = 0

    def resetear (self):

        self.vidas_limite = 3
        self.puntos = 0

