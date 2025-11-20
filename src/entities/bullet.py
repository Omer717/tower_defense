import pygame
from pygame.math import Vector2

class Bullet:
    def __init__(self, start_pos, target_enemy, speed = 200, damage = 5):
        self.position = Vector2(start_pos)
        self.target = target_enemy
        self.speed = speed          # pixels per second
        self.damage = damage
        self.active = True


    def update(self, dt):
        if not self.active or not self.target.is_alive():
            self.active = False
            return

        direction = Vector2(Vector2(self.target.pixel_x, self.target.pixel_y)) - self.position
        distance = direction.length()

        if distance <= self.speed * dt:
            # Hit the target
            self.target.take_damage(self.damage)
            self.active = False
        else:
            direction = direction.normalize()
            self.position += direction * self.speed * dt


    def draw(self, screen):
        pygame.draw.circle(
        screen,
        (255, 255, 0),                      # bullet color (yellow)
        (int(self.position.x), int(self.position.y)),  # position as integers
        4                                   # radius in pixels
    )
