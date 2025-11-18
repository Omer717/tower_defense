import pygame

class Tower:
    def __init__(self, grid_x, grid_y):
        self.grid_x = grid_x
        self.grid_y = grid_y

    def update(self, enemies):
        # TODO: target enemy
        pass

    def draw(self, screen):
        pygame.draw.rect(
            screen,
            (100, 150, 220),
            (self.grid_x, self.grid_y, 32, 32)
        )
