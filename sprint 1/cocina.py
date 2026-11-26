import pyxel
from constantes import (
    MAPA_COCINA,
    ANCHO_PANTALLA,
    ALTO_TABLERO,
    DURACION_SERVICIO_SEG,
    MAX_FALLOS,
    FPS,
)
from estacion import Estacion
from chef import Chef
from pedido import Pedido


class Cocina:
    """Gestiona el estado general de la partida, el tablero de estaciones, pedidos y chefs."""

    def __init__(self):
        """Inicializa el tablero de estaciones, los dos chefs y los contadores del servicio."""
        # Construir la matriz de 9x12 elementos Estacion leyendo el mapa de constantes
        self.__tablero = []
        for fila in range(len(MAPA_COCINA)):
            fila_estaciones = []
            for col in range(len(MAPA_COCINA[fila])):
                tipo = MAPA_COCINA[fila][col]
                fila_estaciones.append(Estacion(fila, col, tipo))
            self.__tablero.append(fila_estaciones)

        # Crear los dos chefs en el centro de sus zonas correspondientes
        self.__chef1 = Chef(1, 2, 5, 8)
        self.__chef2 = Chef(2, 6, 5, 12)

        # Contadores del tablero superior y lista de pedidos activos
        self.__puntuacion = 0
        self.__fallos = 0
        self.__tiempo_servicio_frames = DURACION_SERVICIO_SEG * FPS
        self.__pedidos = []

        # (Opcional para probar visualmente en Sprint 1 que los pedidos se dibujan bien;
        # en Sprint 4 se generarán automáticamente cada ciertos segundos)
        self.__pedidos.append(Pedido("gazpacho"))

    # --- PROPIEDADES ---

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
        """Devuelve la puntuación actual de la partida."""
        return self.__puntuacion

    @property
    def fallos(self) -> int:
        """Devuelve el número de fallos acumulados."""
        return self.__fallos

    @property
    def pedidos(self) -> list:
        """Devuelve la lista de objetos Pedido activos en espera."""
        return self.__pedidos

    # --- ACTUALIZACIÓN Y DIBUJADO ---

    def actualizar(self):
        """Actualiza el estado de la partida en cada fotograma."""
        pass

    def __dibujar_tablero_superior(self):
        """
        Dibuja la franja superior de 192x32 px:
        - Izquierda: hasta 3 pedidos en espera.
        - Derecha: puntuación, contador de fallos y reloj del servicio.
        """
        # Fondo oscuro del tablero de comandas
        pyxel.rect(0, 0, ANCHO_PANTALLA, ALTO_TABLERO, 1)

        # 1. Pedidos activos a la izquierda (x = 2, 42, 82)
        for i, pedido in enumerate(self.__pedidos):
            pedido.dibujar(2 + i * 40, 2)

        # 2. Indicadores a la derecha (a partir de x = 126 para no pisar los 3 pedidos)
        minutos = (self.__tiempo_servicio_frames // FPS) // 60
        segundos = (self.__tiempo_servicio_frames // FPS) % 60
        texto_reloj = f"{minutos:02d}:{segundos:02d}"

        pyxel.text(126, 3, f"PTS:{self.__puntuacion}", 7)
        pyxel.text(126, 13, f"ERR:{self.__fallos}/{MAX_FALLOS}", 8)
        pyxel.text(126, 23, f"TIME:{texto_reloj}", 10)

    def dibujar(self):
        """Dibuja el tablero superior, todas las estaciones y los dos chefs."""
        # 1. Tablero de comandas (pedidos, puntos, fallos y reloj)
        self.__dibujar_tablero_superior()

        # 2. Dibujar las 108 casillas del mapa recorriendo cada fila y estación
        for fila in self.__tablero:
            for estacion in fila:
                estacion.dibujar()

        # 3. Dibujar a los dos chefs sobre el suelo
        self.__chef1.dibujar()
        self.__chef2.dibujar()