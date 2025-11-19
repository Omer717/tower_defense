import pygame

class Tower:
    def __init__(self, tile_x, tile_y, range=100, damage=10, fire_rate=1):
        self.tile_x = tile_x
        self.tile_y = tile_y
        self.grid_x = tile_x * 32
        self.grid_y = tile_y * 32
        self.range = range
        self.damage = damage
        self.fire_rate = fire_rate
        self.time_since_last_shot = 0

    def update(self, enemies):
        # TODO: target enemy
        pass

    def draw(self, screen, is_selected=False):
        color = (150, 150, 220)
        if is_selected:
            color = (255, 215, 0)  # Gold for selected tower
            self.draw_range(screen)

        pygame.draw.rect(
            screen,
            color,
            (self.grid_x, self.grid_y, 32, 32)
        )

    def draw_range(self, screen):
        pygame.draw.circle(
            screen,
            (150, 150, 150),
            (self.grid_x + 16, self.grid_y + 16),
            self.range,
            width=1
        )