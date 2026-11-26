import pyxel
from constantes import MAPA_COCINA, ANCHO_PANTALLA,  ALTO_TABLERO
from estacion import Estacion
from chef import Chef


class Cocina:
    """Gestiona el estado general de la partida, el tablero de estaciones y los chefs."""

    def __init__(self):
        # Construir la matriz de 9x12 elementos Estacion leyendo el mapa de costantes 
        self.__tablero = []
        for fila in range(len(MAPA_COCINA)):
            fila_estaciones = []
            for col in range(len(MAPA_COCINA[fila])):
                tipo = MAPA_COCINA[fila][col]
                fila_estaciones.append(Estacion(fila, col, tipo))
            self.__tablero.append(fila_estaciones)

        # Crear los dos chefs en el centro de sus zonas correspondidas (rojo y azul)
        self.__chef1 = Chef(1, 2, 5, 8)
        self.__chef2 = Chef(2, 6, 5, 12)
        
        # Marcador de puntos y pedidos activos 
        self.__puntuacion = 0
        self.__pedidos = []

    @property
    def tablero(self) -> list:
        """Devuelve la matriz bidimensional de estaciones de la cocina."""
        return self.__tablero

    @property
    def chef1(self) -> Chef:
        """Devuelve el objeto Chef 1 (zona superior)."""
        return self.__chef1

    @property
    def chef2(self) -> Chef:
        """Devuelve el objeto Chef 2 (zona inferior)."""
        return self.__chef2

    @property
    def puntuacion(self) -> int:
        """Devuelve la puntuacion actual de la partida."""
        return self.__puntuacion

    
    def actualizar(self):
        """Actualiza el estado de la partida en cada fotograma (movimiento de chefs, temporizadores, etc.)."""
        pass

    def dibujar(self):
        """Dibujar el tablero superior, todas las estaciones y los dos chefs."""
        # 1. Fondo oscuro (color 1) para el tablero superior donde iran pedidos y puntos
        pyxel.rect(0, 0, ANCHO_VENTANA, ALTO_TABLERO, 1)
        pyxel.text(6, 12, f"PUNTOS: {self.__puntuacion}", 7)

        # 2. Dibujar las 108 casillas del mapa recorriendo cada fila y estacion 
        for fila in self.__tablero:
            for estacion in fila:
                estacion.dibujar()

        # 3. Dibujar a los dos chefs sobre el suelo
        self.__chef1.dibujar()
        self.__chef2.dibujar()
