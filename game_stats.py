class GameStats():
    """ Отслеживание статистики игры"""

    def __init__(self, game_settings):
        """ Инициализирует статистику"""
        self.game_settings = game_settings
        # Игра запускается в неактивном состоянии
        self.game_active = False
        self.reset_stats()
        # Рекорд
        self.high_score = 0
    
    def reset_stats(self):
        """ Инициализирует статистику для одной игры"""
        self.ships_left = self.game_settings.ship_limit
        self.score = 0
        self.level = 1
