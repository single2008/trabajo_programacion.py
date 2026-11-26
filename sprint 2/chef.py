import pyxel
from constantes import TAMANO_CASILLA, ALTO_TABLERO


class Chef:
    """Representa a cada uno de los dos chefs."""

    def __init__(self, numero: int, fila: int, col: int, color: int):
        """Inicializa al chef con su identificador, posición inicial, dirección y color."""
        # Identificador del chef (1 para zona superior, 2 para zona inferior)
        self.__numero = numero
        # Posición en la cuadrícula (filas 0-8, columnas 0-11)
        self.__fila = fila
        self.__col = col
        # Dirección hacia la casilla que mira para saber cuál tiene delante
        self.__direccion = "abajo" if numero == 1 else "arriba"
        # Elemento que lleva en las manos (un plato o None si va con las manos vacías)
        self.__elemento = None
        # Color para diferenciar al Chef 1 del Chef 2
        self.__color = color

    # --- PROPIEDADES ---

    @property
    def numero(self) -> int:
        """Devuelve el número del chef (1 o 2)."""
        return self.__numero

    @property
    def fila(self) -> int:
        """Devuelve la fila del chef en la cuadrícula."""
        return self.__fila

    @property
    def col(self) -> int:
        """Devuelve la columna del chef en la cuadrícula."""
        return self.__col

    @property
    def direccion(self) -> str:
        """Devuelve la dirección hacia la que mira el chef ('arriba', 'abajo', 'izquierda', 'derecha')."""
        return self.__direccion

    @property
    def elemento(self):
        """Devuelve el elemento que lleva el chef en las manos o None si va con las manos vacías."""
        return self.__elemento

    @elemento.setter
    def elemento(self, valor):
        """Permite colocar o quitar el único elemento sobre las manos del chef."""
        self.__elemento = valor

    # --- MOVIMIENTO Y COLISIONES ---

    def mover(self, d_fila: int, d_col: int, nueva_direccion: str, tablero: list):
        """
        Gira al chef hacia la dirección indicada e intenta desplazarlo una casilla
        si el destino está dentro de los límites y es suelo ('SU').

        Args:
            d_fila (int): Desplazamiento vertical (-1 arriba, +1 abajo, 0 quieto).
            d_col (int): Desplazamiento horizontal (-1 izquierda, +1 derecha, 0 quieto).
            nueva_direccion (str): Dirección a la que pasa a mirar el chef.
            tablero (list): Matriz 9x12 de objetos Estacion de la cocina.
        """
        # El chef siempre gira hacia la tecla pulsada, aunque luego choque y no avance
        self.__direccion = nueva_direccion

        nueva_fila = self.__fila + d_fila
        nueva_col = self.__col + d_col

        # Comprobar que no se sale de los bordes de la cuadrícula (9 filas x 12 columnas)
        if 0 <= nueva_fila < len(tablero) and 0 <= nueva_col < len(tablero[0]):
            # Solo puede caminar sobre casillas de suelo ('SU'); bloquea encimeras y barra central
            if tablero[nueva_fila][nueva_col].tipo == "SU":
                self.__fila = nueva_fila
                self.__col = nueva_col

    def casilla_delante(self) -> tuple:
        """
        Calcula las coordenadas (fila, col) de la casilla que el chef tiene justo delante.
        Será clave en el Sprint 3 para interactuar con estaciones y platos.
        """
        desplazamientos = {
            "arriba": (-1, 0),
            "abajo": (1, 0),
            "izquierda": (0, -1),
            "derecha": (0, 1),
        }
        df, dc = desplazamientos[self.__direccion]
        return (self.__fila + df, self.__col + dc)

    # --- DIBUJADO ---

    def dibujar(self):
        """Dibuja al chef en su casilla de 16x16 píxeles e indica hacia dónde mira."""
        # Calcular los píxeles exactos en pantalla a partir de su fila y columna en la cuadrícula
        x = self.__col * TAMANO_CASILLA
        y = ALTO_TABLERO + self.__fila * TAMANO_CASILLA

        # Dibujar el cuerpo del chef (16x16 píxeles) con un margen de 1px y borde negro (0)
        pyxel.rect(x + 1, y + 1, TAMANO_CASILLA - 2, TAMANO_CASILLA - 2, self.__color)
        pyxel.rectb(x + 1, y + 1, TAMANO_CASILLA - 2, TAMANO_CASILLA - 2, 0)

        # Dibujar un punto blanco pequeño (7) en el borde hacia el que mira
        if self.__direccion == "arriba":
            pyxel.rect(x + 6, y + 1, 4, 3, 7)
        elif self.__direccion == "abajo":
            pyxel.rect(x + 6, y + 12, 4, 3, 7)
        elif self.__direccion == "izquierda":
            pyxel.rect(x + 1, y + 6, 3, 4, 7)
        elif self.__direccion == "derecha":
            pyxel.rect(x + 12, y + 6, 3, 4, 7)

        # Si el chef lleva un elemento en las manos, lo dibuja encima
        if self.__elemento is not None:
            self.__elemento.dibujar(x, y)