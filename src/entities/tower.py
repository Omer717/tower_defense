import pygame

from entities.bullet import Bullet

class Tower:
    def __init__(self, tile_x, tile_y, range=100, damage=10, fire_rate=1):
        self.tile_x = tile_x
        self.tile_y = tile_y
        self.pixel_x = tile_x * 32
        self.pixel_y = tile_y * 32
        self.range = range
        self.damage = damage
        self.fire_rate = fire_rate
        self.cooldown = 0

    def update(self, dt, enemies, bullets):
        # Reduce cooldown timer
        if self.cooldown > 0:
            self.cooldown -= dt

        # Can shoot?
        if self.cooldown <= 0:
            target = self.get_target(enemies)
            if target:
                # Fire bullet
                bullets.append(Bullet((self.pixel_x, self.pixel_y), target))
                self.cooldown = 1 / self.fire_rate

    def get_target(self, enemies):
        # Simple nearest target in range
        for enemy in enemies:
            dist = ((enemy.pixel_x - self.pixel_x) ** 2 +
                    (enemy.pixel_y - self.pixel_y) ** 2) ** 0.5
            if dist <= self.range:
                return enemy
        return None
    
    def draw(self, screen, is_selected=False):
        color = (150, 150, 220)
        if is_selected:
            color = (255, 215, 0)  # Gold for selected tower
            self.draw_range(screen)

        pygame.draw.rect(
            screen,
            color,
            (self.pixel_x, self.pixel_y, 32, 32)
        )

    def draw_range(self, screen):
        pygame.draw.circle(
            screen,
            (150, 150, 150),
            (self.pixel_x + 16, self.pixel_y + 16),
            self.range,
            width=1
        )