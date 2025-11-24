import numpy as np
from src.model.Shape import Shape
from typing import Tuple
from numpy.typing import NDArray


class Tetronimo(Shape):
    """Clase genérica del Tetronimo"""
    x: int
    y: int
    color: Tuple[int, int, int]
    type_num: int

    def __init__(self, matrix: NDArray[np.int_], x: int = 0, y: int = 0, type_num: int = 1, color: Tuple[int, int, int] = (0, 0, 0)):

        super().__init__(matrix=matrix)

        self.x = x
        self.y = y
        self.type_num = type_num
        self.color = color

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
        super().__init__(matrix, type_num=1)


class O(Tetronimo):
    def __init__(self):
        matrix = np.array([
            [1, 1],
            [1, 1]
        ], dtype=np.int_)
        super().__init__(matrix, type_num=2)


class T(Tetronimo):
    def __init__(self):
        matrix = np.array([
            [0, 1, 0],
            [1, 1, 1]
        ], dtype=np.int_)
        super().__init__(matrix, type_num=3)


class S(Tetronimo):
    def __init__(self):
        matrix = np.array([
            [0, 1, 1],
            [1, 1, 0]
        ], dtype=np.int_)
        super().__init__(matrix, type_num=4)


class Z(Tetronimo):
    def __init__(self):
        matrix = np.array([
            [1, 1, 0],
            [0, 1, 1]
        ], dtype=np.int_)
        super().__init__(matrix, type_num=5)


class J(Tetronimo):
    def __init__(self):
        matrix = np.array([
            [1, 0, 0],
            [1, 1, 1]
        ], dtype=np.int_)
        super().__init__(matrix, type_num=6)


class L(Tetronimo):
    def __init__(self):
        matrix = np.array([
            [0, 0, 1],
            [1, 1, 1]
        ], dtype=np.int_)
        super().__init__(matrix, type_num=7)


Tetronimos = [I, O, T, S, Z, J, L]
