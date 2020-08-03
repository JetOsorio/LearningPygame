import pygame

import sys

from setting import settings

from ship import Ship

import game_functions as gf

from alien import Alien

from pygame.sprite import Group


def run_game():
    # Initialise game and create a screen object
    pygame.init()
    informpy_settings = settings()
    screen = pygame.display.set_mode((informpy_settings.screen_width, informpy_settings.screen_height))
    pygame.display.set_caption("Invaders from Python")

    #Make a ship, a group of bullets and a group of bullets
    ship = Ship(informpy_settings, screen)
    bullets = Group()
    aliens = Group()

    #Create a fleet of aliens
    gf.create_fleet(informpy_settings, screen, ship, aliens)

    # Start main loop of game
    while True:
        # Watch for keyboard and mouse events:
        gf.check_events(informpy_settings, screen, ship, bullets)  # Refactoring
        ship.update()
        gf.update_bullets(informpy_settings, screen, ship, aliens,  bullets)
        gf.update_aliens(informpy_settings, ship, aliens)
        # print(len(bullets)) #Shows that bullets are actually removed

        gf.update_screen(informpy_settings, screen, ship, aliens,bullets)


run_game()
