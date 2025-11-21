from dataclasses import dataclass


@dataclass
class Constants:

    # ? Game constants
    BLOCK_SIZE: int = 30
    GRID_WIDTH: int = 10
    GRID_HEIGHT: int = 20

    # ? Window constants
    SCREEN_WIDTH: int = BLOCK_SIZE * (GRID_WIDTH+3)
    SCREEN_HEIGHT: int = BLOCK_SIZE * GRID_HEIGHT
