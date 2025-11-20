import pygame
from entities.bullet import Bullet
from settings import TILE_SIZE

class Tower:
    def __init__(self, tile_x, tile_y, range=100, damage=10, fire_rate=1, bullet_speed=200):
        self.tile_x = tile_x
        self.tile_y = tile_y
        # Position as Vector2 at center of the tile
        self.position = pygame.math.Vector2(
            tile_x * TILE_SIZE + TILE_SIZE / 2,
            tile_y * TILE_SIZE + TILE_SIZE / 2
        )
        self.range = range
        self.damage = damage
        self.bullet_speed = bullet_speed
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
                # Fire bullet from tower position
                bullets.append(Bullet(self.position, target, self.bullet_speed, self.damage))
                self.cooldown = 1 / self.fire_rate

    def get_target(self, enemies):
        # Simple nearest target in range
        for enemy in enemies:
            dist = (enemy.position - self.position).length()
            if dist <= self.range:
                return enemy
        return None
    
    def draw(self, screen, is_selected=False):
        color = (150, 150, 220)
        if is_selected:
            color = (255, 215, 0)  # Gold for selected tower
            self.draw_range(screen)

        # Draw rectangle centered at tile
        rect = pygame.Rect(
            self.position.x - TILE_SIZE / 2,
            self.position.y - TILE_SIZE / 2,
            TILE_SIZE,
            TILE_SIZE
        )
        pygame.draw.rect(screen, color, rect)

    def draw_range(self, screen):
        pygame.draw.circle(
            screen,
            (150, 150, 150),
            (int(self.position.x), int(self.position.y)),
            self.range,
            width=1
        )
