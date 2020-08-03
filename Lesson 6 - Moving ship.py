import pygame

import sys

from setting import settings

from ship import Ship

import game_functions as gf


def run_game():
    # Initialise game and create a screen object
    pygame.init()
    informpy_settings = settings()
    screen = pygame.display.set_mode((informpy_settings.screen_width, informpy_settings.screen_height))
    pygame.display.set_caption("Invaders from Python")

    # Create a ship
    ship = Ship(informpy_settings, screen)

    # Start main loop of game
    while True:
        # Watch for keyboard and mouse events:
        gf.check_events(ship)  # Refactoring
        ship.update()
        gf.update_screen(informpy_settings, screen, ship)


run_game()
