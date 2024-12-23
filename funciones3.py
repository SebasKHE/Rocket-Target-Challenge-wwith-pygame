import sys
import pygame
from bullets3 import Bullets3

def eventos(rocket3, ai_settings, pantalla3, bala, boton, stats, balas):
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            sys.exit()
        elif evento.type == pygame.KEYDOWN:
            tecla_presionada(rocket3, evento, ai_settings, pantalla3, bala)
        elif evento.type == pygame.KEYUP:
            tecla_levantada(rocket3, evento)
        elif evento.type == pygame.MOUSEBUTTONDOWN:
            mouse_x, mouse_y = pygame.mouse.get_pos()
            presionar_play(mouse_x, mouse_y, boton, stats, balas)

def presionar_play(mouse_x, mouse_y, boton, stats, balas):
    boton_presionado = boton.rect.collidepoint(mouse_x, mouse_y)
    if boton_presionado and not stats.game_active:
        pygame.mouse.set_visible(False)
        balas.empty()
        stats.resetear()
        stats.game_active = True

def actualizar_pantalla(ai_settings3, pantalla, rocket3, balas, cuadro, boton, stats, settings):
    pantalla.fill(ai_settings3.bg_color)
    for bala in balas.sprites():
        bala.dibujar_bala()
    cuadro.update(stats, settings)
    cuadro.dibujar_cuadro()
    rocket3.posicionar3()
    if not stats.game_active:
        boton.ubicar()
    pygame.display.flip()

def colision(balas, cuadro, stats, pantalla, settings):
    # Verificar colisión entre las balas y el cuadro
    for bala in balas.sprites():
        if pygame.sprite.collide_rect(bala, cuadro):
            stats.puntos += 1
            balas.remove(bala)  # Eliminar la bala cuando colisiona

    pantalla_rect = pantalla.get_rect()
    # Verificar si alguna bala ha salido del borde derecho
    for bala in balas.sprites():
        if bala.rect.right >= pantalla_rect.right:
            stats.vidas_limite -= 1
            balas.remove(bala)  # Eliminar la bala al salir de la pantalla
    incrementar_dificultad(stats, settings)

def incrementar_dificultad (stats, settings):  
    #Incrementar dificultad cada 3 puntos
    if stats.puntos % 3 == 0 and stats.puntos != stats.ultimo_puntaje:
        settings.incrementar_speed()
        stats.ultimo_puntaje = stats.puntos

def game_over (stats, settings):
    if stats.vidas_limite == 0:
        settings.settings_dinamicos()
        pygame.mouse.set_visible(True)
        stats.game_active = False



def tecla_presionada(rocket3, evento, ai_settings, pantalla3, bala):
    if evento.key == pygame.K_UP:
        rocket3.moving_up = True
    if evento.key == pygame.K_DOWN:
        rocket3.moving_down = True
    if evento.key == pygame.K_SPACE:
        disparar_bala(ai_settings, pantalla3, rocket3, bala)

def tecla_levantada(rocket3, evento):
    if evento.key == pygame.K_UP:
        rocket3.moving_up = False
    if evento.key == pygame.K_DOWN:
        rocket3.moving_down = False

def actualizar_balas(balas, pantalla3):
    balas.update()
    for bala in balas.copy():
        if bala.rect.right > 1200:  # Si la bala sale de la pantalla por el lado derecho
            balas.remove(bala)

def disparar_bala(ai_settings, pantalla3, rocket3, bala):
    
    if len(bala) < ai_settings.bala_allowed:  # Verificar que no haya más balas de las permitidas
        nueva_bala = Bullets3(ai_settings, pantalla3, rocket3)
        bala.add(nueva_bala)