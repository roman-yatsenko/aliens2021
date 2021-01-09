import sys

import pygame

def run_game():
    # Инициализирует игру и создает объект экрана
    pygame.init()
    screen = pygame.display.set_mode((800, 600))
    pygame.display.set_caption("Пришельцы 2021")
    # Назначение цвета фона
    bg_color = (230, 230, 230)

    # Запуск основного цикла игры
    while True:
        # Отслеживание событий клавиатуры и мыши
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()

        # При каждом проходе цикла перерисовывается экран
        screen.fill(bg_color)
        
        # Отображение последнего прорисованного экрана
        pygame.display.flip()

run_game()
