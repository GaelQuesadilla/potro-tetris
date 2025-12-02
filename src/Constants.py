from dataclasses import dataclass
import pygame
from typing import Tuple
from pathlib import Path
import sys

pygame.init()


def resource_path(relative: str | Path) -> Path:
    """
    Devuelve la ruta absoluta de un recurso, funcionando tanto en desarrollo como dentro de un ejecutable creado por PyInstaller.
    """
    if hasattr(sys, "_MEIPASS"):
        base = Path(sys._MEIPASS)   # Ruta temporal cuando es --onefile
    else:
        base = Path(__file__).parent.parent  # Ruta del proyecto en desarrollo

    return base / relative


@dataclass
class Constants:

    SCREEN_TITLE: str = "Tetris"

    # ? Game constants
    BLOCK_SIZE: int = 40
    GRID_WIDTH: int = 10
    GRID_HEIGHT: int = 20

    # ? Window constants

    GAME_WIDTH: int = BLOCK_SIZE * GRID_WIDTH
    GAME_HEIGHT: int = BLOCK_SIZE * GRID_HEIGHT
    SCREEN_WIDTH: int = BLOCK_SIZE * (GRID_WIDTH+10)
    SCREEN_HEIGHT: int = BLOCK_SIZE * GRID_HEIGHT + 40
    GAME_FPS: int = 60

    # ? GAME CONSTANTS

    # ! No detecta la fuente
    TITLE_FONT = pygame.font.SysFont('tetrominoes.ttf', 75, bold=True)
    TEXT_FONT = pygame.font.SysFont('tetrominoes.ttf', 40, bold=True)

    BG_COLOR: Tuple[int, int, int] = (30, 30, 50)
    SURFACE_BG: Tuple[int, int, int] = (0, 0, 0)

    # ? Shapes colors

    # ? I, O, T, S, Z, J, L
    T_COLORS: Tuple[Tuple[int, int, int], ...] = (
        (7, 7, 7),
        (13, 250, 255),
        (209, 178, 12),
        (154, 0, 249),
        (113, 253, 22),
        (191, 0, 46),
        (19, 1, 233),
        (252, 97, 15),
    )

    ASSETS_DIR: Path = resource_path("assets")
    MUSIC_DIR: Path = ASSETS_DIR / "music"
    SOUNDTRACK_PATH: Path = MUSIC_DIR / "soundtrack.mp3"

    SFX_DIR: Path = ASSETS_DIR / "sounds"

    SOUND_ROTATE: Path = SFX_DIR / "Tetris (GB) (19)-rotate_piece.wav"
    SOUND_MOVE: Path = SFX_DIR / "Tetris (GB) (18)-move_piece.wav"
    SOUND_DROP: Path = SFX_DIR / "Tetris (GB) (27)-piece_landed.wav"
    SOUND_CLEAR: Path = SFX_DIR / "Tetris (GB) (21)-line_clear.wav"
    SOUND_GAMEOVER: Path = SFX_DIR / "Tetris (GB) (25)-game_over.wav"

    LOGO_DIR: Path = ASSETS_DIR / "logo.png"
