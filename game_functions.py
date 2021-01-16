import sys

import pygame

def check_events(ship):
    """ Отслеживание событий клавиатуры и мыши"""
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT:
                # Переместить корабль вправо
                ship.rect.centerx += 1

def update_screen(game_settings, screen, ship):
    """ Обновляет изображение на экране """
    screen.fill(game_settings.bg_color)
    ship.blitme()            

    # Отображение последнего прорисованного экрана
    pygame.display.flip()
