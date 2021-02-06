import pygame
from pygame.sprite import Sprite


class Alien(Sprite):
    """ Класс Пришелец"""

    def __init__(self, game_settings, screen):
        """ Инициализация пришельца"""
        super().__init__()
        self.screen = screen
        self.game_settings = game_settings

        # Загрузка изображения
        self.image = pygame.image.load('images/alien.bmp')
        self.rect = self.image.get_rect()

        # Каждый новый пришелец появляется в левом верхнем углу экрана
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height

        # Вещественная позиция пришельца
        self.x = float(self.rect.x)

    def blitme(self):
        """ выводит пришельца на экран"""
        self.screen.blit(self.image, self.rect)
        
    def update(self):
        """ Перемещает пришельца вправо"""
        self.x += (self.game_settings.alien_speed_factor * 
                   self.game_settings.fleet_direction)
        self.rect.x = self.x

    def check_edges(self):
        """ Возвращает True, если пришелец у края экрана"""
        screen_rect = self.screen.get_rect()
        if self.rect.right >= screen_rect.right:
            return True
        elif self.rect.left <= 0:
            return True
