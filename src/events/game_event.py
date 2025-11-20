from enum import Enum, auto

class GameEvent(Enum):
    ENEMY_KILLED = "enemy_killed"
    ENEMY_REACHED_END = "enemy_reached_end"
    TOWER_BUILT = "tower_built"
    MONEY_CHANGED = "money_changed"
    ENEMY_SPAWNED = "enemy_spawned"