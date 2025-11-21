
import sys
import pygame

from events.event_bus import EventBus
from events.screen_state import ScreenState
from screens.main_menu_screen import MainMenuScreen
from settings import *
from helpers import PointerMode
from game_state import GameState

pygame.init()

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
clock = pygame.time.Clock()

event_bus = EventBus()

game_state = GameState(event_bus)
main_menu_screen = MainMenuScreen(game_state, event_bus)


def handle_mouse_click(event, game_state):
    if event.button == 3:
        # Switch modes
        if game_state.pointer.mode == PointerMode.SELECT:
            game_state.pointer.set_mode(PointerMode.PLACE_TOWER)
        else:
            game_state.pointer.set_mode(PointerMode.SELECT)
        return

    tile = game_state.pointer.tile_pos

    if game_state.pointer.mode == PointerMode.PLACE_TOWER:
        handle_tower_placement(tile, game_state)

    elif game_state.pointer.mode == PointerMode.SELECT:
        handle_tower_selection(tile, game_state)


def handle_tower_selection(tile, game_state: GameState):
    tower = game_state.tower_manager.get_tower_at(tile)

    if tower:
        game_state.set_selected_tower(tower)
    else:
        game_state.set_selected_tower(None)


def handle_tower_placement(tile, game_state: GameState):
    tile_x, tile_y = tile

    print(f"{tile_x}, {tile_y}")
    # 1. Ask the tower manager if the tile is valid
    if not game_state.tower_manager.can_place_tower(tile):
        print("Cannot place tower here.")
        return

    # 2. Try spending the money
    tower_cost = 10  # Later move to a settings or tower data table
    if not game_state.spend_money(tower_cost):
        print("Not enough money to place tower.")
        return

    # 3. Add the tower
    game_state.tower_manager.add_tower_at(tile)
    print(f"Placed tower at: {tile_x}, {tile_y}")


def handle_game(dt):
    # --- Update ---
    game_state.wave_manager.update_wave(dt)
    game_state.enemy_manager.update_enemies(dt)
    game_state.tower_manager.update_towers(dt)

    # --- Draw ---
    screen.fill((30, 30, 30))

    game_state.grid.draw(screen)
    game_state.path.draw(screen)

    game_state.tower_manager.draw_towers(screen, game_state.selected_tower)
    game_state.enemy_manager.draw_enemies(screen)

    # --- Draw selected tile highlight ---
    game_state.pointer.draw(screen)

    game_state.game_ui.draw(screen)


def handle_game_events():
    for event in pygame.event.get():

        if event.type == pygame.MOUSEBUTTONDOWN:
            handle_mouse_click(event, game_state)

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                game_state.wave_manager.next_wave()

        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()


def main():
    while True:
        dt = clock.tick(FPS) / 1000

        if game_state.current_state == ScreenState.GAME_RUNNING:
            game_state.pointer.update()
            handle_game_events()
            handle_game(dt)

        elif game_state.current_state == ScreenState.MAIN_MENU:
            main_menu_screen.update(pygame.event.get())
            main_menu_screen.draw(screen)

        pygame.display.flip()


if __name__ == "__main__":
    main()
