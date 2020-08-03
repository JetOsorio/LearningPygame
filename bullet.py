import pygame
from pygame.sprite import Sprite

class Bullet(Sprite):
    #Class to manage bullets fired from space ship

    def __init__(self, infrompy_settings, screen, ship):
        #Create a bullet object at the ships position
        super(Bullet, self).__init__()
        self.screen = screen

        #Create a bullet rect at (0,0) and then set the correct position
        self.rect = pygame.Rect(0,0, infrompy_settings.bullet_width, infrompy_settings.bullet_height)
        self.rect.centerx = ship.rect.centerx
        self.rect.top = ship.rect.top

        #Store the bullet's position as a decimal value
        self.y = float(self.rect.y)

        self.colour = infrompy_settings.bullet_colour
        self.speed = infrompy_settings.bullet_speed

    def update(self):
        #Move bullet up the screen.
        #Update the decimal position of the bullets
        self.y -= self.speed
        #Update the rect position
        self.rect.y = self.y


    def draw_bullet(self):
        #Draw the bullet to the screen
        pygame.draw.rect(self.screen, self.colour, self.rect)