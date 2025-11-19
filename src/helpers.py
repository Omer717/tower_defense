def tiles_to_pixel_centers(tiles, tile_size):
    """
    Converts a list of (col,row) tiles into pixel center coordinates.
    """
    return [(x * tile_size + tile_size // 2, y * tile_size + tile_size // 2) for x, y in tiles]

def can_place_tower(grid, grid_x, grid_y, path_tiles, towers=[]):
    """
    Check if a tower can be placed at the given grid coordinates.
    Towers cannot be placed on path tiles or outside the grid.
    """
    if (grid_x, grid_y) in path_tiles:
        return False
    if grid_x < 0 or grid_x >= grid.cols or grid_y < 0 or grid_y >= grid.rows:
        return False
    for tower in towers:
        if tower.grid_x == grid_x and tower.grid_y == grid_y:
            return False
    return True