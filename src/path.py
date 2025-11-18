import pygame
from settings import *

class Path:
    def __init__(self, tile_path):
        self.tile_path = tile_path

    def draw(self, screen):
        for tile in self.tile_path:
            x, y = tile
            rect = pygame.Rect(x * TILE_SIZE, y * TILE_SIZE, TILE_SIZE, TILE_SIZE)
            pygame.draw.rect(screen, COLOR_PATH, rect)
