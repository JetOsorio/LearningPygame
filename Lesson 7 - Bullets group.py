import pygame

import sys

from setting import settings

from ship import Ship

import game_functions as gf

from pygame.sprite import Group


def run_game():
    # Initialise game and create a screen object
    pygame.init()
    informpy_settings = settings()
    screen = pygame.display.set_mode((informpy_settings.screen_width, informpy_settings.screen_height))
    pygame.display.set_caption("Invaders from Python")

    # Create a ship
    ship = Ship(informpy_settings, screen)

    #Make a group to store bullets in
    bullets = Group()

    # Start main loop of game
    while True:
        # Watch for keyboard and mouse events:
        gf.check_events(informpy_settings, screen, ship, bullets)  # Refactoring
        ship.update()
        gf.update_bullets(bullets)

        # print(len(bullets)) #Shows that bullets are actually removed

        gf.update_screen(informpy_settings, screen, ship, bullets)


run_game()
