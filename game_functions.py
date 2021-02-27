import sys
from time import sleep

import pygame
from pygame.sprite import Group
from bullet import Bullet

from ship import Ship
from alien import Alien
from game_stats import GameStats
from button import Button
from scoreboard import Scoreboard

class AlienGame():

    def __init__(self, screen, game_settings):
        """ Конструктор класса игры"""
        self.game_settings = game_settings
        self.screen = screen
        # Создание объекта статистики игры
        self.stats = GameStats(game_settings)
        self.sb = Scoreboard(game_settings, screen, self.stats)
        # Создание корабля
        self.ship = Ship(game_settings, screen)
        # Создание пришельца
        self.aliens = Group()
        # Создание флота пришельцев
        self.create_fleet()
        # Создание группы для хранения пуль
        self.bullets = Group()
        # Создание кнопки Play
        self.play_button = Button(game_settings, screen, "Play")

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
            elif event.type == pygame.MOUSEBUTTONDOWN:
                mouse_x, mouse_y = pygame.mouse.get_pos()
                self.check_play_button(mouse_x, mouse_y)

    def check_play_button(self, mouse_x, mouse_y):
        """ Запускает новую игру при нажатии кнопки Play """
        button_clicked = self.play_button.rect.collidepoint(mouse_x, mouse_y)
        if button_clicked and not self.stats.game_active:
            # Сброс игровых настроек
            self.game_settings.initialize_dynamic_settings()

            # Скрываем указатель мыши
            pygame.mouse.set_visible(False)

            # Сброс игровой статистики
            self.stats.reset_stats()
            self.stats.game_active = True

            # Очистка пришельцев и пуль
            self.aliens.empty()
            self.bullets.empty()

            # Создание флота и корабля в центре
            self.create_fleet()
            self.ship.center_ship()

    def update_screen(self):
        """ Обновляет изображение на экране """
        self.screen.fill(self.game_settings.bg_color)
        # Все пули позади корабля и пришельцев
        for bullet in self.bullets.sprites():
            bullet.draw_bullet()
        self.ship.blitme()            
        self.aliens.draw(self.screen)

        # Вывод счета
        self.sb.show_score()

        # Кнопка Play отображается, если игра неактивна
        if not self.stats.game_active:
            self.play_button.draw_button()

        # Отображение последнего прорисованного экрана
        pygame.display.flip()

    def update_bullets(self):
        """ Обновляет пули """
        self.bullets.update()

        # Удаление пуль, вышедших за край экрана
        for bullet in self.bullets.copy():
            if bullet.rect.bottom <= 0:
                self.bullets.remove(bullet)
        
        self.check_bullet_alien_collisions()

    def check_bullet_alien_collisions(self):    
        # Проверка попаданий в пришельцев
        collisions = pygame.sprite.groupcollide(self.bullets, self.aliens, True, True)
        if collisions:
            for aliens in collisions.values():
                self.stats.score += self.game_settings.alien_points * len(aliens)
            self.sb.prep_score()

        if len(self.aliens) == 0:
            # Уничтожение существующих пуль и создание нового флота
            self.bullets.empty()
            self.game_settings.increase_speed()
            self.create_fleet()

    def get_number_aliens_x(self, alien_width):
        """ Вычисляет количество пришельцев в ряду """
        available_space_x = self.game_settings.screen_width - 2 * alien_width
        number_aliens_x = int(available_space_x / (2 * alien_width))
        return number_aliens_x

    def get_number_rows(self, ship_height, alien_height):
        """ Определяет количество рядов флота пришельцев"""
        available_space_y = self.game_settings.screen_height - 3 * alien_height - ship_height
        number_rows = int(available_space_y / (2 * alien_height))
        return number_rows

    def create_alien(self, alien_number, row_number):
        # Создание пришельца и размещение его в ряду
        alien = Alien(self.game_settings, self.screen)
        alien_width = alien.rect.width
        alien.x = alien_width + 2 * alien_width * alien_number
        alien.rect.x = alien.x
        alien.rect.y = alien.rect.height + 2 * alien.rect.height * row_number
        self.aliens.add(alien)

    def create_fleet(self):
        """ Создает флот пришельцев """
        # Вычисление количества пришельцев
        alien = Alien(self.game_settings, self.screen)
        number_aliens_x = self.get_number_aliens_x(alien.rect.width)
        number_rows = self.get_number_rows(self.ship.rect.height, alien.rect.height)

        # Создание флота пришельцев
        for row_number in range(number_rows):
            # Создание ряда пришельцев
            for alien_number in range(number_aliens_x):
                self.create_alien(alien_number, row_number)            

    def update_aliens(self):
        """ Обновление позиции всех пришельцев"""
        self.check_fleet_edges()
        self.aliens.update()

        # Проверка коллизий пришелец-корабль
        if pygame.sprite.spritecollideany(self.ship, self.aliens):
            self.ship_hit()
        
        # Проверка достижения нижнего края пришельцами
        self.check_aliens_bottom()

    def check_aliens_bottom(self):
        """ Проверяет, дорались ли пришельцы до нижнего края"""
        screen_rect = self.screen.get_rect()
        for alien in self.aliens.sprites():
            if alien.rect.bottom >= screen_rect.bottom:
                self.ship_hit()
                break

    def ship_hit(self):
        """ Обрабатывает столкновение корабля с пришельцем"""
        if self.stats.ships_left > 0:
            self.stats.ships_left -= 1
            self.aliens.empty()
            self.bullets.empty()
            self.create_fleet()
            self.ship.center_ship()
            # Пауза
            sleep(0.5)
        else:
            self.stats.game_active = False
            pygame.mouse.set_visible(True)        

    def check_fleet_edges(self):
        """ Реагирует на достижение флотом края экрана"""
        for alien in self.aliens.sprites():
            if alien.check_edges():
                self.change_fleet_direction()
                break

    def change_fleet_direction(self):
        """ Изменяет направление флота"""
        for alien in self.aliens.sprites():
            alien.rect.y += self.game_settings.fleet_drop_speed
        self.game_settings.fleet_direction *= -1
