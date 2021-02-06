class GameStats():
    """ Отслеживание статистики игры"""

    def __init__(self, game_settings):
        """ Инициализирует статистику"""
        self.game_settings = game_settings
        # Игра запускается в активном состоянии
        self.game_active = True
        self.reset_stats()
    
    def reset_stats(self):
        """ Инициализирует статистику для одной игры"""
        self.ships_left = self.game_settings.ship_limit
