from enum import Enum


class ScreenState(Enum):
    MAIN_MENU = "main_menu"
    GAME_RUNNING = "game_running"
    GAME_PAUSED = "game_paused"
    GAME_OVER = "game_over"
