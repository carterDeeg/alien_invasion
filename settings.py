import pygame


class Settings():
    """A class to store all settings for alien invasion"""

    def __init__(self):
        """ initialize game's settings"""

        # screen settings
        self.bg_color = (230, 230, 230)
        self.screen_width = 800
        self.screen_height = 600

        # bullet settings
        self.bullet_speed = 1
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = (255, 0, 0)

        # player settings
        self.lives = 3
        self.score = 0

        # set font
        self.font = pygame.font.Font('freesansbold.ttf', 32)
        # create a text surface object, on which text is drawn on it.
        self.text = self.font.render('Score: ' + str(self.score), True, (0, 255, 0), (0, 0, 255))
        # create a rectangular object for the text surface object
        self.text_Rect = self.text.get_rect()
        # set the center of the rectangular object.
        self.text_Rect.center = (self.screen_width/ 2, 35)


