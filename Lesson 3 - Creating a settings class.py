import pygame

import sys

from setting import settings

def run_game():
    #Initialise game and create a screen object
    pygame.init()
    imformpy_settings = settings()
    screen = pygame.display.set_mode((imformpy_settings.screen_width, imformpy_settings.screen_height))
    pygame.display.set_caption("Invaders from Python")

    #Start main loop of game
    while True:

        #Watch for keyboard and mouse events:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()

        #redraw the screen during each pass through the loop
        screen.fill(imformpy_settings.bg_colour)

        #make the most recently drawn screen visable
        pygame.display.flip()

run_game()
