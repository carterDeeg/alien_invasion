import pygame
from pygame.sprite import Sprite


class Bulllets(Sprite):

    def __init__(self, screen, ship):
        super(Bullets, self).__init__()
        self.screen = screen

        self.rect = pygame.Rect(0, 0, 3, 15)
        self.rect.centerx = ship.rect.centerx
        self.rect.top = ship.rect.top

        self.y = float(self.rect.y)

        self.color = (255,0,0)
        self.speed = 1

    def update(self):
        self.y -= self.speed
        self.rect.y = self.y

    def draw_bullet(self):
        """draw bullet to screem"""
        pygame.draw.rect(self.screen, self.color, self.rect)
