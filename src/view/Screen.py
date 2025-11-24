import pygame
import sys
from src.Constants import Constants as c
from typing import Tuple


class Screen:
    """Maneja la pantalla principal"""

    def __init__(
            self, width: int, height: int, title: str, bg_color: Tuple[int, int, int], fps: int
    ):
        pygame.init()

        self.width = width
        self.height = height
        self.title = title
        self.surface = pygame.display.set_mode((width, height))
        self.fps = fps

        pygame.display.set_caption(title)

        self.clock = pygame.time.Clock()
        self.delta_time: float = 0

        self.bg_color = bg_color

        self.running = True

    def render(self):
        """Renderiza los elementos del juego (sobrescribir en subclases)"""
        self.surface.fill(self.bg_color)

    def run(self):
        """Bucle principal del juego"""
        while self.running:

            pygame.display.flip()
            self.delta_time = self.clock.tick(self.fps) / 1000.0

        self.quit()

    def quit(self):
        """Salida del juego"""
        pygame.quit()
        sys.exit()
