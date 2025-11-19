import pygame
from helpers import PointerMode, can_place_tower
from settings import TILE_SIZE


class Pointer:
    def __init__(self, grid, path, tower_manager):
        self.grid = grid
        self.path = path
        self.tower_manager = tower_manager

        self.mouse_pos = (0, 0)
        self.tile_pos = (0, 0)
        self.state = PointerMode.SELECT

    def update(self):
        self.mouse_pos = pygame.mouse.get_pos()
        self.tile_pos = (self.mouse_pos[0] // TILE_SIZE, self.mouse_pos[1] // TILE_SIZE)

    def draw(self, screen):
        color = (255, 255, 255)
        if self.state == PointerMode.PLACE_TOWER:
            color = (255, 0, 0)
            if can_place_tower(self.grid, self.tile_pos[0], self.tile_pos[1], self.path.tile_path):
                color = (0, 255, 0)

        if self.state == PointerMode.SELECT:
            if self.path.is_tile_on_path(self.tile_pos[0], self.tile_pos[1]):
                return
            
        pygame.draw.rect(screen, color,
                         (self.tile_pos[0] * TILE_SIZE, self.tile_pos[1] * TILE_SIZE, TILE_SIZE, TILE_SIZE), 2)