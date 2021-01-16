import sys

import pygame

def check_events():
    """ Отслеживание событий клавиатуры и мыши"""
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

def update_screen(game_settings, screen, ship):
    """ Обновляет изображение на экране """
    screen.fill(game_settings.bg_color)
    ship.blitme()            

    # Отображение последнего прорисованного экрана
    pygame.display.flip()
    