class TowerManager:
    def __init__(self):
        self.towers = []

    def add_tower(self, tower):
        self.towers.append(tower)

    def update(self, enemies):
        for tower in self.towers:
            tower.update(enemies)

    def draw(self, screen):
        for tower in self.towers:
            tower.draw(screen)

    def is_tower_at(self, tile):
        for tower in self.towers:
            if (tower.grid_x, tower.grid_y) == tile:
                return True
        return False