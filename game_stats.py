class GameStats:
    #Track stats for invaders from python
    def __init__(self, infrompy_settings):
        #initialise stats
        self.infrompy_settings = infrompy_settings
        self.reset_stats()

        #Start game in an inactive state
        self.game_active = False

        #Highscore should never be reset
        self.high_score = 0

    def reset_stats(self):
        #initialize stats that can change during the game
        self.ships_left = self.infrompy_settings.ship_limit
        self.score = 0
        self.level = 1


