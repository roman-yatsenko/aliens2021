import sys

import pygame

from settings import Settings
from ship import Ship

def run_game():
    # Инициализирует игру и создает объект экрана
    pygame.init()
    game_settings = Settings()
    screen = pygame.display.set_mode((game_settings.screen_width, game_settings.screen_height))
    pygame.display.set_caption("Пришельцы 2021")

    # Создание корабля
    ship = Ship(screen)

    # Запуск основного цикла игры
    while True:
        # Отслеживание событий клавиатуры и мыши
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()

        # При каждом проходе цикла перерисовывается экран
        screen.fill(game_settings.bg_color)
        ship.blitme()

        # Отображение последнего прорисованного экрана
        pygame.display.flip()

run_game()
