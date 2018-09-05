import pygame

class Settings():
    """ A class to store all settings for Alien Invasion"""

    def __init__(self):
        """Initializae the game's settings."""
        # Screen settings
        self.screen_width = 1000
        self.screen_height = 600
        self.bg_color = (135, 206, 250)
        self.image_background = pygame.image.load('images/aerial_view.png')
        self.image_debris = pygame.image.load('images/debris.png')
        self.image_background = pygame.transform.scale(self.image_background, 
            (self.screen_width, self.screen_height))
        self.image_debris = pygame.transform.scale(self.image_debris,
            (self.screen_width, self.screen_height))

        #Ship Settings
        self.ship_speed_factor = 1.5

        # Bullet settings
        self.bullet_speed_factor = 5
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = (60, 60, 60)
        self.bullets_allowed = 5

    def set_music_background(self):
        """Add music background."""
        pygame.mixer.init()
        pygame.mixer.music.load('music/intro.ogg')
        pygame.mixer.music.play(-1)

    def set_screen_background(self, screen):
        """Add screen backgoudn"""
        pass
        
        



        