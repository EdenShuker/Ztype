import pygame
from config import FONT_SIZE, FONT_COLOR


class Word(pygame.sprite.Sprite):
    """
    Word rectangle in game.
    """

    def __init__(self, word_str, speed, *groups):
        """
        Constructor.
        :param word_str: word string.
        :param speed: speed of falling down the screen.
        :param groups: groups to add this word to.
        """
        super(Word, self).__init__(*groups)
        self.letters = [letter for letter in word_str]
        self.speed = speed
        self.font = pygame.font.Font(None, FONT_SIZE)
        self.image = self.font.render(word_str, True, FONT_COLOR)
        self.rect = self.image.get_rect()

    def update(self, *args):
        """
        Move word's rectangle.
        :param args: None.
        """
        self.rect.move_ip(self.speed)
        print self.rect
