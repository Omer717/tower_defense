import random
from entities.enemy import Enemy
from wave_generation.enemy_type import EnemyType

class EnemyFactory:
    @staticmethod
    def create(enemy_type, path):
        if enemy_type == EnemyType.EASY:
            return Enemy(path, enemy_type, speed=random.uniform(50, 70), health=random.randint(10, 30), reward=5, damage=1)
        elif enemy_type == EnemyType.REGULAR:
            return Enemy(path, enemy_type, speed=random.uniform(40, 60), health=random.randint(30, 50), reward=10, damage=2)
        elif enemy_type == EnemyType.HEAVY:
            return Enemy(path, enemy_type, speed=random.uniform(40, 60), health=random.randint(50, 80), reward=20, damage=10)

