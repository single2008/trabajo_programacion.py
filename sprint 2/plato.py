import pyxel
import constantes as cte
from ingrediente import Ingrediente


class Plato:
    """
    Representa un plato de la cocina.
    Puede estar vacío, contener una lista de ingredientes en preparación,
    o contener una receta ya cocinada/preparada lista para servir.
    """

    def __init__(self):
        """Inicializa un plato vacío, sin ingredientes ni receta terminada."""
        # Atributos privados inicializados exclusivamente en __init__
        self.__ingredientes = []          # Lista de objetos Ingrediente sueltos
        self.__receta_terminada = None    # Nombre de la receta (str) o None si aún no está hecha
        self.__es_desperdicio = False     # True si se cocinó una mezcla que no corresponde a ninguna receta

    # --- PROPIEDADES ---

    @property
    def ingredientes(self) -> list:
        """Devuelve la lista de ingredientes sueltos que contiene el plato."""
        return self.__ingredientes

    @property
    def receta_terminada(self):
        """Devuelve el nombre de la receta lista para servir, o None si no hay."""
        return self.__receta_terminada

    @property
    def es_desperdicio(self) -> bool:
        """Indica si el plato contiene comida echada a perder (mezcla inválida cocinada)."""
        return self.__es_desperdicio

    # --- CONSULTAS DE ESTADO ---

    def esta_vacio(self) -> bool:
        """
        Comprueba si el plato está completamente vacío.

        Returns:
            bool: True si no tiene ingredientes, ni receta terminada, ni desperdicio.
        """
        return (
            len(self.__ingredientes) == 0
            and self.__receta_terminada is None
            and not self.__es_desperdicio
        )

    def esta_lleno_para_servir(self) -> bool:
        """
        Indica si el plato tiene una receta terminada válida lista para entregar.
        """
        return self.__receta_terminada is not None and not self.__es_desperdicio

    # --- MANIPULACIÓN DEL CONTENIDO ---

    def anadir_ingrediente(self, ingrediente: Ingrediente) -> bool:
        """
        Añade un ingrediente al plato si el plato no tiene ya una receta terminada
        ni comida echada a perder.

        Args:
            ingrediente (Ingrediente): Objeto ingrediente a añadir.

        Returns:
            bool: True si se añadió correctamente, False en caso contrario.
        """
        if self.__receta_terminada is None and not self.__es_desperdicio:
            self.__ingredientes.append(ingrediente)
            return True
        return False

    def transferir_a(self, otro_plato: "Plato") -> bool:
        """
        Vacía el contenido de este plato dentro de otro plato (por ejemplo,
        al juntar ingredientes en la barra central).
        Este plato queda vacío tras la transferencia.

        Args:
            otro_plato (Plato): Plato destino que recibirá el contenido.

        Returns:
            bool: True si se pudo realizar el traspaso, False si no era válido.
        """
        # No se puede traspasar si este plato está vacío o ya es una receta terminada/desperdicio
        if self.esta_vacio() or self.__receta_terminada is not None or self.__es_desperdicio:
            return False

        # Solo se puede traspasar si el plato destino admite ingredientes
        if otro_plato.receta_terminada is None and not otro_plato.es_desperdicio:
            for ing in self.__ingredientes:
                otro_plato.anadir_ingrediente(ing)
            self.vaciar()
            return True
        return False

    def servir_preparacion(self, nombre_receta):
        """
        Carga en un plato vacío el resultado de un aparato (batidora o sartén).

        Args:
            nombre_receta (str | None): Clave de la receta en cte.RECETAS si la mezcla
                                        era válida, o None si la mezcla no coincide con ninguna.
        """
        self.__ingredientes = []
        if nombre_receta is not None:
            self.__receta_terminada = nombre_receta
            self.__es_desperdicio = False
        else:
            self.__receta_terminada = None
            self.__es_desperdicio = True

    def vaciar(self):
        """
        Vacía por completo el contenido del plato (al tirarlo al cubo de basura
        o al meter sus ingredientes en un aparato/tabla). El plato sigue existiendo vacío.
        """
        self.__ingredientes = []
        self.__receta_terminada = None
        self.__es_desperdicio = False

    # --- VALIDACIÓN DE RECETAS ---

    def comprobar_receta(self, aparato: str):
        """
        Comprueba si los ingredientes actuales del plato forman alguna de las recetas
        definidas en cte.RECETAS para el aparato indicado, sin importar el orden.

        Args:
            aparato (str): Código del aparato ('BAT', 'SA', 'TAB', etc.).

        Returns:
            str | None: El nombre de la receta si coincide exactamente, o None si no.
        """
        # Convertimos los ingredientes actuales a sus etiquetas (ej. ['tomate_cortado', 'cebolla_cortada'])
        etiquetas_actuales = sorted([ing.etiqueta_receta() for ing in self.__ingredientes])

        for nombre_receta, datos in cte.RECETAS.items():
            if datos["aparato"] == aparato:
                # Ordenamos ambas listas para comparar contenido exacto sin importar el orden
                if etiquetas_actuales == sorted(datos["ingredientes"]):
                    return nombre_receta
        return None

    # --- DIBUJADO ---

    def dibujar(self, x: int, y: int):
        """
        Dibuja el sprite de 16x16 píxeles del plato en (x, y) según su estado:
        vacío, con ingredientes en curso, con receta terminada o desperdicio.

        Args:
            x (int): Coordenada X en píxeles.
            y (int): Coordenada Y en píxeles.
        """
        if hasattr(cte, "SPRITES_PLATOS"):
            if self.esta_vacio():
                u, v = cte.SPRITES_PLATOS["vacio"]
            elif self.__receta_terminada in cte.SPRITES_PLATOS:
                u, v = cte.SPRITES_PLATOS[self.__receta_terminada]
            elif self.__es_desperdicio and "desperdicio" in cte.SPRITES_PLATOS:
                u, v = cte.SPRITES_PLATOS["desperdicio"]
            else:
                u, v = cte.SPRITES_PLATOS["vacio"]

            pyxel.blt(x, y, 0, u, v, cte.TAMANO_CASILLA, cte.TAMANO_CASILLA, 0)
        else:
            # Representación visual temporal para Sprint 1 antes de tener el .pyxres
            pyxel.circ(x + 8, y + 8, 6, 7)  # Plato blanco
            if self.__receta_terminada is not None:
                pyxel.circ(x + 8, y + 8, 4, 11)  # Verde: receta lista
            elif self.__es_desperdicio:
                pyxel.circ(x + 8, y + 8, 4, 4)   # Marrón: comida quemada/inválida
            elif len(self.__ingredientes) > 0:
                # Dibuja encima el último ingrediente añadido
                self.__ingredientes[-1].dibujar(x, y)