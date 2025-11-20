import pygame
from settings import *

class Enemy:
    def __init__(self, pixel_path, speed, health, reward, damage):
        # Convert path points to Vector2
        self.pixel_path = [pygame.math.Vector2(p) for p in pixel_path]
        self.speed = speed
        self.health = health
        self.reward = reward
        self.damage = damage
        self.path_index = 0

        # Use Vector2 for position
        self.position = self.pixel_path[0].copy()

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
        pygame.draw.circle(screen, (200, 50, 50),
                           (int(self.position.x), int(self.position.y)), 10)

    def is_alive(self):
        return self.health > 0

    def reached_end(self):
        return self.path_index >= len(self.pixel_path)

    def take_damage(self, damage):
        self.health -= damage
