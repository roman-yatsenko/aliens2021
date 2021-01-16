import pygame

class Ship():
    """ Космический корабль игрока"""

    def __init__(self, game_settings, screen):
        """ Инициализирует корабль и задает его начальную позицию"""
        self.screen = screen
        self.game_settings = game_settings

        # Загрузка изображения корабля и получение прямоугольника
        self.image = pygame.image.load('images/ship.bmp')
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()
        # Каждый новый корабль появляется у нижнего края экрана
        self.rect.centerx = self.screen_rect.centerx
        self.rect.bottom = self.screen_rect.bottom

        # Вещественная координата центра корабля
        self.center = float(self.rect.centerx)

        # Флаги перемещения
        self.moving_right = False
        self.moving_left = False

    def update(self):
        """ Обновляет позицию корабля с учетом флага """
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.center += self.game_settings.ship_speed_factor
        if self.moving_left and self.rect.left > 0:
            self.center -= self.game_settings.ship_speed_factor
        
        # Обновление атрибута centerx
        self.rect.centerx = self.center

    def blitme(self):
        """ рисует корабль в текущей позиции"""
        self.screen.blit(self.image, self.rect)
        