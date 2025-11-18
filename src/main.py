
import sys
import pygame

from settings import *


pygame.init()

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
clock = pygame.time.Clock()


def main():
    while True:
        # --- Events ---
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        # --- Update ---
        # for enemy in enemies:
        #     enemy.update()

        # --- Draw ---
        screen.fill((30, 30, 30))
        # grid.draw(screen)
        
        # for enemy in enemies:
        #     enemy.draw(screen)

        pygame.display.flip()
        clock.tick(FPS)


if __name__ == "__main__":
    main()
