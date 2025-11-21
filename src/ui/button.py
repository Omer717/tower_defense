import pygame


class Button:
    def __init__(self, x, y, w, h, text, on_click,
                 font=None,
                 color_idle=(70, 70, 70),
                 color_hover=(100, 100, 100),
                 color_text=(255, 255, 255)):

        self.rect = pygame.Rect(x, y, w, h)
        self.text = text
        self.on_click = on_click

        self.color_idle = color_idle
        self.color_hover = color_hover
        self.color_text = color_text

        self.font = font or pygame.font.SysFont("arial", 24)

        self.hovered = False

    def update(self, events):
        mouse_pos = pygame.mouse.get_pos()
        self.hovered = self.rect.collidepoint(mouse_pos)

        for event in events:
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1 and self.hovered:
                    self.on_click()  # trigger callback

    def draw(self, surface):
        color = self.color_hover if self.hovered else self.color_idle
        pygame.draw.rect(surface, color, self.rect, border_radius=6)

        text_surf = self.font.render(self.text, True, self.color_text)
        text_rect = text_surf.get_rect(center=self.rect.center)
        surface.blit(text_surf, text_rect)
