
import sys
import pygame

from settings import *
from grid import Grid
from path import Path
from enemy import Enemy
from player import Player
from helpers import PointerMode, can_place_tower, tiles_to_pixel_centers
from pointer import Pointer
from tower_manager import TowerManager
from tower import Tower

pygame.init()

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
clock = pygame.time.Clock()

player = Player("Player1")
grid = Grid(GRID_ROWS, GRID_COLS, TILE_SIZE)
path = Path(PATH)

tower_manager = TowerManager()

pointer = Pointer(grid, path, tower_manager)  # Tower manager is None for now
selected_tile = None

enemy_path = path.pixel_path
enemies = [Enemy(enemy_path)]  # Example enemy list

def main():
    while True:
        # --- Events ---
        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN:
                if pointer.mode == PointerMode.PLACE_TOWER:
                    tile_x, tile_y = pointer.tile_pos
                    if can_place_tower(grid, tile_x, tile_y, path.tile_path, tower_manager.towers):
                        if player.spend_money(10):
                            tower_manager.add_tower(Tower(tile_x, tile_y))
                            print(f"Placed tower at: {tile_x}, {tile_y}")
                        else :
                            print("Not enough money to place tower.")
                if pointer.mode == PointerMode.SELECT:
                    selected_tile = pointer.tile_pos
                    print(f"Selected tile: {selected_tile}")
                if event.button == 3:  # Right click to switch modes
                    if pointer.mode == PointerMode.SELECT:
                        pointer.set_mode(PointerMode.PLACE_TOWER)
                    else:
                        pointer.set_mode(PointerMode.SELECT)

            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        # --- Update ---
        pointer.update()

        for enemy in enemies:
            enemy.update()
            if not enemy.is_alive():
                enemies.remove(enemy)
                player.take_damage(10)
                print(f"Player Health: {player.health}")


        # --- Draw ---
        screen.fill((30, 30, 30))
        grid.draw(screen)
        player.draw(screen)
        path.draw(screen)
        
        tower_manager.draw(screen)

        for enemy in enemies:
            enemy.draw(screen)

        # --- Draw selected tile highlight ---
        pointer.draw(screen)
        pygame.display.flip()
        clock.tick(FPS)


if __name__ == "__main__":
    main()
