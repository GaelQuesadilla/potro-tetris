import numpy as np
from src.Constants import Constants as c
from src.model.Tetromino import Tetronimo
import numpy as np
from numpy.typing import NDArray


class Board:
    """Modelo del tablero"""

    def __init__(self, width=c.GRID_WIDTH, height=c.GRID_HEIGHT):
        self.width = width
        self.height = height
        self.grid = np.zeros((height, width), dtype=int)
        self.tile_size = c.TILE_SIZE

    def is_collision(self, piece: NDArray[np.int_], piece_x: int, piece_y: int) -> bool:
        """Verifica que la pieza tenga colisión

        Parameters
        ----------
        piece : piece: NDArray[np.int_]
            Figura de la pieza a verificar si tiene colisión
        piece_x : int
            Posición x a verificar
        piece_y : int
            Posición y a verificar

        Returns
        -------
        bool
            Verdadero si hay colisión, falso si no
        """
        for y in range(piece.shape[0]):
            for x in range(piece.shape[1]):
                if piece[y, x] != 0:
                    grid_x = piece_x + x
                    grid_y = piece_y + y

                    if (grid_x < 0 or grid_x >= self.width or
                            grid_y >= self.height):
                        return True

                    if grid_y >= 0 and self.grid[grid_y, grid_x] != 0:
                        return True
        return False

    def place_piece(self, piece: NDArray[np.int_], piece_x: int, piece_y: int, piece_type: int):
        """Coloca una pieza en el tablero

        Parameters
        ----------
        piece : NDArray[np.int_]
            Figura de la pieza a colocar
        piece_x : int
            Posición x de la pieza a colocar
        piece_y : int
            Posición y de la pieza a colocar
        piece_type : int
            Tipo de la pieza
        """
        for y in range(piece.shape[0]):
            for x in range(piece.shape[1]):
                if piece[y, x] != 0:
                    grid_x = piece_x + x
                    grid_y = piece_y + y
                    if 0 <= grid_y < self.height and 0 <= grid_x < self.width:
                        self.grid[grid_y, grid_x] = piece_type

    def clear_lines(self) -> int:
        """Limpia las lineas completas y retorna la cantidad de lineas

        Returns
        -------
        int
            Cantidad de lineas completadas
        """
        lines_to_clear = []

        for y in range(self.height):
            if np.all(self.grid[y, :] != 0):
                lines_to_clear.append(y)

        for line in sorted(lines_to_clear):
            self.grid = np.delete(self.grid, line, axis=0)
            self.grid = np.vstack(
                [np.zeros((1, self.width), dtype=int), self.grid])

        return len(lines_to_clear)

    def reset(self):
        """Reinicia el tablero
        """
        self.grid = np.zeros((self.height, self.width), dtype=int)
