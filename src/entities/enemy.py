import pygame
from settings import *

class Enemy:
    def __init__(self, path, speed, health, reward, damage):
        self.path = path
        self.speed = speed
        self.health = health
        self.reward = reward
        self.damage = damage
        self.path_index = 0
        self.x, self.y = path[0]

    def update(self, dt):
        if self.path_index >= len(self.path):
            return  # already reached the end

        target = self.path[self.path_index]
        dir_x = target[0] - self.x
        dir_y = target[1] - self.y
        distance = (dir_x ** 2 + dir_y ** 2) ** 0.5

        if distance == 0:
            self.path_index += 1
            return

        # normalize direction
        dir_x /= distance
        dir_y /= distance

        # move
        move_dist = self.speed * dt
        self.x += dir_x * move_dist
        self.y += dir_y * move_dist

        # check if reached target point
        if distance <= move_dist:
            self.position = list(target)
            self.path_index += 1


    def draw(self, screen):
        pygame.draw.circle(screen, (200, 50, 50), (int(self.x), int(self.y)), 10)

    def reached_end(self):
        return self.path_index >= len(self.path)

