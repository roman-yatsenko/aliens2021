import sys

import pygame

def check_events(ship):
    """ Отслеживание событий клавиатуры и мыши"""
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT:
                ship.moving_right = True
        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_RIGHT:
                ship.moving_right = False

def update_screen(game_settings, screen, ship):
    """ Обновляет изображение на экране """
    screen.fill(game_settings.bg_color)
    ship.blitme()            

    # Отображение последнего прорисованного экрана
    pygame.display.flip()
