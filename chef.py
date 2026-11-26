import pyxel
from constantes import TAMANO_CASILLA, ALTO_TABLERO


class Chef:
    """Representa a cada uno de los dos chefs"""

    def __int__(self, numero: int, fila: int, col: int, color: int):
        #Identificador del chef (1 para zona superior, 2 para zona inferior)
        self.__numero = numero
        #Posicion en la cuadricula (filas 0-8, columnas 0-11)
        self.__fila = fila
        self.__col = col
        # Direccion hacia la casilla que mira para saber cual tiene delante
        self.__direccion = "abajo" if numero == 1 else "arriba"
        #Elemento que lleva en las manos (un plato o None si va con las manos vacias)
        self.__elemento = None
        # Color para diferenciar al Chef 1 del Chef 2 en el Sprint 1
        self.__color = color

@property
def numero(self) -> int:
    """Devuelve el numero del chef (1 o 2)."""
    return self.__numero

@property
def fila(self) -> int:
    """Devuelve la fila del chef en la cuadricula."""
    return self.__fila

@property
def col(self) -> int:
    """Devuelve la columna del chef en la cuadricula."""
    return self.__col

@property
def direccion(self) -> str:
    """Devuelve la direccion hacia la que mira el chef ("arriba", "abajo", "izquierda", "derecha")."""
    return self.__direccion

@property
def elemento(self):
    """Devuelve el elemento que lleva el chef en las manos o None si va con las manos vacias."""
    return self.__elemento

@elemento.setter
def elemento(self, valor):
    """Permite colocar o quitar el unico elemento sobre las manos del chef."""
    self.__elemento = valor

def dibujar(self):
    """Dibuja al chef en su casilla de 16x16 pixeles e indica hacia donde mira."""
    # Calcular los pixeles exactos en pantalla apartir de su fila y columna en la cuadricula
    x = self.__col * TAMANO_CASILLA
    y = ALTO_TABLERO + self.__fila * TAMANO_CASILLA

    # Dibujar el cuerpo del chef (16x16 pixeles) con un margen de 1px y borde negro (0)
    pyxel.rect(x + 1, y + 1, TAMANO_CASILLA - 2, TAMANO_CASILLA - 2, self.__color)
    pyxel.rectb(x + 1, y + 1, TAMANO_CASILLA - 2, TAMANO_CASILLA - 2, 0)

    #Dibujar un punto blanco pequeño (7) en el borde hacia el que mira
    if self.__direccion == "arriba": 
        pyxel.rect(x + 6, y + 1, 4, 3, 7)
    elif self.__direccion == "abajo":
        pyxel.rect(x + 6, y + 12, 4, 3, 7)
    elif self.__direccion == "izquierda":
        pyxel.rect(x + 1, y + 6, 3, 4, 7)
    elif self.__direccion == "derecha":
        pyxel.rect(x + 12, y + 6, 3, 4, 7)
        pyxel.rect(x + 12, y + 6, 3, 4, 7)
