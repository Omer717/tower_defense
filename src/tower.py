import pygame

class Tower:
    def __init__(self, tile_x, tile_y):
        self.tile_x = tile_x
        self.tile_y = tile_y
        self.pos_x = tile_x * 32
        self.pos_y = tile_y * 32

    def update(self, enemies):
        # TODO: target enemy
        pass

    def draw(self, screen):
        pygame.draw.rect(
            screen,
            (100, 150, 220),
            (self.pos_x, self.pos_y, 32, 32)
        )
