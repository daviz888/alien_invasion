import pygame
from pygame.sprite import Sprite

class Bullet(Sprite):
    """A class to manage bullet fired from the ship"""

    def __init__(self, ai_settings, screen, ship):
        """Create a bullet object at the ship's current position"""
        super(Bullet, self).__init__()
        self.screen = screen

        # Create a bullet rect at (0, 0) and then sset correct position
        # self.rect = pygame.Rect(0, 0, ai_settings.bullet_width,
        #     ai_settings.bullet_height)
        # updates uses image instead of drawing Rect.
        self.bullet_image = pygame.image.load('images/shot2.png')
        self.rect = self.bullet_image.get_rect()
        self.rect.centerx = ship.rect.centerx
        self.rect.top = ship.rect.top

        # Store the bullet's position as a decimal value
        self.y = float(self.rect.y)
        
        self.color = ai_settings.bullet_color
        self.speed_factor = ai_settings.bullet_speed_factor
        
        self.fire_sound = pygame.mixer.Sound('music/missile.ogg')

        

    def update(self):
        """Move the bullet up the screen."""
        # Update the decimal position of the bullet
        self.y -= self.speed_factor
        
        # Update the rect position
        self.rect.y = self.y

    def draw_bullet(self):
        """Draw the bullet to the screen"""
        # pygame.draw.rect(self.screen, self.color, self.rect)
        self.screen.blit(self.bullet_image, self.rect)

