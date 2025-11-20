import pygame


class GameUI:
    def __init__(self, game_state, font_name="Arial", font_size=20):
        self.game_state = game_state
        self.font = pygame.font.SysFont(font_name, font_size)
        self.padding = 10
        self.line_height = font_size + 4  # spacing between lines

    def draw(self, screen):
        x = self.padding
        y = self.padding

        # --- Health ---
        health_text = self.font.render(f"Health: {self.game_state.health}", True, (255, 0, 0))
        screen.blit(health_text, (x, y))
        y += self.line_height

        # --- Money ---
        money_text = self.font.render(f"Money: {self.game_state.money}", True, (255, 255, 0))
        screen.blit(money_text, (x, y))
        y += self.line_height

        # --- Wave ---
        wave_text = self.font.render(f"Wave: {self.game_state.wave}", True, (0, 255, 0))
        screen.blit(wave_text, (x, y))
        y += self.line_height

        # --- Selected Tower ---
        if self.game_state.selected_tower:
            tower = self.game_state.selected_tower
            tower_info_text = self.font.render(f"Selected Tower: ({tower.tile_x}, {tower.tile_y})", True, (0, 255, 255))
            screen.blit(tower_info_text, (x, y))
            y += self.line_height