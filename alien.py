"""
alien class

"""
import pygame
from pygame.sprite import Sprite

class Alien(Sprite):
    """A class to represent a single alien in the fleet."""

    def __init__(self, ai_settings, screen):
        """Initialize the alien and set its starting position."""
        super().__init__()
        self.screen = screen
        self.ai_settings = ai_settings

        # Load the alien image and set its rect attribute.
        self.image = pygame.image.load('images/alien_ship.png')
        self.rect = self.image.get_rect()

        # Loade explosion sheet
        self.img_explode = pygame.image.load('images/explosion.png').convert_alpha()
        self.sheet = pygame.transform.scale(self.img_explode, (1536, 64))


        # Start each new alien new that top of the screen.
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height

        # Store the alien's exact position.
        self.x = float(self.rect.x)

        # initialize animation frames.
        self.frames = []

    def blitme(self):
        """Draw the alien at its current location."""
        self.screen.blit(self.image, self.rect)

    def check_edges(self):
        """Return if alien is at edge of screen."""
        screen_rect = self.screen.get_rect()
        if self.rect.right >= screen_rect.right:
            return True
        elif self.rect.left <= 0:
            return True

    def update(self):
        """Move the alien right"""
        self.x += (self.ai_settings.alien_speed_factor * self.ai_settings.fleet_direction)
        self.rect.x = self.x

    def explode(self):
        width, height = (64, 64) 
        for col in range(int(self.sheet.width / width)):
            rect = pygame.Rect(col * width, 0, width, height)
            image = pygame.Surface(rect.size).convert()
            image.blit(self.sheet, (0,0), rect)
            self.frames.append(image)
