from enum import StrEnum


def tiles_to_pixel_centers(tiles, tile_size):
    """
    Converts a list of (col,row) tiles into pixel center coordinates.
    """
    return [(x * tile_size + tile_size // 2, y * tile_size + tile_size // 2) for x, y in tiles]


def can_place_tower(grid, tile_x, tile_y, path_tiles, towers=[]):
    """
    Check if a tower can be placed at the given grid coordinates.
    Towers cannot be placed on path tiles or outside the grid.
    """
    if (tile_x, tile_y) in path_tiles:
        return False
    if tile_x < 0 or tile_x >= grid.cols or tile_y < 0 or tile_y >= grid.rows:
        return False

    for tower in towers:
        if tower.tile_x == tile_x and tower.tile_y == tile_y:
            return False
    return True


def draw_glow_text(surface, text, font, color, pos, glow_color=(50, 50, 50)):
    # Glow layer
    glow = font.render(text, True, glow_color)
    for offset in range(1, 6):
        surface.blit(glow, (pos[0]-offset, pos[1]))
        surface.blit(glow, (pos[0]+offset, pos[1]))
        surface.blit(glow, (pos[0], pos[1]-offset))
        surface.blit(glow, (pos[0], pos[1]+offset))

    # Main text
    text_surface = font.render(text, True, color)
    surface.blit(text_surface, pos)


class PointerMode(StrEnum):
    SELECT = "select"
    PLACE_TOWER = "place_tower"
