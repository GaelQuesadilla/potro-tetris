import numpy as np
from src.model.Shape import Shape
from typing import List, Type, Union
from numpy.typing import NDArray


"""Constructor del Tetronimo

        Parameters
        ----------
        matrix : NDArray[np.int_]
            Matriz con el estado inicial de la figura
        x : int, optional
            Posición en el eje x del tablero, by default 0
        y : int, optional
            Posición en el eje y del tablero, by default 0
        """


class Tetronimo(Shape):
    """Clase genérica del Tetronimo"""
    x: int
    y: int
    type_num: int

    def __init__(self, matrix: NDArray[np.int_], x: int = 0, y: int = 0, type_num: int = 1):

        super().__init__(matrix=matrix)

        self.x = x
        self.y = y
        type_num = 1

    def move_left(self):
        self.x -= 1

    def move_right(self):
        self.x += 1

    def move_down(self):
        self.y += 1


class I(Tetronimo):
    def __init__(self):
        matrix = np.array([
            [1, 1, 1, 1]
        ], dtype=np.int_)
        super().__init__(matrix, type_num=0)


class O(Tetronimo):
    def __init__(self):
        matrix = np.array([
            [1, 1],
            [1, 1]
        ], dtype=np.int_)
        super().__init__(matrix, type_num=1)


class T(Tetronimo):
    def __init__(self):
        matrix = np.array([
            [0, 1, 0],
            [1, 1, 1]
        ], dtype=np.int_)
        super().__init__(matrix, type_num=2)


class S(Tetronimo):
    def __init__(self):
        matrix = np.array([
            [0, 1, 1],
            [1, 1, 0]
        ], dtype=np.int_)
        super().__init__(matrix, type_num=3)


class Z(Tetronimo):
    def __init__(self):
        matrix = np.array([
            [1, 1, 0],
            [0, 1, 1]
        ], dtype=np.int_)
        super().__init__(matrix, type_num=4)


class J(Tetronimo):
    def __init__(self):
        matrix = np.array([
            [1, 0, 0],
            [1, 1, 1]
        ], dtype=np.int_)
        super().__init__(matrix, type_num=5)


class L(Tetronimo):
    def __init__(self):
        matrix = np.array([
            [0, 0, 1],
            [1, 1, 1]
        ], dtype=np.int_)
        super().__init__(matrix, type_num=6)


Tetronimos = [I, O, T, S, Z, J, L]
