import pygame

class Rocket3:

    def __init__(self, ai_settings3, pantalla):
        
        self.ai_settings3 = ai_settings3
        self.pantalla = pantalla
        self.imagen = pygame.image.load("rocket3.png")
        self.imagen_rect = self.imagen.get_rect()
        self.pantalla_rect = pantalla.get_rect()
        self.imagen_rect.left = self.pantalla_rect.left
        self.imagen_rect.centery = self.pantalla_rect.centery

        self.center = float(self.imagen_rect.centery)

        self.moving_up = False
        self.moving_down = False


    def posicionar3 (self):

        self.pantalla.blit(self.imagen, self.imagen_rect )

    def actualizar_pos (self, ai_settings3):

        if self.moving_up and self.imagen_rect.top > 0:
            self.center -= ai_settings3.velocidad_cohete
        if self.moving_down and self.imagen_rect.bottom < self.pantalla_rect.bottom:
            self.center += ai_settings3.velocidad_cohete

        self.imagen_rect.centery = self.center