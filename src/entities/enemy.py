import pygame
from settings import *

class Enemy:
    def __init__(self, pixel_path, speed, health, reward, damage):
        self.pixel_path = pixel_path
        self.speed = speed
        self.health = health
        self.reward = reward
        self.damage = damage
        self.path_index = 0
        self.pixel_x, self.pixel_y = pixel_path[0]

    def update(self, dt):
        if self.reached_end():
            return  # already reached the end

        target = self.pixel_path[self.path_index]
        dir_x = target[0] - self.pixel_x
        dir_y = target[1] - self.pixel_y
        distance = (dir_x ** 2 + dir_y ** 2) ** 0.5

        if distance == 0:
            self.path_index += 1
            return

        # normalize direction
        dir_x /= distance
        dir_y /= distance

        # move
        move_dist = self.speed * dt
        self.pixel_x += dir_x * move_dist
        self.pixel_y += dir_y * move_dist

        # check if reached target point
        if distance <= move_dist:
            self.pixel_x, self.pixel_y = list(target)
            self.path_index += 1


    def draw(self, screen):
        pygame.draw.circle(screen, (200, 50, 50), (int(self.pixel_x), int(self.pixel_y)), 10)

    def reached_end(self):
        return self.path_index >= len(self.pixel_path)

