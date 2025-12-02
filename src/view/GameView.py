import pygame
import sys
from src.Constants import Constants as c
from src.view.Screen import Screen
from typing import Tuple
from src.model.GameModel import GameModel, PieceState

from src.controller.AudioController import AudioController


class GameView:

    _game_over_sound_played: bool = False

    def __init__(self, model: GameModel, audio_controller: AudioController):
        self.model = model
        self.audio_controller = audio_controller

        self.game_surface = pygame.Surface((c.GAME_WIDTH, c.GAME_HEIGHT))

        self.grid = self._create_grid_rects()
        self.bg = pygame.Surface((c.SCREEN_WIDTH, c.SCREEN_HEIGHT))
        self.bg.fill(c.BG_COLOR)

        self.title_txt = c.TITLE_FONT.render("TETRIS", True, (255, 255, 255))
        self.title_shadow = c.TITLE_FONT.render(
            "TETRIS", True, (100, 100, 100))
        self.next_piece_txt = c.TEXT_FONT.render(
            "Pieza siguiente", True, (255, 255, 255))

    def _create_grid_rects(self):
        """Crea los rectángulos de la cuadrícula"""
        return [pygame.Rect(x * c.BLOCK_SIZE, y * c.BLOCK_SIZE,
                            c.BLOCK_SIZE, c.BLOCK_SIZE)
                for x in range(c.GRID_WIDTH) for y in range(c.GRID_HEIGHT)]

    def render(self, surface):
        """Renderiza todos los elementos en la superficie dada"""
        # Dibujar fondo principal
        surface.blit(self.bg, (0, 0))

        # Dibujar superficie del juego
        surface.blit(self.game_surface, (20, 20))
        self.game_surface.fill(c.T_COLORS[0])

        # Dibujar elementos del juego
        self._draw_grid()
        self._draw_board()
        self._draw_current_piece()
        self._draw_ui(surface)
        self._draw_next_piece(surface)

        # Dibujar game over si es necesario
        if self.model.game_over:
            self._draw_game_over(surface)

    def _draw_grid(self):
        """Dibuja la cuadrícula del tablero"""
        for rect in self.grid:
            pygame.draw.rect(self.game_surface, (40, 40, 40), rect, 1)

    def _draw_board(self):
        """Dibuja las piezas fijadas en el tablero"""
        for y in range(self.model.board.height):
            for x in range(self.model.board.width):
                if self.model.board.grid[y, x] != 0:

                    color = c.T_COLORS[self.model.board.grid[y, x]]

                    rect = pygame.Rect(
                        x * c.BLOCK_SIZE, y * c.BLOCK_SIZE,
                        c.BLOCK_SIZE, c.BLOCK_SIZE)
                    pygame.draw.rect(self.game_surface, color, rect)
                    pygame.draw.rect(
                        self.game_surface,
                        (255, 255, 255), rect, 1)

    def _draw_current_piece(self):
        """Dibuja la pieza actual con borde blanco"""
        piece = self.model.current_piece

        for y in range(piece.matrix.shape[0]):
            for x in range(piece.matrix.shape[1]):
                if piece.matrix[y, x] != 0:
                    rect = pygame.Rect(
                        (piece.x + x) * c.BLOCK_SIZE,
                        (piece.y + y) * c.BLOCK_SIZE,
                        c.BLOCK_SIZE, c.BLOCK_SIZE)
                    # Dibujar el bloque con color de la pieza
                    pygame.draw.rect(
                        self.game_surface,
                        c.T_COLORS[piece.type_num], rect)
                    # Dibujar borde blanco
                    pygame.draw.rect(
                        self.game_surface,
                        (255, 255, 255), rect, 1)

    def _draw_ui(self, surface):
        """Dibuja la interfaz de usuario"""

        # Salta el tablero + el margen + extra
        surface.blit(self.title_shadow, (
            c.BLOCK_SIZE * c.GRID_WIDTH+20 + 60 - 2,
            c.BLOCK_SIZE*1 + 2))
        surface.blit(self.title_txt, (
            c.BLOCK_SIZE * c.GRID_WIDTH+20 + 60,
            c.BLOCK_SIZE*1))

        surface.blit(
            self.next_piece_txt,
            (c.BLOCK_SIZE * c.GRID_WIDTH+20 + 60,
             c.BLOCK_SIZE * 3))

        # Información del juego
        score_text = c.TEXT_FONT.render(
            f"Puntuacion: {self.model.score}", True, (255, 255, 255))
        level_text = c.TEXT_FONT.render(
            f"Nivel: {self.model.level}", True, (255, 255, 255))
        lines_text = c.TEXT_FONT.render(
            f"Lineas: {self.model.lines_cleared}", True, (255, 255, 255))

        # Estado de la pieza
        state = self.model.get_piece_state()
        state_text = c.TEXT_FONT.render(
            f"Estado: {state.value}", True, (255, 255, 255))

        surface.blit(
            score_text,
            (c.BLOCK_SIZE * c.GRID_WIDTH+20 + 60,
             c.BLOCK_SIZE * (c.GRID_HEIGHT - 5)))
        surface.blit(
            level_text,
            (c.BLOCK_SIZE * c.GRID_WIDTH+20 + 60,
             c.BLOCK_SIZE * (c.GRID_HEIGHT - 3)))
        surface.blit(
            lines_text,
            (c.BLOCK_SIZE * c.GRID_WIDTH+20 + 60 - 2,
             c.BLOCK_SIZE * (c.GRID_HEIGHT - 1)))
        surface.blit(
            state_text,
            (c.BLOCK_SIZE * c.GRID_WIDTH+20 + 60,
             c.BLOCK_SIZE * 10))

    def _draw_next_piece(self, surface):
        """Dibuja la siguiente pieza usando constantes (c) para posición y tamaño."""
        # Posición de la columna lateral / margen (coherente con _draw_ui)
        sidebar_x = 20 + c.BLOCK_SIZE * c.GRID_WIDTH + 60
        sidebar_y = 20 + c.BLOCK_SIZE

        # Área donde se mostrará la pieza siguiente (cuadrado)
        area_size = c.BLOCK_SIZE * 4  # configurable desde c si cambias BLOCK_SIZE
        area_x = sidebar_x
        # colocamos el área justo debajo del título "Pieza siguiente" (ese texto usa y = c.BLOCK_SIZE * 3)
        area_y = sidebar_y + c.BLOCK_SIZE * 3

        next_area = pygame.Rect(area_x, area_y, area_size, area_size)
        # fondo y borde del área (mantén coherencia visual con el resto)
        pygame.draw.rect(surface, (0, 0, 0), next_area)
        pygame.draw.rect(surface, (255, 255, 255), next_area, 1)

        piece = self.model.next_piece
        if piece is None:
            return

        # calculamos el tamaño de celda para que la pieza quepa en el área
        cols = piece.matrix.shape[1]
        rows = piece.matrix.shape[0]
        # cell_size no supera c.BLOCK_SIZE y se adapta a area_size
        cell_size = min(c.BLOCK_SIZE, max(1, area_size // max(cols, rows)))

        # centrado dentro del cuadro next_area
        start_x = area_x + (area_size - cols * cell_size) // 2
        start_y = area_y + (area_size - rows * cell_size) // 2

        # dibujar la pieza (en la superficie principal, con borde blanco como el resto)
        for y in range(rows):
            for x in range(cols):
                if piece.matrix[y, x] != 0:
                    rect = pygame.Rect(
                        start_x + x * cell_size,
                        start_y + y * cell_size,
                        cell_size, cell_size
                    )
                    pygame.draw.rect(surface, c.T_COLORS[piece.type_num], rect)
                    pygame.draw.rect(surface, (255, 255, 255), rect, 1)

    def _draw_game_over(self, surface):
        """Dibuja la pantalla de game over"""

        overlay = pygame.Surface(
            (c.SCREEN_WIDTH, c.SCREEN_HEIGHT), pygame.SRCALPHA)
        overlay.fill((0, 0, 0, 128))
        surface.blit(overlay, (0, 0))

        game_over_text = c.TITLE_FONT.render("GAME OVER", True, (255, 0, 0))

        surface.blit(game_over_text, (750 // 2 - game_over_text.get_width() // 2,
                                      940 // 2 - 50))

        self.audio_controller.stop_music()
        if not self._game_over_sound_played:
            self.audio_controller.play_sound("gameover")
            self._game_over_sound_played = True
