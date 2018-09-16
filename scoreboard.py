"""
scoreboard.py handles the game scoreboard class
"""
import pygame
import pygame.font
from pygame.sprite import Group
from ship import Ship
from sprite_sheets import SpriteSheets
class Scoreboard():
    """A class to report scoring information."""

    def __init__(self, ai_settings, screen, stats):
        """Initialize scorekeeping attribultes."""
        self.screen = screen
        self.screen_rect = screen.get_rect()
        self.ai_settings = ai_settings
        self.stats = stats

        # Font settings for scoring information.
        self.text_color = (0, 255, 0)
        self.font = pygame.font.SysFont(None, 48)

        # Prepare the initial score image.
        self.prep_score()
        self.prep_high_score()
        self.prep_level()
        self.prep_ships()
    
    def prep_score(self):
        """Turn the core into a rendered image."""
        score_str = "{:,}".format(int(round(self.stats.score, -1)))
        self.score_image = self.font.render(score_str, True, self.text_color, None)

        # Display the core at the top right of the screen.
        self.score_rect = self.score_image.get_rect()
        self.score_rect.right = self.screen_rect.right - 20
        self.score_rect.top = 20

    def prep_high_score(self):
        """Turn the high score into a rendered image."""
        high_score_str = "{:,}".format(int(round(self.stats.high_score, -1)))
        self.high_score_image = self.font.render(high_score_str, True, self.text_color, None)

        # Center the high score at the top of the screen.
        self.high_score_rect = self.high_score_image.get_rect()
        self.high_score_rect.centerx = self.screen_rect.centerx
        self.high_score_rect.top = self.score_rect.top

    def prep_level(self):
        """Turn the level into a rendered image."""
        self.level_image = self.font.render(str(self.stats.level), True, self.text_color, None)

        # Position the level below the score.
        self.level_rect = self.level_image.get_rect()
        self.level_rect.right = self.score_rect.right
        self.level_rect.top = self.score_rect.bottom + 10
    
    # def prep_ships(self):
    #     """Show how many ships are left."""
    #     self.ships = Group()
    #     for ship_number in range(self.stats.ships_left):
    #         ship = Ship(self.ai_settings, self.screen)
    #         ship.rect.x = 10 + ship_number * ship.img_rect.width
    #         ship.rect.y = 10
            
    #         # self.ships.add(ship.image.subsurface((ship.img_rect.left, ship.img_rect.height / 2, ship.img_rect.width, ship.img_rect.height / 2)))

    #         self.ships.add(ship)

    def prep_ships(self):
        """ show space ships spritesheets """
        # self.space_ships = Group()
        scale = (30 ,48)
        space_ships = SpriteSheets('images/space_ship.png', 2, 1, scale)

        space_ship = space_ships.get_sheet_frame()
        for ship in range(self.stats.ships_left):
            shipx = 20 + ship * space_ships.cell_width
            shipy = 15
            self.screen.blit(space_ship[1], (shipx, shipy))





    def show_score(self):
        """Draw scor to the screen."""
        self.screen.blit(self.score_image, self.score_rect)
        self.screen.blit(self.high_score_image, self.high_score_rect)
        self.screen.blit(self.level_image, self.level_rect)
        # Draw ships.
        # self.ships.draw(self.screen)
        self.prep_ships()