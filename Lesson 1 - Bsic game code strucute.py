import pygame

import sys

def run_game():
    #Initialise game and create a screen object
    pygame.init()
    screen = pygame.display.set_mode((1200, 800))
    pygame.display.set_caption("Invaders from Python")

    #Start main loop of game

    while True:

        #Watch for keyboard and mouse events:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()

        #make the most recently drawn screen visable
        pygame.display.flip()

run_game()
