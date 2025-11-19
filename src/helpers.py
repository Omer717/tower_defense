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

from enum import StrEnum

class PointerMode(StrEnum):
    SELECT = "select"
    PLACE_TOWER = "place_tower"