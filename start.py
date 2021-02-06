import pygame

from settings import Settings
from game_functions import AlienGame

def run_game():
    # Инициализирует игру и создает объект экрана
    pygame.init()
    game_settings = Settings()
    screen = pygame.display.set_mode((game_settings.screen_width, game_settings.screen_height))
    pygame.display.set_caption("Пришельцы 2021")

    # Создание главного объекта игры
    main_game = AlienGame(screen, game_settings)

    # Запуск основного цикла игры
    while True:
        # Отслеживание событий клавиатуры и мыши
        main_game.check_events()

        # При каждом проходе цикла перерисовывается экран
        main_game.ship.update()
        main_game.update_bullets()
        main_game.update_aliens()
        main_game.update_screen()

run_game()
