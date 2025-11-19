
import sys
import pygame

from settings import *
from grid import Grid
from path import Path
from enemy import Enemy
from player import Player
from helpers import PointerMode, can_place_tower, tiles_to_pixel_centers
from pointer import Pointer

pygame.init()

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
clock = pygame.time.Clock()

player = Player("Player1")
grid = Grid(GRID_ROWS, GRID_COLS, TILE_SIZE)
path = Path(PATH)

pointer = Pointer(grid, path, None)  # Tower manager is None for now
selected_tile = None

enemy_path = path.pixel_path
enemies = [Enemy(enemy_path)]  # Example enemy list

def main():
    while True:
        # --- Events ---
        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN:
                if pointer.state == PointerMode.PLACE_TOWER:
                    grid_x, grid_y = pointer.tile_pos
                    if can_place_tower(grid, grid_x, grid_y, path.tile_path):
                        # Place tower logic here
                        print(f"Placed tower at: {grid_x}, {grid_y}")
                if pointer.state == PointerMode.SELECT:
                    selected_tile = pointer.tile_pos
                    print(f"Selected tile: {selected_tile}")
                if event.button == 3:  # Right click to switch modes
                    if pointer.state == PointerMode.SELECT:
                        pointer.state = PointerMode.PLACE_TOWER
                    else:
                        pointer.state = PointerMode.SELECT

            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        # --- Update ---
        pointer.update()

        for enemy in enemies:
            enemy.update()
            if not enemy.is_alive():
                enemies.remove(enemy)
                player.health -= 10
                print(f"Player Health: {player.health}")


        # --- Draw ---
        screen.fill((30, 30, 30))
        grid.draw(screen)
        player.draw(screen)
        path.draw(screen)
        
        for enemy in enemies:
            enemy.draw(screen)

        # --- Draw selected tile highlight ---
        pointer.draw(screen)
        pygame.display.flip()
        clock.tick(FPS)


if __name__ == "__main__":
    main()
