import sys

from time import sleep

import pygame

from bullet import Bullet

from alien import Alien


def ship_hit(infrompy_settings, screen, stats, sb, ship, aliens, bullets):
    # Respond to ship getting hit by an alien
    if stats.ships_left > 0:
        # Decrement ships_left
        stats.ships_left -= 1

        #update scoreboard
        sb.prep_ships()

        # empty the list of aliens and bullets
        aliens.empty()
        bullets.empty()

        # Create a new fleet and center the ship
        create_fleet(infrompy_settings, screen, ship, aliens)
        ship.center_ship()

        # Pause
        sleep(0.5)
    else:
        stats.game_active = False
        pygame.mouse.set_visible(True)


def check_keydown_events(event, infrompy_settings, screen, ship, bullets):
    # Respond to key presses
    if event.key == pygame.K_RIGHT:
        ship.moving_right = True
    elif event.key == pygame.K_LEFT:
        ship.moving_left = True
    # elif event.key == pygame.K_UP:
    # ship.moving_up = True
    # elif event.key == pygame.K_DOWN:
    # ship.moving_down = True
    elif event.key == pygame.K_SPACE:
        # Create new bullet and add it to bullets group
        new_bullet = Bullet(infrompy_settings, screen, ship)
        bullets.add(new_bullet)  # stores new bullets in bullets list


def check_keyup_events(event, ship):
    # Respond to keyup releases
    if event.key == pygame.K_RIGHT:
        ship.moving_right = False
    if event.key == pygame.K_LEFT:
        ship.moving_left = False
        # if event.key == pygame.K_UP:
        ship.moving_up = False
        # if event.key == pygame.K_DOWN:
        ship.moving_down = False


def check_events(infrompy_settings, screen, stats, sb, play_button, ship, aliens, bullets):  # Refactoring part 1
    # Respond to key presses and mouse events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            check_keydown_events(event, infrompy_settings, screen, ship, bullets)
        elif event.type == pygame.KEYUP:
            check_keyup_events(event, ship)
        elif event.type == pygame.MOUSEBUTTONDOWN:
            mouse_x, mouse_y = pygame.mouse.get_pos()
            check_play_button(infrompy_settings, screen, stats, sb, play_button, ship, aliens, bullets, mouse_x, mouse_y)


def check_play_button(infrompy_settings, screen, stats, sb, play_button, ship, aliens, bullets, mouse_x, mouse_y):
    # Start new game when the play button is clicked
    button_clicked = play_button.rect.collidepoint(mouse_x, mouse_y)
    if button_clicked and not stats.game_active:
        # reset game settings
        infrompy_settings.initialize_dynamic_settings()

        # Hide mouse
        pygame.mouse.set_visible(False)

        # Reset the game stats
        stats.reset_stats()
        stats.game_active = True

        #Reset scoreboard images
        sb.prep_score()
        sb.prep_high_score()
        sb.prep_level()
        sb.prep_ships()

    # Empty the list of aliens and bullets
    aliens.empty()
    bullets.empty()

    # Create a new fleet and center the shi[
    create_fleet(infrompy_settings, screen, ship, aliens)
    ship.center_ship()


def update_screen(infrompy_settings, screen, stats, sb, ship, aliens, bullets, play_button):
    # Redraw the screen during each pass through the loop.
    screen.fill(infrompy_settings.bg_colour)

    # Redraw all bullets behind the ship and aliens.
    for bullet in bullets.sprites():
        bullet.draw_bullet()
    ship.blitme()
    aliens.draw(screen)

    # Draw the score info
    sb.show_score()

    # Draw the play button if the game is inactive
    if not stats.game_active:
        play_button.draw_button()

    # Make the most recently drawn screen visible.
    pygame.display.flip()


def update_bullets(infrompy_settings, screen, stats, sb, ship, aliens, bullets):
    # Update position of bullets and remove old bullets

    bullets.update()

    # remove bullets that have left the game screen
    # Remove bullets that go off screen
    for bullet in bullets.copy():  # 'copy' method allows modification of original list
        if bullet.rect.bottom <= 0:
            bullets.remove(bullet)

    check_bullet_alien_collisions(infrompy_settings, screen, stats, sb, ship, aliens, bullets)


def check_bullet_alien_collisions(infrompy_settings, screen, stats, sb, ship, aliens, bullets):
    # Respond to alien bullet collisions
    # Remove any bullets and aliens that have collided

    collisions = pygame.sprite.groupcollide(bullets, aliens, True, True)
    for aliens in collisions.values():
        stats.score += infrompy_settings.alien_points * len(aliens)
        sb.prep_score()

    check_high_score(stats, sb)

    if len(aliens) == 0:
        # Destroy existing bullets, speed up and create new fleet
        bullets.empty()
        infrompy_settings.increase_speed()

        #Increase level
        stats.level += 1
        sb.prep_level()

        create_fleet(infrompy_settings, screen, ship, aliens)


def create_fleet(infrompy_settings, screen, ship, aliens):
    # Create a fleet of aliens
    # Create an alien and find number of aliens in a row

    alien = Alien(infrompy_settings, screen)
    number_of_aliens_x = get_number_alienx_x(infrompy_settings, alien.rect.width)
    number_rows = get_number_of_rows(infrompy_settings, ship.rect.height, alien.rect.height)

    # Create fleet of aliens
    for row_number in range(number_rows):
        for alien_number in range(number_of_aliens_x):
            create_alien(infrompy_settings, screen, aliens, alien_number, row_number)


def get_number_alienx_x(infrompy_settings, alien_width):
    # How many aliens will fit in a row
    available_space_x = infrompy_settings.screen_width - 2 * alien_width
    number_of_aliens_x = int(available_space_x / (2 * alien_width))
    return number_of_aliens_x


def create_alien(infrompy_settings, screen, aliens, alien_number, row_number):
    # Create an alien and place it in a row
    alien = Alien(infrompy_settings, screen)
    alien_width = alien.rect.width
    alien.x = alien_width + 2 * alien_width * alien_number
    alien.rect.x = alien.x
    alien.rect.y = alien.rect.height + 2 * alien.rect.height * row_number
    aliens.add(alien)


def get_number_of_rows(infrompy_settings, ship_height, alien_height):
    # Determine the number of rows of aliens that fit on the screen
    available_space_y = (infrompy_settings.screen_height - (3 * alien_height) - ship_height)
    number_rows = int(available_space_y / (2 * alien_height))
    return number_rows


def check_fleet_edges(infrompy_settings, aliens):
    # Respond if alien reaches edge of screen
    for alien in aliens.sprites():
        if alien.check_edges():
            change_fleet_direction(infrompy_settings, aliens)
            break


def change_fleet_direction(infrompy_settings, aliens):
    for alien in aliens.sprites():
        alien.rect.y += infrompy_settings.fleet_drop_speed
    infrompy_settings.fleet_direction *= -1


def check_aliens_bottom(infrompy_settings, screen, stats, sb, ship, aliens, bullets):
    # check if aliens have reached bottom of the screen
    screen_rect = screen.get_rect()
    for alien in aliens.sprites():
        if alien.rect.bottom >= screen_rect.bottom:
            # treat this same if ship got hit
            ship_hit(infrompy_settings, screen, stats, sb, ship, aliens, bullets)
            break


def update_aliens(informpy_settings, screen, stats, sb, ship, aliens, bullets):
    # check if the fleet has reached the edge and then update the positions of all aliens
    check_fleet_edges(informpy_settings, aliens)
    aliens.update()

    # look for alien-ship collisions
    if pygame.sprite.spritecollideany(ship, aliens):
        ship_hit(informpy_settings, screen, stats, sb, ship, aliens, bullets)

    # look for aliens hitting the bottom of the screen
    check_aliens_bottom(informpy_settings, screen, stats, sb, ship, aliens, bullets)


def check_high_score(stats, sb):
    #Check to see if there is new high score
    if stats.score > stats.high_score:
        stats.high_score = stats.score
        sb.prep_high_score()