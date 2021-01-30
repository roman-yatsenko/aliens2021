import sys

import pygame
from pygame.sprite import Group
from bullet import Bullet

from ship import Ship
from alien import Alien

class AlienGame():

    def __init__(self, screen, game_settings):
        """ Конструктор класса игры"""
        self.game_settings = game_settings
        self.screen = screen
        # Создание корабля
        self.ship = Ship(game_settings, screen)
        # Создание пришельца
        self.aliens = Group()
        # Создание флота пришельцев
        self.create_fleet()
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
        elif event.key == pygame.K_ESCAPE:
            sys.exit()

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
        self.aliens.draw(self.screen)

        # Отображение последнего прорисованного экрана
        pygame.display.flip()

    def update_bullets(self):
        """ Обновляет пули """
        self.bullets.update()

        # Удаление пуль, вышедших за край экрана
        for bullet in self.bullets.copy():
            if bullet.rect.bottom <= 0:
                self.bullets.remove(bullet)

    def get_number_aliens_x(self, alien_width):
        """ Вычисляет количество пришельцев в ряду """
        available_space_x = self.game_settings.screen_width - 2 * alien_width
        number_aliens_x = int(available_space_x / (2 * alien_width))
        return number_aliens_x

    def create_alien(self, alien_number):
        # Создание пришельца и размещение его в ряду
        alien = Alien(self.game_settings, self.screen)
        alien_width = alien.rect.width
        alien.x = alien_width + 2 * alien_width * alien_number
        alien.rect.x = alien.x
        self.aliens.add(alien)

    def create_fleet(self):
        """ Создает флот пришельцев """
        # Вычисление количества пришельцев
        alien = Alien(self.game_settings, self.screen)
        number_aliens_x = self.get_number_aliens_x(alien.rect.width)

        # Создание первого ряда пришельцев
        for alien_number in range(number_aliens_x):
            self.create_alien(alien_number)            
