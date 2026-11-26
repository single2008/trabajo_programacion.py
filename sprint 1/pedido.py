import pyxel
import constantes as cte


class Pedido:
    """
    Representa una comanda activa en el tablero superior.
    Almacena la receta solicitada, los puntos y penalización asociados,
    el contador de tiempo en fotogramas y su representación gráfica.
    """

    def __init__(self, nombre_receta: str):
        """
        Inicializa un pedido a partir de una clave válida de cte.RECETAS.

        Args:
            nombre_receta (str): Nombre de la receta (ej. 'gazpacho', 'tortilla', 'huevos_chorizo').
        """
        # Todos los atributos son privados y se inicializan exclusivamente en __init__
        self.__nombre_receta = nombre_receta

        # Extraemos los datos fijos desde el diccionario de constantes
        datos_receta = cte.RECETAS[nombre_receta]
        self.__ingredientes = list(datos_receta["ingredientes"])
        self.__aparato = datos_receta["aparato"]
        self.__puntos = datos_receta["puntos"]
        # Usamos .get() para evitar errores si alguna clave aún tiene tilde en constantes.py
        self.__penalizacion = datos_receta.get("penalizacion", datos_receta.get("penalización", 0))

        # El tiempo se controla en fotogramas (segundos * FPS)
        self.__tiempo_total_frames = datos_receta["tiempo"] * cte.FPS
        self.__tiempo_restante_frames = self.__tiempo_total_frames

    # --- PROPIEDADES ---

    @property
    def nombre_receta(self) -> str:
        """Devuelve el identificador de la receta del pedido."""
        return self.__nombre_receta

    @property
    def ingredientes(self) -> list:
        """Devuelve la lista de ingredientes requeridos para esta comanda."""
        return self.__ingredientes

    @property
    def puntos(self) -> int:
        """Devuelve los puntos que otorga completar este pedido."""
        return self.__puntos

    @property
    def penalizacion(self) -> int:
        """Devuelve los puntos que se restan si este pedido caduca."""
        return self.__penalizacion

    @property
    def tiempo_restante_seg(self) -> int:
        """Devuelve el tiempo restante redondeado hacia arriba en segundos."""
        return (self.__tiempo_restante_frames + cte.FPS - 1) // cte.FPS

    # --- LÓGICA DE TIEMPO Y VALIDACIÓN ---

    def actualizar(self):
        """
        Descuenta un fotograma del tiempo disponible del pedido.
        Debe llamarse una vez por frame desde la actualización del juego.
        """
        if self.__tiempo_restante_frames > 0:
            self.__tiempo_restante_frames -= 1

    def ha_caducado(self) -> bool:
        """
        Comprueba si se ha agotado el tiempo límite de la comanda.

        Returns:
            bool: True si el tiempo llegó a 0, False mientras siga activo.
        """
        return self.__tiempo_restante_frames <= 0

    def coincide_con(self, receta_entregada: str) -> bool:
        """
        Comprueba si el plato entregado en el mostrador corresponde a este pedido.

        Args:
            receta_entregada (str): Nombre de la receta terminada en el plato.

        Returns:
            bool: True si coincide exactamente con la receta pedida.
        """
        return self.__nombre_receta == receta_entregada

    # --- REPRESENTACIÓN VISUAL EN EL TABLERO ---

    def dibujar(self, x: int, y: int):
        """
        Dibuja la tarjeta de la comanda en el tablero superior (alto máximo 32 px).
        Incluye el icono del plato terminado, los ingredientes y la barra de tiempo.

        Args:
            x (int): Coordenada X donde empieza la tarjeta de este pedido.
            y (int): Coordenada Y donde empieza la tarjeta (normalmente 2).
        """
        ancho_tarjeta = 38
        alto_tarjeta = 28

        # 1. Fondo y borde de la comanda
        pyxel.rect(x, y, ancho_tarjeta, alto_tarjeta, 1)
        pyxel.rectb(x, y, ancho_tarjeta, alto_tarjeta, 7)

        # 2. Barra de tiempo en la parte superior de la tarjeta (cambia de verde a rojo)
        proporcion = self.__tiempo_restante_frames / self.__tiempo_total_frames
        ancho_barra = int((ancho_tarjeta - 4) * proporcion)
        color_barra = 11 if proporcion > 0.5 else (9 if proporcion > 0.25 else 8)
        pyxel.rect(x + 2, y + 2, ancho_barra, 3, color_barra)

        # 3. Icono del plato terminado (sprite 16x16 si existe, o texto abreviado en Sprint 1)
        if hasattr(cte, "SPRITES_PLATOS") and self.__nombre_receta in cte.SPRITES_PLATOS:
            u, v = cte.SPRITES_PLATOS[self.__nombre_receta]
            pyxel.blt(x + 2, y + 6, 0, u, v, cte.TAMANO_CASILLA, cte.TAMANO_CASILLA, 0)
        else:
            # Iniciales de la receta (ej. "GAZ", "TOR", "HUE") mientras se crean los sprites
            etiqueta = self.__nombre_receta[:3].upper()
            pyxel.text(x + 4, y + 9, etiqueta, 7)

        # 4. Indicadores de los ingredientes necesarios a la derecha del icono
        for i, ing in enumerate(self.__ingredientes):
            if hasattr(cte, "SPRITES_MINI_INGREDIENTES") and ing in cte.SPRITES_MINI_INGREDIENTES:
                u, v = cte.SPRITES_MINI_INGREDIENTES[ing]
                pyxel.blt(x + 20, y + 6 + i * 6, 0, u, v, 6, 6, 0)
            else:
                # Inicial de cada ingrediente (ej. T, C, H, P) en Sprint 1
                pyxel.text(x + 22, y + 6 + i * 6, ing[0].upper(), 10)