import numpy as np
from numpy.typing import NDArray


class Shape:
    """Clase genérica de figura"""
    matrix: NDArray[np.int_]

    def __init__(self, matrix: NDArray[np.int_]):
        self.matrix = matrix

    def rotate_right(self) -> NDArray[np.int_]:
        """Rota la figura 90º hacia la derecha y actualiza el estado de la misma

        Returns
        -------
        NDArray[np.int_]
            La nueva matriz rotada
        """

        self.matrix = np.rot90(self.matrix, -1)
        return self.matrix

    def rotate_left(self) -> NDArray[np.int_]:
        """Rota la figura 90º hacia la izquierda y actualiza el estado de la misma

        Returns
        -------
        NDArray[np.int_]
            La nueva matriz rotada
        """
        self.matrix = np.rot90(self.matrix, 1)
        return self.matrix

    def get_matrix(self) -> NDArray[np.int_]:
        """Obtiene la matriz de la figura

        Returns
        -------
        NDArray[np.int_]
            Matriz que representa el estado de la figura
        """
        return self.matrix
