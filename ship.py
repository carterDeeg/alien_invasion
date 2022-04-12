import pygame

class Ship():

    def __init__(self, screen):
        self.screen = screen

        # load image of ship and access
        self.image = pygame.image.load('images/pngaaa.com-3547629.png')
        self.image = pygame.transform.scale(self.image, (50, 75))
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()
        #set starting location os each ship
        #makes the center x value of the ship the same as the center x value of the screen
        self.rect.centerx = self.screen_rect.centerx
        #makes the bottom of the ship the same as the bottom of the screen
        self.rect.bottom = self.screen_rect.bottom

        self.moving_right = False
        self.moving_left = False

        self.available_space_x = self.settings.screen_width - (2 * self.rect.width))
        self.number

    def blitme(self):
        """draw the ship on the screen"""
        self.screen.blit(self.image, self.rect)

    def update(self):
        if self.moving_right == True:
            self.rect.centerx += 1
        if self.moving_left:
            self.rect.centerx -= 1