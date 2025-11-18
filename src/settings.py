SCREEN_WIDTH = 960
SCREEN_HEIGHT = 640
FPS = 60

TILE_SIZE = 32
GRID_ROWS = SCREEN_HEIGHT // TILE_SIZE
GRID_COLS = SCREEN_WIDTH // TILE_SIZE

COLOR_GRID = (50, 50, 50)
COLOR_PATH = (130, 100, 50)

PATH = [
    # Horizontal from (1,10) to (5,10)
    (1,10), (2,10), (3,10), (4,10), (5,10),
    # Vertical up from (5,10) to (5,5)
    (5,9), (5,8), (5,7), (5,6), (5,5),
    # Horizontal right from (5,5) to (15,5)
    (6,5), (7,5), (8,5), (9,5), (10,5),
    (11,5), (12,5), (13,5), (14,5), (15,5),
    # Vertical down from (15,5) to (15,12)
    (15,6), (15,7), (15,8), (15,9), (15,10),
    (15,11), (15,12),
    # Horizontal right from (15,12) to (25,12)
    (16,12), (17,12), (18,12), (19,12), (20,12),
    (21,12), (22,12), (23,12), (24,12), (25,12)
]