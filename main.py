import pygame
from src.Constants import Constants as c
from src.model.GameModel import GameModel
from src.view.GameView import GameView
from src.controller.GameController import GameController
from src.view.Screen import Screen
from src.controller.AudioController import AudioController


class Game(Screen):
    """Clase principal que coordina MVC"""

    def __init__(self):
        super().__init__(width=c.SCREEN_WIDTH, height=c.SCREEN_HEIGHT, title="Tetris",
                         bg_color=c.BG_COLOR, fps=c.GAME_FPS)

        # Inicializar MVC
        self.audio_controller = AudioController()
        self.model = GameModel(self.audio_controller)
        self.view = GameView(self.model, self.audio_controller)
        self.controller = GameController(self.model, self.audio_controller)

    def run(self):
        """Bucle principal del juego"""
        while self.running:
            # Controlador maneja eventos
            self.running = self.controller.handle_events()

            # Controlador actualiza modelo
            self.controller.update(self.delta_time)

            # Vista renderiza el estado actual
            self.view.render(self.surface)

            # Actualizar pantalla
            pygame.display.flip()
            self.delta_time = self.clock.tick(c.GAME_FPS) / 1000.0

        self.quit()


# Punto de entrada
if __name__ == "__main__":
    game = Game()
    game.run()
