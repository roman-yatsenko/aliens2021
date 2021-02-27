class Settings():
    """Класс для хранения всех настроек игры"""

    def __init__(self):
        """Инициализирует настройки игры"""
        self.screen_width = 800
        self.screen_height = 600
        self.bg_color = (230, 230, 230)

        # Настройки корабля
        self.ship_speed_factor = 0.5
        self.ship_limit = 3

        # Параметры пули
        self.bullet_speed_factor = 0.3
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = 60, 60, 60
        self.bullets_allowed = 3

        # Настройки пришельцев
        self.alien_speed_factor = 0.1
        self.fleet_drop_speed = 10
        # 1 - вправо, -1 - влево
        self.fleet_direction = 1
