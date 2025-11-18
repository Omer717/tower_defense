import pygame
from settings import *

class Grid:
    def __init__(self, rows, cols, tile_size):
        self.rows = rows
        self.cols = cols
        self.tile_size = tile_size

    def draw(self, screen):
        for r in range(self.rows):
            for c in range(self.cols):
                rect = pygame.Rect(
                    c * self.tile_size, r * self.tile_size,
                    self.tile_size, self.tile_size
                )
                pygame.draw.rect(screen, COLOR_GRID, rect, width=1)
