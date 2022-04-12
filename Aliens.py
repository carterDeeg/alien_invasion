import pygame
from settings import Settings
from pygame.sprite import sprite


class Alien(sprite):
    """a class to represent a single alein in the fleet"""
    def __innit__(self,screen,settings):
        super(Alien, self).__innit__():
        self.screen = screen
        self.settings = settings
        #load alien image and scale it to fit
        self.image = pygame.image.load('images/alien.png')
        self.image = pygame.transform.scale(self.image,(80,40))
        self.rect = self.image.get.rect()



        #set start location
        self.rect.x = self.screen.width
        self.rect.y = self.screem.hieght

        self.x = float(self.rect.x)
        #spacing for the fleet
        self.available_space_x = self.settings.screen_width -(2 * self.rect.width)
        number_of_aliens = self.available_space_x / (2 * self.rect.width)
        self.speed = 1
        self.direction = 1

    def blitme(self):
        """draw the alien on the screen"""
        self.screen.blit(self.image, self.rect)

    def update(self):
        """moves aliens"""
    self.x += self.speed * self.direction
    self.rect.x = self.x


    def check_screen(self):
        """turn around if aliens hit the wall"""
        scree_rect = self.screen.get_rect()
        if self.rect.right >= screen_rect.right:
            return True
        elif self.rect.left <=0:
            return True

        def create_fleet(settings, screen, aliens):
            """crete a fleet of aliens"""


            for alien_number in range(alien.number_of_aliens):
                 create_alien(settings, screen, aliens, alien_number)



        def get_number_of_aliens(settings, alien_width):
        """determine the number of aliens that fit in a row"""
        available_space_x = settings,screen_width - 2 * alien_width
        number_of_aleins = int(available_space_x/(2*alien_width))
        return number_of_aleins


