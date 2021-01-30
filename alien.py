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
        