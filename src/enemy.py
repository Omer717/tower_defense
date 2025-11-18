import pygame
from settings import *
from path import PATH

class Enemy:
    def __init__(self, path):
        self.path = path
        self.speed = 5 * TILE_SIZE / FPS
        self.path_index = 0
        self.x, self.y = path[0]

    def update(self):
        if self.path_index + 1 < len(self.path):
            target_x, target_y = self.path[self.path_index + 1]

            # Compute direction
            dx = target_x - self.x
            dy = target_y - self.y
            distance = (dx**2 + dy**2)**0.5

            if distance != 0:
                # Move toward next point
                self.x += self.speed * dx / distance
                self.y += self.speed * dy / distance

            # Advance to next path point if reached
            if distance < self.speed:
                self.path_index += 1


    def draw(self, screen):
        pygame.draw.circle(screen, (200, 50, 50), (int(self.x), int(self.y)), 10)

    def is_alive(self):
        return self.path_index < len(self.path) - 1

