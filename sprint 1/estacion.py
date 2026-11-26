import pyxel
from constantes import TAMANO_CASILLA, ALTO_TABLERO


class Estacion:
    """Representa cada casilla fija de la cocina (encimera, cajón, aparato, suelo, etc.)."""

    def __init__(self, fila: int, col: int, tipo: str):
        """Inicializa la estación con su posición en la cuadrícula y su tipo."""
        # Guardar la posición en la cuadrícula (filas 0-8, columnas 0-11)
        self.__fila = fila
        self.__col = col
        # Tipo de casilla según el mapa ("SU", "EN", "TAB", "C_CEB", etc.)
        self.__tipo = tipo
        # Calcular los píxeles exactos en pantalla (casillas de 16x16, debajo de los 32px del tablero)
        self.__x = col * TAMANO_CASILLA
        self.__y = ALTO_TABLERO + fila * TAMANO_CASILLA
        # Cada estación contiene un solo elemento a la vez (o None si está vacía)
        self.__elemento = None

    @property
    def tipo(self) -> str:
        """Devuelve el código de la estación."""
        return self.__tipo

    @property
    def elemento(self):
        """Devuelve el elemento apoyado en la estación o None si está vacía."""
        return self.__elemento

    @elemento.setter
    def elemento(self, valor):
        """Permite colocar o quitar un único elemento sobre la estación."""
        self.__elemento = valor

    def dibujar(self):
        """Dibuja la casilla de 16x16 píxeles en su posición de la cocina y su contenido."""
        # Diccionario con el color de Pyxel (0-15) asignado a cada tipo de estación
        colores = {
            "SU": 7, "EN": 15, "PA": 5, "PS": 9, "BA": 8,
            "TAB": 11, "BAT": 12, "SA": 12, "PLA": 6, "ENT": 3,
            "FR": 12, "HO": 2, "LA": 6, "MI": 4
        }
        # Todos los cajones de ingredientes van en amarillo (color 10)
        color = 10 if self.__tipo.startswith("C_") else colores.get(self.__tipo, 0)
        # Dibuja el cuadrado relleno y su borde gris (13) de 16x16 píxeles
        pyxel.rect(self.__x, self.__y, TAMANO_CASILLA, TAMANO_CASILLA, color)
        pyxel.rectb(self.__x, self.__y, TAMANO_CASILLA, TAMANO_CASILLA, 13)

        # Si hay un elemento encima (como un plato), lo dibuja sobre la estación
        if self.__elemento is not None:
            self.__elemento.dibujar(self.__x, self.__y)