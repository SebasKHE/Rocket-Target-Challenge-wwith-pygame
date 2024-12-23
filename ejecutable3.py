import sys
import pygame
from settings3 import Settings3
import funciones3 as f3
from rocket3 import Rocket3
from pygame.sprite import Group
from clases import Rectangulo
from boton import Boton
from stats import Estadisticas

def run_game():

    pygame.init()
    ai_settings3 = Settings3()
    pantalla = pygame.display.set_mode((ai_settings3.screen_width, ai_settings3.screen_heigth))
    pygame.display.set_caption("Practicando en el costado")

    rocket3 = Rocket3(ai_settings3, pantalla)
    balas = Group()
    cuadro = Rectangulo(pantalla)
    boton = Boton(pantalla, "Play")

    stats = Estadisticas()

    while True:
    
        if stats.game_active:
            rocket3.actualizar_pos(ai_settings3)
            f3.actualizar_balas(balas, pantalla)
            f3.game_over(stats, ai_settings3)
            f3.colision(balas, cuadro, stats, pantalla, ai_settings3)
        f3.eventos(rocket3, ai_settings3, pantalla, balas, boton, stats, balas)
        f3.actualizar_pantalla(ai_settings3, pantalla, rocket3, balas, cuadro, boton, stats, ai_settings3)

        print(len(balas))
        print("Vidas " + str(stats.vidas_limite))
        print("Puntos" + str(stats.puntos))


run_game()