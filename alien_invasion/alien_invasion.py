import pygame
from pygame.sprite import Group

from settings import Settings
from ship import Ship
import game_functions as gf
from game_stats import GameStats
from button import Button

def run_game():
    #Initialize pygame, settings and screen object
    pygame.init()
    ai_sets = Settings()
    screen = pygame.display.set_mode(
        (ai_sets.screen_width, ai_sets.screen_height))
    pygame.display.set_caption("Alien Invasion")

    # Make the Play button.
    play_button = Button(ai_sets, screen, "Play")

    # Create an instance to store game statistics.
    stats = GameStats(ai_sets)

    # Make our ship
    ship = Ship(ai_sets, screen)

    # Make an alien
    aliens = Group()

    # Make a group to store bullets in.
    bullets = Group()
    
    # Create the fleet of aliens.
    gf.create_fleet(ai_sets, screen, ship, aliens)
    
    #start the main loop for the game
    while True:
        # Watch for keyboard and mouse events.
        gf.check_events(ai_sets, screen, stats, play_button, ship, bullets)
        if stats.game_active:
            
            ship.update()

            gf.update_bullets(ai_sets, screen, ship, aliens, bullets)
            gf.update_aliens(ai_sets, stats, screen, ship, aliens, bullets)

        # Redraw the screen and ship during each pass through loop
        # Make the most recently drawn screen visible.
        gf.update_screen(ai_sets, screen, stats, ship, aliens, bullets, play_button)
        

run_game()
