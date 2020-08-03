import pygame

import sys

def run_game():
    #Initialise game and create a screen object
    pygame.init()
    screen = pygame.display.set_mode((1200, 800))
    pygame.display.set_caption("Invaders from Python")

    #set background colour
    bg_colour = (135, 206, 250)

    #Start main loop of game

    while True:

        #Watch for keyboard and mouse events:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()

        #redraw the screen during each pass through the loop
        screen.fill(bg_colour)

        #make the most recently drawn screen visable
        pygame.display.flip()

run_game()
