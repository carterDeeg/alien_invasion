import pygame
import sys
from bullets import Bullets
from Aliens import Alien
from settings import Settings


def check_events(settings, screen, ship, bullets):
    """ checks for key/mouse events and responds"""
    # loop to check keypress events
    for event in pygame.event.get():
        # if escape key pressed, exit game
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            keydown_event(event, settings, screen, ship, bullets)

        elif event.type == pygame.KEYUP:
            keyup_event(event, ship)


def keydown_event(event, settings, screen, ship, bullets):
    if event.key == pygame.K_RIGHT or event.key == pygame.K_d:
        ship.moving_right = True
    if event.key == pygame.K_LEFT or event.key == pygame.K_a:
        ship.moving_left = True
    if event.key == pygame.K_UP or event.key == pygame.K_w:
        ship.moving_up = True
    if event.key == pygame.K_DOWN or event.key == pygame.K_s:
        ship.moving_down = True
    if event.key == pygame.K_SPACE:
        new_bullet = Bullets(settings, screen, ship)
        bullets.add(new_bullet)


def keyup_event(event, ship):
    if event.key == pygame.K_RIGHT or event.key == pygame.K_d:
        ship.moving_right = False
    if event.key == pygame.K_LEFT or event.key == pygame.K_a:
        ship.moving_left = False
    if event.key == pygame.K_UP or event.key == pygame.K_w:
        ship.moving_up = False
    if event.key == pygame.K_DOWN or event.key == pygame.K_s:
        ship.moving_down = False
    if event.key == pygame.K_q:
        ship.rotate_counterclockwise = False
    if event.key == pygame.K_e:
        ship.rotate_clockwise = False


def create_fleet(settings, screen, ship, aliens):
    """create a fleet of aliens"""
    alien = Alien(settings, screen)
    number_of_aliens = get_number_of_aliens(settings, alien.rect.width)
    number_of_rows = get_number_rows(settings, alien.rect.height, ship.rect.height)

    for row_number in range(number_of_rows):
        for alien_number in range(number_of_aliens):
            create_alien(settings, screen, aliens, alien_number, row_number)


def get_number_of_aliens(settings, alien_width):
    """Determine the number of aliens that fit in a row"""
    available_space_x = settings.screen_width - 2 * alien_width
    number_of_aliens = int(available_space_x/(2*alien_width))
    return number_of_aliens


def get_number_rows(settings, alien_height, ship_height):
    available_space_y = settings.screen_height - 3 * alien_height - ship_height
    number_of_rows = int(available_space_y/(2*alien_height))
    return number_of_rows


def create_alien(settings, screen, aliens, alien_number, row_number):
    """Create and alien and place it on a row"""
    alien = Alien(settings, screen)
    alien_width = alien.rect.width
    alien.x = 2 * alien_width * alien_number
    alien.rect.x = alien.x

    alien.rect.y = alien.rect.height + 2 * alien.rect.height * row_number

    aliens.add(alien)

def update_aliens(settings, screen, ship, aliens, bullets):

    # draw fleet of aliens
    aliens.draw(screen)
    aliens.update()

    for alien in aliens:
        if alien.check_screen():
            update_fleet(aliens)
            break


def update_fleet(aliens):
    for alien in aliens:
        alien.direction = alien.direction * -1
        alien.rect.y += alien.drop



def check_collision(bullets, aliens, settings):
    if pygame.sprite.groupcollide(bullets, aliens, True, True):
        settings.score += 3
        print(settings.score)

def update_screen(settings, screen, ship, bullets, aliens):
        # color the screen with background color
        screen.fill(settings.bg_color)

        # draw new bullets on the screen; move bullets
        for bullet in bullets.sprites():
            bullet.draw_bullet()
            bullet.update()

        update_aliens(settings, screen, ship, aliens, bullets)

        # update the ship
        ship.update()
        # draw the ship on the screen
        ship.blitme()

        check_collision(bullets, aliens, settings)

        scoreboard(settings, screen)

        if len(aliens) == 0:
            create_fleet(settings, screen, ship, aliens)

        # update the display
        pygame.display.flip()


def scoreboard(settings, screen):
    # create a text surface object, on which text is drawn on it.
    text = settings.font.render('Score: ' + str(settings.score), True, (0, 255, 0), (0, 0, 255))
    # create a rectangular object for the text surface object
    text_Rect = text.get_rect()
    # set the center of the rectangular object.
    text_Rect.center = (settings.screen_width / 2, 35)

    screen.blit(settings.text, settings.text_Rect)
