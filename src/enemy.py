import pygame
from settings import *
from path import PATH

class Enemy:
    def __init__(self):
        self.speed = 1
        self.path_index = 0
        self.x, self.y = PATH[0]

    def update(self):
        # TODO: move toward next path point
        pass

    def draw(self, screen):
        pygame.draw.circle(screen, (200, 50, 50), (int(self.x), int(self.y)), 10)
