import numpy as np
from numpy.typing import NDArray


class Shape:
    """Clase genérica de figura"""
    matrix: NDArray[np.int_]

    def __init__(self, matrix: NDArray[np.int_]):
        self.matrix = matrix

    def rotate_right(self) -> NDArray[np.int_]:
        """Rota la figura 90º hacia la derecha

        Returns
        -------
        NDArray[np.int_]
            La nueva matriz rotada
        """

        return self.matrix

    def rotate_left(self) -> NDArray[np.int_]:
        """Rota la figura 90º hacia la izquierda

        Returns
        -------
        NDArray[np.int_]
            La nueva matriz rotada
        """
        return self.matrix
