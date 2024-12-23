import pygame   
from pygame.sprite import Sprite

class Bullets3 (Sprite):

    def __init__(self, ai_settings, pantalla3, rocket3):
        super().__init__()
        self.pantalla3 = pantalla3

        self.rect = pygame.Rect(0,0, ai_settings.bala_width, ai_settings.bala_heigth)
        self.rect.centery = rocket3.imagen_rect.centery
        self.rect.right = rocket3.imagen_rect.right

        self.x = float(self.rect.x)
        self.color = ai_settings.bala_color
        self.speed_factor = ai_settings.bala_speed_factor

    def update (self,):

        self.x += self.speed_factor
        self.rect.x = self.x

    def dibujar_bala(self):
        pygame.draw.rect(self.pantalla3, self.color, self.rect)