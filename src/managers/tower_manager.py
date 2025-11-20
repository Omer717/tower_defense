from entities.tower import Tower
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from game_state import GameState  # imported only for type checking


class TowerManager:
    def __init__(self, game_state: "GameState"):
        self.towers = []
        self.game_state = game_state

    def add_tower_at(self, tile):
        self.towers.append(Tower(tile[0], tile[1]))

    def update_towers(self):
        for tower in self.towers:
            tower.update(self.game_state.enemy_manager.enemies)

    def draw_towers(self, screen, selected_tower=None):
        for tower in self.towers:
            tower.draw(screen, is_selected=(tower == selected_tower))

    def is_tower_at(self, tile):
        for tower in self.towers:
            if (tower.tile_x, tower.tile_y) == tile:
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

    def can_place_tower(self, tile):
        if self.is_tower_at(tile):
            return False

        if self.game_state.path.is_tile_on_path(tile[0], tile[1]):
            return False

        return True
