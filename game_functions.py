import pygame
import sys
from Aliens import Alien


def check_events(ship):
    """ checks for key/mouse events and respond"""
    # loop to check keypress, exit game
    for event in pygame.event.get():
        #if escape keypresed, exit game
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            keydown(event)
        if event.type == pygame.KEYUP:
            keyup(event)


def keyup(event):
    if event.key == pygame.K_RIGHT:
        ship.moving_right = False
    if event.key == pygame.K_LEFT:
        ship.moving_left = False


def keydown(event):
    if event.key == pygame.K_RIGHT:
        ship.moving_right = True
    if event.key == pygame.K_LEFT:
        ship.moving_left = True


def update_screen(settings, screen, ship, bullets, alien):
    #color the screen with background color
    aliens.draw(screen)
    screen.fill(settings.bg_color)
    #update the ship
    ship.update()
    #draw the ship on the screen
    ship.blitme()
    #update the display
    pygame.display.flip()


def create_feet(settings,screen, ship, aliens):
    """create a fleet of aliens"""
    alien = Alien(settings, screen)
    number_of_aliens = get_number_of_aliens(settings,alien.rect.width)
    number_of_rows = get_number_of_rows((settings, alien.rect.height, ship.rect.height))


    for row_number in range(number_of_rows):
        for alien_number in range(number_of_aliens):
            create_alien(settings, screen, alien_width)

    for alien_number in range(alien.number_of_aleins):
        alien.x = 2 * alien_width * alien_number
        alien.rect,x = alien.x
        aliens



def check_collosion(bullets, aliens):
    pygame.sprite.groupcollide(bullets,aliens,True, True)




def get_number_of_rows(settings, alien_height, ship_height):
    available_space_y = settings.screen_height - 3 * alien_height - ship_height
    number_of_rows = int(available_space_y/(2*alien_height))
    return number_of_rows



def create_alien(settings, screen, aliens, alien_number, row_number):
    """create aliens and place it on a row"""
    alien = Alien(settings, screen)