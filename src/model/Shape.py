import numpy as np
from numpy.typing import NDArray
from dataclasses import dataclass
from src.model.Node import Node, CNode


class Shape:
    """Clase genérica de figura"""

    node: CNode[NDArray[np.int_]]

    def __init__(self, matrix: NDArray[np.int_]):
        # ? Creamos un nodo
        # ? Creamos un nodo y nos colocamos ahí
        self.node = CNode(value=matrix)

        # ? Creamos los nodos vecinos
        self.node.connect_right(value=np.rot90(matrix, -1))
        self.node.connect_left(value=np.rot90(matrix, 1))

        # ? A través del nodo de la derecha, accedemos a la derecha de nuevo
        self.node.right.connect_right(value=np.rot90(matrix, -2))

        # ? Conectamos este ultimo nodo con el nodo de hasta la izquierda
        self.node.left.left = self.node.right.right

    def rotate_right(self) -> NDArray[np.int_]:
        """Rota la figura 90º hacia la derecha desplazándose a través del nodo 

        Returns
        -------
        NDArray[np.int_]
            La nueva matriz rotada
        """

        self.node = self.node.right
        return np.rot90(self.matrix, -1)

    def rotate_left(self) -> NDArray[np.int_]:
        """Rota la figura 90º hacia la izquierda desplazándose a través del nodo

        Returns
        -------
        NDArray[np.int_]
            La nueva matriz rotada
        """
        self.node = self.node.left
        return np.rot90(self.matrix, 1)

    def get_rotate_right(self) -> NDArray[np.int_]:
        """Obtén la figura rotada 90º hacia la derecha desplazándose a través del nodo 

        Returns
        -------
        NDArray[np.int_]
            La nueva matriz rotada
        """

        self.node = self.node.right
        return self.node.right.value

    def get_rotate_left(self) -> NDArray[np.int_]:
        """Obtén la figura rotada 90º hacia la izquierda desplazándose a través del nodo

        Returns
        -------
        NDArray[np.int_]
            La nueva matriz rotada
        """

        return self.node.left.value

    @property
    def matrix(self):
        return self.node.value
