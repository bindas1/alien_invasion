import pygame
from pygame.sprite import Group

def run_game():
    #Initialize pygame, settings and screen object
    pygame.init()

    screen = pygame.display.set_mode(
        (1024, 640))
    pygame.display.set_caption("Downpour")

    raindrops = Group()
    
