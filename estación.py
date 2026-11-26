import pyxel
from constantes import TAMANO_CASILLA, ALTO_TABLERO


class Estacion:
    """Representa cada casilla fija de la cocina (encimera, cajon, aparato, suelo, etc)."""

    def__init__(self, fila: int, col: int, tipo: str):
        #Guardar la posicion en la cuadricula (filas 0-8, columnas 0-11)
        self.__fila = fila
        self.__col = col
        #Tipo de casilla segun el mapa ("SU", "EN", "TAB, "C_CEB", etc.)
        self.__tipo = tipo
        #Calcular os pixeles exactos en pantalla (casillas de 16x16, debajo de los 32px del tablero)
        self.__x = col * TAMANO_CASILLA
        self.__y = ALTO_TABLERO + fila * TAMANO_CASILLA
        #Cada estacion contiene un solo elemento a la vez (o None si esta vacia)
        self.__elemento = None

@property
def tipo(self) -> str:
    "Devuelve el codigo de la estacion"""
    return self.__tipo

@property
def elemento(self):
    """Devuelve el elemento apoyado en la estacion o None si esta vacia"""
    return self.__elemento

@elemento.setter
def elemento(self, valor):
    """Permite colocar o quitar un unico elemento sobre la estacion."""
    self.__elemento = valor

def dibujar(self):
    """Dibuja la casilla de 16x16 pixeles en su posicion de la cocina."""
    #Diccionario con el color de Pyxel (0-15) asignado a cada tipo de estacion.
    colores = {
        "SU": 7, "EN": 15, "PA": 5, "PS": 9, "BA": 8,
        "TAB": 11, "BAT": 12, "SAR"_:12, "PLA": 6, "ENT": 3,
        "FR": 12, "HO": 2, "LA": 6, "MI": 4
    }
    #Todos los cajones de ingredientes van en amarillo (color 10)
    color=10 if self.__tipo.startswith("C_") else colores.get(self.__tipo, 0)
    #Dibuja el cuadrado relleno y su borde gris (13) de 16x16 pixeles 
    pyxel.rect(self.__x, self.__y, TAMANO_CASILLA, TAMANO_CASILLA, color)
    pyxel.rectb(self.__x, self.__y, TAMANO_CASILLA, TAMAÑO_CASILLA, 13)



    

        
