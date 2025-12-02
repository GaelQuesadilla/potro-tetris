import numpy as np
from enum import Enum
from src.model.Board import Board
from src.model.Tetromino import Tetronimo, Tetronimos, O
from random import choice
from typing import Type
from src.Constants import Constants as c
from src.controller.AudioController import AudioController


class PieceState(Enum):
    """Estados posibles de una pieza de Tetris"""
    MOVIENDO = "MOVIENDO"      # Se está moviendo (LEFT/RIGHT)
    ROTANDO = "ROTANDO"        # Se está rotando (UP)
    CAYENDO = "CAYENDO"        # Está cayendo automáticamente (TIMER)
    BLOQUEADO = "BLOQUEADO"    # Fijada en el tablero (SPACE o COLISIÓN)


class GameModel:
    """Modelo que coordina el estado del juego"""

    def __init__(self, audio_controller: AudioController = None):
        self.board = Board()
        self.current_piece = self._create_new_piece()
        self.next_piece = self._create_new_piece()
        self.score = 0
        self.level = 1
        self.lines_cleared = 0
        self.game_over = False
        self.fall_speed = 1000
        self.fall_time = 0
        self.audio_controller = audio_controller

        # Estado de la pieza actual
        self.piece_state = PieceState.CAYENDO
        self.last_state = PieceState.CAYENDO

    def _create_new_piece(self) -> Tetronimo:
        tetronimo = choice(Tetronimos)()
        tetronimo.x = c.GRID_WIDTH // 2 - tetronimo.matrix.shape[1] // 2
        return tetronimo

    def get_piece_state(self) -> PieceState:
        """
        Retorna el estado actual de la pieza basado en las condiciones:
        - MOVIENDO: Se acaba de mover (LEFT/RIGHT)
        - ROTANDO: Se acaba de rotar (UP)
        - CAYENDO: Está cayendo automáticamente por timer
        - BLOQUEADO: Está fijada en el tablero (SPACE o COLISIÓN)

        Returns:
            PieceState: El estado actual de la pieza
        """
        return self.piece_state

    def move_piece(self, dx, dy) -> bool:
        """Intenta mover la pieza actual"""
        if self.game_over:
            return False

        if not self.board.is_collision(
                self.current_piece.matrix,
                self.current_piece.x + dx,
                self.current_piece.y + dy):

            self.current_piece.x += dx
            self.current_piece.y += dy

            # Cambiar estado a MOVIENDO si hay movimiento horizontal
            if dx != 0:
                self.piece_state = PieceState.MOVIENDO

            print(f"{self.current_piece.y=}")
            return True
        return False

    def rotate_piece(self):
        """Intenta rotar la pieza actual"""
        if self.game_over:
            return False

        rotated = self.current_piece.get_rotate_left()
        if not self.board.is_collision(rotated, self.current_piece.x, self.current_piece.y):
            self.current_piece.rotate_left()
            self.piece_state = PieceState.ROTANDO
            print(
                f"Rotación exitosa\t{self.current_piece.x=}, {self.current_piece.y=}")
            return True
        else:
            print(
                f"Hay colisión al rotar\t{self.current_piece.x=}, {self.current_piece.y=}")
        return False

    def hard_drop(self):
        """Deja caer la pieza instantáneamente"""
        if self.game_over:
            return

        while self.move_piece(0, 1):
            pass

        # Cambiar estado a BLOQUEADO cuando se fija la pieza
        self.piece_state = PieceState.BLOQUEADO
        self._lock_piece()

    def _lock_piece(self):
        """Fija la pieza actual en el tablero"""
        self.board.place_piece(
            self.current_piece.matrix,
            self.current_piece.x,
            self.current_piece.y,
            self.current_piece.type_num)

        # ?  Verificar líneas completas
        lines = self.board.clear_lines()
        if lines > 0:
            self._update_score(lines)
            self.lines_cleared += lines
            self.level = self.lines_cleared // 10 + 1
            if self.audio_controller:
                self.audio_controller.play_sound("clear")

        # ? Crear nueva pieza
        self.current_piece = self.next_piece
        self.next_piece = self._create_new_piece()

        # ?  Verificar game over
        if self.board.is_collision(
                self.current_piece.matrix,
                self.current_piece.x,
                self.current_piece.y):
            self.game_over = True

    def _update_score(self, lines_cleared):
        """Actualiza la puntuación basada en líneas eliminadas"""
        points = {1: 100, 2: 300, 3: 500, 4: 800}
        self.score += points.get(lines_cleared, 0) * self.level

    def update(self, delta_time):
        """Actualiza la lógica del juego (caída)"""
        if self.game_over:
            return

        self.fall_time += delta_time * 1000  # Convertir a ms
        if self.fall_time >= self.fall_speed:
            self.fall_time = 0

            # Cambiar estado a CAYENDO en cada actualización de caída
            self.piece_state = PieceState.CAYENDO

            if not self.move_piece(0, 1):
                # Si no puede caer más, cambiar a BLOQUEADO por colisión
                self.piece_state = PieceState.BLOQUEADO
                self._lock_piece()

        # Actualizar velocidad basada en nivel
        self.fall_speed = max(100, 1000 - (self.level - 1) * 125)

    def restart(self):
        """Reinicia el juego completo"""
        self.board.reset()
        self.current_piece = self._create_new_piece()
        self.next_piece = self._create_new_piece()
        self.score = 0
        self.level = 1
        self.lines_cleared = 0
        self.game_over = False
        self.fall_time = 0
        self.piece_state = PieceState.CAYENDO
        self.last_state = PieceState.CAYENDO
