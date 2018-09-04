import pygame

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
        self.bullet_speed_factor = 5
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = (60, 60, 60)
        self.bullets_allowed = 5

    def set_music_background(self):
        pygame.mixer.init()
        pygame.mixer.music.load('music/intro.mp3')
        pygame.mixer.music.play()



        