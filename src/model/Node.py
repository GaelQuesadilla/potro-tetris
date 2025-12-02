from __future__ import annotations
from dataclasses import dataclass
from typing import Generic, TypeVar, Optional

T = TypeVar("T")


@dataclass
class Node(Generic[T]):
    """Clase que representa un nodo"""

    value: T
    left: Optional[Node[T]] = None
    right: Optional[Node[T]] = None

    def connect_right(self, value: T):
        """Crea un nodo a la derecha y lo enlaza con el nodo actual

        Parameters
        ----------
        value : T
            Valor que contendrá el nodo
        """
        node: Node[T] = Node(value=value)
        self.right = node
        node.left = self

    def connect_left(self, value: T):
        """Crea un nodo a la izquierda y lo enlaza con el nodo actual

        Parameters
        ----------
        value : T
            Valor que contendrá el nodo
        """
        node: Node[T] = Node(value=value)
        self.left = node
        node.right = self


@dataclass
class CNode(Node):
    """Clase que representa un el nodo de un grafo que siempre será circular"""
    value: T
    left: Node[T]
    right: Node[T]

    def __init__(self, value: T):
        self.value = value
        self.left = self
        self.right = self

    def connect_right(self, value: T):
        """Crea un nodo a la derecha y lo enlaza con el nodo actual

        Parameters
        ----------
        value : T
            Valor que contendrá el nodo
        """
        node = Node(value)
        node.right = self.right
        node.left = self
        self.right.left = node
        self.right = node

    def connect_left(self, value: T):
        node = Node(value)
        node.left = self.left
        node.right = self
        self.left.right = node
        self.left = node
