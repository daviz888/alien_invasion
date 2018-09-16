import sys

import pygame
from pygame.constants import QUIT, K_ESCAPE, KEYDOWN


def sprite( SCREEN_WIDTH, SCREEN_HEIGHT, screen, w, h, center):
    animation_frames = []
    # timer = pygame.time.Clock()
    # screen = pygame.display.set_mode( ( SCREEN_WIDTH, SCREEN_HEIGHT ))
    image = pygame.image.load( "images/explosion.png" ).convert_alpha()
    image = pygame.transform.scale(image, (1536, 64))

    width, height = image.get_size()

    for i in range( int( width / w ) ):
        animation_frames.append( image.subsurface( ( i * w, 0, w, h ) ) )

    counter = 0

    total_cells = int(width / w)
    exploding = True

    while exploding:
        for evt in pygame.event.get():
            if evt.type == QUIT or ( evt.type == KEYDOWN and evt.key == K_ESCAPE ) :
                sys.exit()
        if counter == (total_cells - 1):
            exploding = False

        # screen.fill( ( 27, 27, 27 ) )

        screen.blit( animation_frames[counter], (center[0]-64, center[1]-64))
        counter = ( counter + 1 ) % int((width / w))
        pygame.display.flip()

if __name__ == "__main__":
    sprite( 800, 600, 64, 64 )