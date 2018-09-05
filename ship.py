import pygame

class Ship():
    """ Ship class"""
    def __init__(self, ai_settings, screen):
        """Initialize the ship set its settings position"""
        self.screen = screen
        self.ai_settings = ai_settings

        # Load the ship image and get its rect.
        # self.image = pygame.image.load('images/superman.png')
        self.image = pygame.image.load('images/ship.png')

        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()

        # Start each new ship at the bottom center of the screen
        self.rect.centerx = self.screen_rect.centerx
        self.rect.bottom = self.screen_rect.bottom

        # Store a decimal value for the ship's center
        self.center = float(self.rect.centerx)

        # Movement flag
        self.moving_right = False
        self.moving_left = False
        self.moving_up = False
        self.moving_down = False

    def update(self):
        """Update the ship's position based on the movement flag."""
        # Update the ship's center value, not the rect.
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.center += self.ai_settings.ship_speed_factor
        if self.moving_left and self.rect.left > 0:
            self.center -= self.ai_settings.ship_speed_factor
        if self.moving_up and self.rect.y > self.screen_rect.top:
            self.rect.y -= self.ai_settings.ship_speed_factor
        if self.moving_down and self.rect.bottom < self.screen_rect.bottom:
            self.rect.y += self.ai_settings.ship_speed_factor
            
        self.rect.centerx = self.center


    def blitme(self):
        """Draw the ship at its current loacation"""
        self.screen.blit(self.image, self.rect)
