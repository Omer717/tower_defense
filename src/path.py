import pygame
from settings import *

class Path:
    def __init__(self, tile_path):
        self.tile_path = tile_path
        self.pixel_path = self.tiles_to_pixel_centers(tile_path)

    @staticmethod
    def tiles_to_pixel_centers(tiles):
        """
        Convert a list of (col,row) tiles into pixel center coordinates
        """
        return [(x * TILE_SIZE + TILE_SIZE // 2, y * TILE_SIZE + TILE_SIZE // 2) for x, y in tiles]

    def draw(self, screen):
        for tile in self.tile_path:
            x, y = tile
            rect = pygame.Rect(x * TILE_SIZE, y * TILE_SIZE, TILE_SIZE, TILE_SIZE)
            pygame.draw.rect(screen, COLOR_PATH, rect)
    def is_tile_on_path(self, grid_x, grid_y):
        return (grid_x, grid_y) in self.tile_path