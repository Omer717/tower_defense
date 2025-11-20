import pygame
from helpers import PointerMode, can_place_tower
from settings import TILE_SIZE


class Pointer:
    def __init__(self, game_state):
        self.grid = game_state.grid
        self.path = game_state.path
        self.game_state = game_state

        self.mouse_pos = (0, 0)
        self.tile_pos = (0, 0)
        self.mode = PointerMode.SELECT

    def update(self):
        self.mouse_pos = pygame.mouse.get_pos()
        self.tile_pos = (self.mouse_pos[0] // TILE_SIZE, self.mouse_pos[1] // TILE_SIZE)

    def draw(self, screen):
        color = (255, 255, 255)
        if self.mode == PointerMode.PLACE_TOWER:
            color = (255, 0, 0)
            if can_place_tower(self.grid, self.tile_pos[0], self.tile_pos[1], self.path.tile_path, self.game_state.tower_manager.towers):
                color = (0, 255, 0)

        if self.mode == PointerMode.SELECT:
            if self.path.is_tile_on_path(self.tile_pos[0], self.tile_pos[1]):
                return
            
        pygame.draw.rect(screen, color,
                         (self.tile_pos[0] * TILE_SIZE, self.tile_pos[1] * TILE_SIZE, TILE_SIZE, TILE_SIZE), 2)
        
    def set_mode(self, mode):
        self.mode = mode

    def get_mode(self):
        return self.mode
    
    def get_mouse_pos(self):
        return self.mouse_pos
    
    def get_tile_pos(self):
        return self.tile_pos