from pygame. sprite import Sprite
import pygame

class Rectangulo(Sprite):
    def __init__(self, pantalla):
        super().__init__()

        self.rect = pygame.Rect(0,0, 50, 150)
        self.pantalla = pantalla
        self.pantalla_rect = self.pantalla.get_rect()
        self.rect.right = self.pantalla_rect.right
        self.rect.centery = self.pantalla_rect.centery
        self.y = float(self.rect.centery)
        self.moving_down = True


    def dibujar_cuadro(self):
        pygame.draw.rect(self.pantalla, (255,255,255), self.rect)

    def update(self, stats, settings):
        
        if stats.game_active:
            if self.moving_down:
                self.y += settings.velocidad_cuadro
                self.rect.y = self.y
                if self.rect.bottom >= self.pantalla_rect.bottom:  # Cambia de dirección al llegar al borde inferior
                    self.moving_down = False
            else:
                self.y -= settings.velocidad_cuadro
                self.rect.y = self.y
                if self.rect.top <= self.pantalla_rect.top:  # Cambia de dirección al llegar al borde superior
                    self.moving_down = True

    