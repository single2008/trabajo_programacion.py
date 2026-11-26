import pyxel
from constantes import ANCHO_VENTANA, ALTO_VENTANA
from cocina import Cocina


class Juego:
    """Clase principal que inicia la ventana de Pyxel y conecta con la cocina."""

    def __init__(self):
        # Inicializar la ventana con las dimensiones definidas en constantes.py
        pyxel.init(ANCHO_VENTANA, ALTO_VENTANA, title="Service Rush")
        # Crear la cocina con todas sus estaciones y chefs
        self.__cocina = Cocina()
        # Iniciar el bucle principal de Pyxel (update y draw)
        pyxel.run(self.update, self.draw)

    def update(self):
        """Actualizar el estado del juego en cada fotograma."""
        self.__cocina.actualizar()

    def draw(self):
        """Dibujar el estado actual de la pantalla y limpiarla."""
        pyxel.cls(0)
        self.__cocina.dibujar()

if __name__ == "__main__":
    Juego()
    
