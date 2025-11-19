import pygame


class Player:
    def __init__(self, name):
        self.name = name
        self.health = 100
        self.money = 50

        pygame.font.init() # Initialize the font module

        # Create a Font object (using default system font, size 30)
        self.font = pygame.font.SysFont(None, 30)

    def draw(self, screen):
        text_surface = self.font.render(f"{self.name} - Health: {self.health} Money: {self.money}", True, (255, 255, 255))
        screen.blit(text_surface, (10, 10))

    def is_alive(self):
        return self.health > 0
    
    def take_damage(self, amount):
        self.health -= amount
        if self.health < 0:
            self.health = 0

    def earn_money(self, amount):
        self.money += amount

    def spend_money(self, amount):
        if amount <= self.money:
            self.money -= amount
            return True
        return False