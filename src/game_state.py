class GameState:
    def __init__(self):
        self.hovered_tower = None
        self.selected_tower = None
        self.selected_tile = None

    def set_hovered_tower(self, tower):
        self.hovered_tower = tower

    def set_selected_tower(self, tower):
        self.selected_tower = tower

    def set_selected_tile(self, tile):
        self.selected_tile = tile 