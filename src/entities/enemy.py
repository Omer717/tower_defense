import pygame
from settings import *
from wave_generation.enemy_type import EnemyType

class Enemy:
    def __init__(self, pixel_path, type, speed, health, reward, damage):
        # Convert path points to Vector2
        self.pixel_path = [pygame.math.Vector2(p) for p in pixel_path]
        self.speed = speed
        self.max_health = health
        self.health = health
        self.reward = reward
        self.damage = damage
        self.path_index = 0

        # Use Vector2 for position
        self.position = self.pixel_path[0].copy()

        if type == EnemyType.EASY:
            self.color = (0, 200, 0)  # green
        elif type == EnemyType.REGULAR:
            self.color = (255, 165, 0)  # orange
        elif type == EnemyType.HEAVY:
            self.color = (200, 0, 0)    # red

    def update(self, dt):
        if self.reached_end():
            return  # already reached the end

        target = self.pixel_path[self.path_index]
        direction = target - self.position
        distance = direction.length()

        if distance == 0:
            self.path_index += 1
            return

        direction = direction.normalize()
        move_dist = self.speed * dt
        self.position += direction * move_dist

        # Snap to target if we overshoot
        if distance <= move_dist:
            self.position = target.copy()
            self.path_index += 1

    def draw(self, screen):
        # --- Draw enemy body ---
        pygame.draw.circle(screen, self.color, self.position, 10)

        # --- Draw health bar ---
        bar_width = 20
        bar_height = 4
        bar_x = self.position.x - bar_width / 2
        bar_y = self.position.y - 16  # slightly above the enemy

        # Health percentage
        health_ratio = max(self.health / self.max_health, 0)

        # Color gradient: green → yellow → red
        if health_ratio > 0.6:
            bar_color = (0, 255, 0)  # green
        elif health_ratio > 0.3:
            bar_color = (255, 255, 0)  # yellow
        else:
            bar_color = (255, 0, 0)  # red

        # Background (gray)
        pygame.draw.rect(screen, (50, 50, 50), (bar_x, bar_y, bar_width, bar_height))
        # Foreground (current health)
        pygame.draw.rect(screen, bar_color, (bar_x, bar_y, bar_width * health_ratio, bar_height))

    def is_alive(self):
        return self.health > 0

    def reached_end(self):
        return self.path_index >= len(self.pixel_path)

    def take_damage(self, damage):
        self.health -= damage
