import pygame
from ship import Ship
from settings import Settings
import game_functions as gf



def alien_invasion():
    # initialize pygame library
    pygame.init()
    # define settings as settings class
    settings = Settings()

    # create display
    screen = pygame.display.set_mode((settings.screen_width, settings.screen_height))
    pygame.display.set_caption('Alien Invasion')

    # define ship as ship class
    ship = Ship(screen)

    # initialize main game loop
    while True:

        gf.check_events(ship)
        gf.update_screen(settings, screen, ship)


    while True:

        #gf.check_events(settings,)










alien_invasion()