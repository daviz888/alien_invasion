"""
game_function.py module main mudule
"""

import sys
import explosion
from time import sleep
import pygame
from bullet import Bullet
from alien import Alien

def check_keydown_events(event, ai_settings, stats, sb, screen, ship, aliens, bullets):
    """Respond to keypresses."""
    if event.key == pygame.K_RIGHT:
        ship.moving_right = True
    elif event.key == pygame.K_LEFT:
        ship.moving_left = True
    elif event.key == pygame.K_UP:
        ship.moving_up = True
    elif event.key == pygame.K_DOWN:
        ship.moving_down = True
    elif event.key == pygame.K_SPACE:
        if stats.game_active:
            fire_bullets(ai_settings, screen, ship, bullets)
    elif event.key == pygame.K_p:
        if not stats.game_active:
            check_play_button(ai_settings, screen, stats, sb, ship, aliens, bullets)
    elif event.key == pygame.K_q:
        sys.exit()
        
def check_keyup_events(event, ship):
    """Respond to key releases."""
    if event.key == pygame.K_RIGHT:
        ship.moving_right = False
    elif event.key == pygame.K_LEFT:
        ship.moving_left = False
    elif event.key == pygame.K_UP:
        ship.moving_up = False
    elif event.key == pygame.K_DOWN:
        ship.moving_down = False

def check_events(ai_settings, screen, stats, sb, play_button, ship, aliens, bullets):
    """Respond to keypresses and mouse events."""
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            check_keydown_events(event, ai_settings, stats, sb, screen, ship, aliens, bullets)

        elif event.type == pygame.KEYUP:
            check_keyup_events(event, ship)

        elif event.type == pygame.MOUSEBUTTONDOWN:
            mouse_x, mouse_y = pygame.mouse.get_pos()
            check_play_button(ai_settings, screen, stats, sb, ship, aliens, bullets, play_button, mouse_x, mouse_y)

# def start_game(ai_settings, screen, stats, play_button, ship, aliens, bullets, mouse_x = 0, mouse_y = 0):
#     # user user use key to start the game.
#     if stats.game_active

def check_play_button(ai_settings, screen, stats, sb, ship, aliens, bullets, play_button='', mouse_x=0, mouse_y=0):
    """Start a new game when the player clicks Play."""
    # check if user user keyboard/mouse to start the game.
    if play_button:
        button_clicked = play_button.rect.collidepoint(mouse_x, mouse_y)

    elif mouse_x == 0 and mouse_y == 0:
        button_clicked = True

    if button_clicked and not stats.game_active:
        # Reset the game settings.
        ai_settings.initialize_dynamic_settings()

        # Hide the mouse cursor.
        pygame.mouse.set_visible(False)
        # Reset the statatistics.
        stats.reset_stats()
        stats.game_active = True

        # Reset scoreboard images.
        sb.prep_score()
        sb.prep_high_score()
        sb.prep_level()
        sb.prep_ships()

        # Empty the list of aliens and bullets
        aliens.empty()
        bullets.empty()

        # Create a new fleet and center the ship.
        create_fleet(ai_settings, screen, ship, aliens)
        ship.center_ship()

def update_screen(ai_settings, screen, stats, sb, ship, aliens, bullets, play_button):
    """Update images on the screen and flip to the screen"""
    # Redraw screen during each pass through the loop
    screen.fill(ai_settings.bg_color)
    screen.blit(ai_settings.image_background, [0, 0])
    # screen.blit(ai_settings.image_debris, screen.get_rect())

    ship.blitme()
    aliens.draw(screen)

    # Draw the score information.
    sb.show_score()
    # Redraw all bullets behind ship and aliens.
    for bullet in bullets.sprites():
        bullet.draw_bullet()

    # Draw the play button if the game is inactive.
    if not stats.game_active:
        play_button.draw_button()

    # Make the most recently drawn screen visible
    pygame.display.flip()

def update_bullets(ai_settings, screen, stats, sb, ship, aliens, bullets):
    """Update position of bullets and get rid of old bulletes"""
    # Update bullets position.
    bullets.update()

    # GEt rid of the bullets that have disappreared.
    for bullet in bullets.copy():
        if bullet.rect.bottom <= 0:
            bullets.remove(bullet)

    check_bullet_alien_collisions(ai_settings, screen, stats, sb, ship, aliens, bullets)

def check_bullet_alien_collisions(ai_settings, screen, stats, sb, ship, aliens, bullets):
    """Respond to bullet-alien collisions."""
    # Remove any bullets and aliens that have collided.
    collisions = pygame.sprite.groupcollide(bullets, aliens, True, True)


    if collisions:
        for collide in collisions:
            ai_settings.explosion_effects.play()
            explosion.sprite(ai_settings.screen_width, ai_settings.screen_height, screen, 64,64, collide.rect.center)
        for alien in collisions.values():
            stats.score += ai_settings.alien_points * len(alien)
            sb.prep_score()
        check_high_score(stats, sb)

    if len(aliens) == 0:
        # Destroy existing bullets and create new fleet.
        # If the entire fleet is destroyed, start a new level.
        bullets.empty()
        ai_settings.increase_speed()

        # increase level. 
        stats.level +=1
        sb.prep_level()

        create_fleet(ai_settings, screen, ship, aliens)


def fire_bullets(ai_settings, screen, ship, bullets):
    """Fire a bullet if limit not reached yet"""
    # Create a new bullet and add it to the bullets group
    if len(bullets) < ai_settings.bullets_allowed:
        new_bullet = Bullet(ai_settings, screen, ship)
        new_bullet.fire_sound.play()
        bullets.add(new_bullet)

def get_number_aliens_x(ai_settings, alien_width):
    """Determine the number if aliens that fit in a row"""
    available_space_x = ai_settings.screen_width - 2 * alien_width
    number_aliens_x = int(available_space_x / (2 * alien_width))
    return number_aliens_x

def get_number_rows(ai_settings, ship_height, alien_height):
    """Determine the number of rows aliens that fit on the screen."""
    available_space_y = (ai_settings.screen_height -
                            (3 * alien_height) - ship_height)
    number_rows = int(available_space_y / (2 * alien_height))
    return number_rows

def create_alien(ai_settings, screen, aliens, alien_number, row_number):
    """Create an alien and place it in the row."""
    alien = Alien(ai_settings, screen)
    alien_width = alien.rect.width
    alien.x = alien_width + 2 * alien_width * alien_number
    alien.rect.x = alien.x
    alien.rect.y = alien.rect.height + 2 * alien.rect.height * row_number
    aliens.add(alien) 

def create_fleet(ai_settings, screen, ship, aliens):
    """Create a full fleet of aliens"""
    # Create an alien and find the number of alines in a row.
    alien = Alien(ai_settings, screen)
    number_aliens_x = get_number_aliens_x(ai_settings, alien.rect.width)
    number_rows = get_number_rows(ai_settings, ship.rect.height,
        alien.rect.height)

    # Create the first row of aliens.
    for row_number in range(number_rows):
        for alien_number in range(number_aliens_x):
            # Create an alien and place it in the row.
            create_alien(ai_settings, screen, aliens, alien_number, row_number)

def check_fleet_edges(ai_settings, aliens):
    """Respond appropriately if any aliens have reached an edge."""
    for alien in aliens.sprites():
        if alien.check_edges():
            change_fleet_direction(ai_settings, aliens)
            break

def change_fleet_direction(ai_settings, aliens):
    """Drop the entire fleet and change the fleet's direction."""
    for alien in aliens.sprites():
        alien.rect.y += ai_settings.fleet_drop_speed
    ai_settings.fleet_direction *= -1

def ship_hit(ai_settings, screen, stats, sb, ship, aliens, bullets):
    """Respond to ship being hit by alien."""

    if stats.ships_left > 0:
        # Decrement ships_left.
        stats.ships_left -= 1

        # Update scoreboard.
        sb.prep_ships()

        # Empty the list of aliens and bullets.
        aliens.empty()
        bullets.empty()

        # Create a new fleet and center the ship.
        create_fleet(ai_settings, screen, ship, aliens)
        ship.center_ship()

        # Pause
        sleep(0.5)
    else:
        stats.game_active = False
        pygame.mouse.set_visible(True)

def check_aliens_bottom(ai_settings, screen, stats, sb, ship, aliens, bullets):
    """Check if any aliens have reach the buttom of the screen."""
    screen_rect = screen.get_rect()
    for alien in aliens.sprites():
        if alien.rect.bottom >= screen_rect.bottom:
            # Treat this the same as if the ship got hit.
            ship_hit(ai_settings, screen, stats, sb, ship, aliens, bullets)
            break

def check_high_score(stats, sb):
    """Check to see if there's a new high score."""

    if stats.score > stats.high_score:
        stats.high_score = stats.score
        sb.prep_high_score()


def update_aliens(ai_settings, screen, stats, sb, ship, aliens, bullets):
    """
    Check if the fleet is at an edge,
    and then update the position of all alines in the fleet.
    """
    check_fleet_edges(ai_settings, aliens)
    aliens.update()

    # Look for alien-ship collisions.
    if pygame.sprite.spritecollideany(ship, aliens):
        ship_hit(ai_settings, screen, stats, sb, ship, aliens, bullets)

    # Look for aliens hitting the bottom of the screen.
    check_aliens_bottom(ai_settings, screen, stats, sb, ship, aliens, bullets)

def ship_explod(screen):
    explosion_frames = []
    timer = pygame.time.Clock()

    w, h = (64, 64) 
    img_explode = pygame.image.load('images/explosion.png')
    img_explode = pygame.transform.scale(img_explode, (1536, 64))

    width, height = img_explode.get_size()

    for col in range(int(width / w)):     
        explosion_frames.append(img_explode.subsurface(( col * w, 0, w, h )))
    image = pygame.image.load('images/ship.png')

    counter = 0
    total_cells = int(width / w)
    exploding = True
    while exploding:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        if counter == (total_cells - 1):
            exploding = False

        print(counter)
        print(f'total{total_cells}')
        print(explosion_frames[counter])
        screen.blit(image, (100, 15))
        counter += 1
        timer.tick(10)


# def ship_explod(ings, screen):
#     img_explode = pygame.image.load('images/explosion.png')
#     img_explode = pygame.transform.scale(img_explode, (1536, 64))

#     explosion_frames = []
#     timer = pygame.time.Clock()

#     width, height = (64, 64) 
#     total_cells = int(1536/ width)
#     for col in range(total_cells):     
#         rect = pygame.Rect(col * width, 0, width, height)
#         blust = pygame.Surface(rect.size)
#         blust.blit(img_explode, rect)
#         explosion_frames.append(blust)
#     counter = 0
#     exploding = True
#     while exploding:
#         for event in pygame.event.get():
#             if event.type == pygame.QUIT:
#                 pygame.quit()
#                 quit()

#         if counter < total_cells:
#             exploding = False
#         print(counter)
#         print(f'total{total_cells}')
#         screen.blit(explosion_frames[counter], (90, 60))
#         counter += 1
#         timer.tick(20)


        
       