def tiles_to_pixel_centers(tiles, tile_size):
    """
    Converts a list of (col,row) tiles into pixel center coordinates.
    """
    return [(x * tile_size + tile_size // 2, y * tile_size + tile_size // 2) for x, y in tiles]
