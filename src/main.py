
import sys
import pygame

from settings import *
from grid import Grid
from path import Path
from enemy import Enemy
from player import Player
from helpers import tiles_to_pixel_centers

pygame.init()

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
clock = pygame.time.Clock()

player = Player("Player1")
grid = Grid(GRID_ROWS, GRID_COLS, TILE_SIZE)
path = Path(PATH)

enemy_path = path.pixel_path
enemies = [Enemy(enemy_path)]  # Example enemy list

def main():
    while True:
        # --- Events ---
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        # --- Update ---
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

        pygame.display.flip()
        clock.tick(FPS)


if __name__ == "__main__":
    main()
