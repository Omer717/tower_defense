class TowerManager:
    def __init__(self):
        self.towers = []

    def add_tower(self, tower):
        self.towers.append(tower)

    def update(self, enemies):
        for tower in self.towers:
            tower.update(enemies)

    def draw(self, screen, selected_tower=None):
        for tower in self.towers:
            tower.draw(screen, is_selected=(tower == selected_tower))

    def is_tower_at(self, tile):
        for tower in self.towers:
            if (tower.grid_x, tower.grid_y) == tile:
                return True
        return False
    
    def get_tower_at(self, tile):
        for tower in self.towers:
            if (tower.tile_x, tower.tile_y) == tile:
                return tower
        return None
    
    def deselect_all(self):
        for tower in self.towers:
            tower.set_selected(False)