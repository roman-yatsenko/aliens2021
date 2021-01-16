import pygame
from pygame.sprite import Group

from settings import Settings
from ship import Ship
import game_functions as gf

def run_game():
    # Инициализирует игру и создает объект экрана
    pygame.init()
    game_settings = Settings()
    screen = pygame.display.set_mode((game_settings.screen_width, game_settings.screen_height))
    pygame.display.set_caption("Пришельцы 2021")

    # Создание корабля
    ship = Ship(game_settings, screen)
    # Создание группы для хранения пуль
    bullets = Group()

    # Запуск основного цикла игры
    while True:
        # Отслеживание событий клавиатуры и мыши
        gf.check_events(game_settings, screen, ship, bullets)

        # При каждом проходе цикла перерисовывается экран
        ship.update()
        gf.update_bullets(bullets)
        
        gf.update_screen(game_settings, screen, ship, bullets)

run_game()
