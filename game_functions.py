import sys

import pygame
from pygame.sprite import Group
from bullet import Bullet

from ship import Ship

class AlienGame():

    def __init__(self, screen, game_settings):
        """ Конструктор класса игры"""
        self.game_settings = game_settings
        self.screen = screen
        # Создание корабля
        self.ship = Ship(game_settings, screen)
        # Создание группы для хранения пуль
        self.bullets = Group()

    def check_keydown_events(self, event):
        """ Реагирует на нажатие клавиш"""
        if event.key == pygame.K_RIGHT:
            self.ship.moving_right = True
        elif event.key == pygame.K_LEFT:
            self.ship.moving_left = True
        elif event.key == pygame.K_SPACE:
            self.fire_bullet()

    def fire_bullet(self):
        # Создание новой пули и включение в группу bullets
        if len(self.bullets) < self.game_settings.bullets_allowed:
            new_bullet = Bullet(self.game_settings, self.screen, self.ship)
            self.bullets.add(new_bullet)

    def check_keyup_events(self, event):
        """ Реагирует на отпускание клавиш """
        if event.key == pygame.K_RIGHT:
            self.ship.moving_right = False
        elif event.key == pygame.K_LEFT:
            self.ship.moving_left = False

    def check_events(self):
        """ Отслеживание событий клавиатуры и мыши"""
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                self.check_keydown_events(event)
            elif event.type == pygame.KEYUP:
                self.check_keyup_events(event)

    def update_screen(self):
        """ Обновляет изображение на экране """
        self.screen.fill(self.game_settings.bg_color)
        # Все пули позади корабля и пришельцев
        for bullet in self.bullets.sprites():
            bullet.draw_bullet()
        self.ship.blitme()            

        # Отображение последнего прорисованного экрана
        pygame.display.flip()

    def update_bullets(self):
        """ Обновляет пули """
        self.bullets.update()

        # Удаление пуль, вышедших за край экрана
        for bullet in self.bullets.copy():
            if bullet.rect.bottom <= 0:
                self.bullets.remove(bullet)
