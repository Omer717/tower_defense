from enemy_manager import EnemyManager
from events.game_event import GameEvent
from game_ui import GameUI
from grid import Grid
from path import Path
from pointer import Pointer
from settings import GRID_COLS, GRID_ROWS, PATH, TILE_SIZE
from tower_manager import TowerManager


class GameState:
    def __init__(self, event_bus):
        self.event_bus = event_bus

        self.health = 100
        self.money = 50
        self.wave = 1


        self.grid = Grid(GRID_ROWS, GRID_COLS, TILE_SIZE)
        self.path = Path(PATH)

        self.tower_manager = TowerManager(self)
        self.enemy_manager = EnemyManager(self, self.event_bus)

        self.pointer = Pointer(self)

        self.game_ui = GameUI(self)
        self.hovered_tower = None
        self.selected_tower = None
        self.selected_tile = None

        # Subscribe to events
        event_bus.subscribe(GameEvent.ENEMY_KILLED, self.on_enemy_killed)
        event_bus.subscribe(GameEvent.ENEMY_REACHED_END, self.on_enemy_reached_end)


    def on_enemy_killed(self, enemy):
        self.earn_money(enemy.reward)

    def on_enemy_reached_end(self, enemy):
        self.take_damage(enemy.damage)

    def set_hovered_tower(self, tower):
        self.hovered_tower = tower

    def set_selected_tower(self, tower):
        self.selected_tower = tower

    def set_selected_tile(self, tile):
        self.selected_tile = tile 

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