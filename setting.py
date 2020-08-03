class settings():
    # a class to store the game's settings

    def __init__(self):
        # initialize our games settings and screen settings
        self.screen_width = 1600
        self.screen_height = 800
        self.bg_colour = (135, 206, 250)

        # ship settings
        self.ship_limit = 3

        # Bullet Settings
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_colour = (60, 60, 60)

        #Alien settings
        self.fleet_drop_speed = 10

        #How quickly the game speeds up
        self.speedup_scale = 1.2

        #how quickly alien point value increases
        self.score_scale = 1.5

        self.initialize_dynamic_settings()

    def initialize_dynamic_settings(self):
        #initialize settings that change during game
        self.ship_speed = 3
        self.bullet_speed = 8
        self.alien_speed_factor = 1

        # fleet direction of 1 represents right and -1 represents left
        self.fleet_direction = 1

        #Scoring
        self.alien_points = 100


    def increase_speed(self):
        #increase speed settings and alien point values
        self.ship_speed *= self.speedup_scale
        self.bullet_speed *= self.speedup_scale
        self.alien_speed_factor *= self.speedup_scale
        self.alien_points = int(self.alien_points * self.score_scale)