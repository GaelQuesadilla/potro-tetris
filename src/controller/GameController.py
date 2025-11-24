import pygame
from src.model.GameModel import GameModel
from src.controller.AudioController import AudioController


class GameController:
    """Controlador del juego"""

    def __init__(self, model: GameModel, audio_controller: AudioController):
        self.model = model
        self.audioController = audio_controller
        self.audioController.play_music()

    def handle_events(self) -> bool:
        """Procesa todos los eventos y actualiza el modelo"""
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return False
            self._handle_event(event)
        return True

    def _handle_event(self, event) -> bool:
        """Maneja un evento específico"""
        if event.type == pygame.KEYDOWN:
            if self.model.game_over:
                if event.key == pygame.K_r:
                    self.model.restart
            else:
                if event.key in (pygame.K_ESCAPE,):
                    return False
                elif event.key in (pygame.K_LEFT, pygame.K_a):
                    if self.model.move_piece(-1, 0):
                        self.audioController.play_sound("move")
                elif event.key in (pygame.K_RIGHT, pygame.K_d):
                    if self.model.move_piece(1, 0):
                        self.audioController.play_sound("move")

                elif event.key in (pygame.K_DOWN, pygame.K_s):
                    self.model.move_piece(0, 1)
                elif event.key in (pygame.K_UP, pygame.K_w):
                    if self.model.rotate_piece():
                        self.audioController.play_sound("rotate")
                elif event.key in (pygame.K_SPACE,):
                    self.model.hard_drop()
                    self.audioController.play_sound("drop")
        return True

    def update(self, delta_time):
        """Actualiza la lógica del juego"""
        self.model.update(delta_time)
