import sys
import pygame

from events.screen_state import ScreenState
from helpers import draw_glow_text
from settings import GAME_FONT_NAME, SCREEN_HEIGHT, SCREEN_WIDTH
from ui.button import Button


class MainMenuScreen:
    def __init__(self, game_state):
        self.game_state = game_state

        button_font = pygame.font.Font(GAME_FONT_NAME, 18)
        self.buttons = [
            Button(
                x=SCREEN_WIDTH / 2 - 125, y=SCREEN_HEIGHT / 2 - 30, w=250, h=60,
                text="Start Game",
                font=button_font,
                on_click=self.start_game
            ),
            Button(
                x=SCREEN_WIDTH / 2 - 125, y=SCREEN_HEIGHT / 2 + 70, w=250, h=60,
                text="Quit",
                font=button_font,
                on_click=self.quit_game
            )
        ]

    def start_game(self):
        self.game_state.set_screen_state(ScreenState.GAME_RUNNING)

    def quit_game(self):
        pygame.quit()
        sys.exit()

    def update(self, events):

        for event in events:
            if event.type == pygame.QUIT:
                self.quit_game()

        hovered_any = False
        for btn in self.buttons:
            btn.update(events)
            if btn.hovered:
                hovered_any = True

        if hovered_any:
            pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_HAND)
        else:
            pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_ARROW)

    def draw(self, screen):
        screen.fill((30, 30, 30))
        self.game_state.grid.draw(screen)

        title_font = pygame.font.Font(
            GAME_FONT_NAME, 48)
        title_surf = title_font.render("Tower Defense", True, (255, 255, 255))
        title_rect = title_surf.get_rect(center=(SCREEN_WIDTH // 2, 120))

        draw_glow_text(screen, "Tower Defense", title_font,
                       (255, 255, 255), title_rect.topleft)

        screen.blit(title_surf, title_rect)
        for btn in self.buttons:
            btn.draw(screen)
