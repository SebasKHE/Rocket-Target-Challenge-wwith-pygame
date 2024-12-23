import pygame.font

class Boton():
    
    def __init__(self, pantalla, msg):
        
        self.rect = pygame.Rect(0, 0, 150, 50)
        self.pantalla = pantalla
        self.pantalla_rect = self.pantalla.get_rect()
        self.rect.center = self.pantalla_rect.center
        self.font = pygame.font.SysFont(None, 48)

        self.preparar_msg(msg)

    def preparar_msg (self, msg):

        self.msg_imagen = self.font.render(msg, True, (4,5,6),(45,4,0))
        self.msg_imagen_rect = self.msg_imagen.get_rect()
        self.msg_imagen_rect.center = self.rect.center

    def ubicar (self):

        self.pantalla.fill((45,4,0), self)
        self.pantalla.blit(self.msg_imagen, self.msg_imagen_rect)