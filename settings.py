class Settings():
    """ A class to store all settings for Alien Invasion"""

    def __init__(self):
        """Initializae the game's settings."""
        # Screen settings
        self.screen_width = 1000
        self.screen_height = 600
        self.bg_color = (135, 206, 250)

        #Ship Settings
        self.ship_speed_factor = 1.5

        # Bullet settings
        self.bullet_speed_factor = 2
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = (60, 60, 60)

        