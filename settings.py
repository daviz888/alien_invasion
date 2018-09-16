import sys
import pygame

class Settings():
    """ A class to store all settings for Alien Invasion"""

    def __init__(self):
        """Initializae the game's settings."""
        # Screen settings
        self.screen_width = 1024
        self.screen_height = 600
        self.bg_color = (135, 206, 250)
        # self.image_background = pygame.image.load('images/bgimage.png').convert()
        self.image_background = pygame.image.load('images/universe.png')
        self.image_debris = pygame.image.load('images/debris.png')
        self.image_background = pygame.transform.scale(self.image_background, (self.screen_width, self.screen_height))
        self.image_debris = pygame.transform.scale(self.image_debris,
            (self.screen_width, self.screen_height))


          # Loade explosion sheet
        # self.img_explode = pygame.image.load('images/explosion.png')
        # self.img_explode = pygame.transform.scale(self.img_explode, (1536, 64))

        #Ship Settings
        self.ship_limit = 3

        # Bullet settings
        self.bullet_width = 0
        self.bullet_height = 15
        self.bullet_color = (60, 60, 60)
        self.bullets_allowed = 5

        # Alien settings.
        self.fleet_drop_speed = 10
       

        # how quickly the game speeds up
        self.speedup_scale = 1.1
        # how quickly the alien point values increase
        self.score_scale = 1.5

        self.initialize_dynamic_settings()

        # Set explosion effects.
        self.explosion_effects = pygame.mixer.Sound('music/explosion.ogg')

    def set_music_background(self):
        """Add music background."""
        pygame.mixer.init()
        pygame.mixer.music.load('music/soundtrack.ogg')
        pygame.mixer.music.play(-1)

    def initialize_dynamic_settings(self):
        """Initialize settings that change throughout the game."""
        self.ship_speed_factor = 1.5
        self.bullet_speed_factor = 3
        self.alien_speed_factor = 1

         # fleet_direction of 1 represents right; -1 represents left.
        self.fleet_direction = 1

        # Scoring
        self.alien_points = 50

    def increase_speed(self):
        """Increase speed settings."""
        self.ship_speed_factor *= self.speedup_scale
        self.bullet_speed_factor *= self.speedup_scale
        self.alien_speed_factor *= self.speedup_scale

        self.alien_points = int(self.alien_points * self.score_scale)

