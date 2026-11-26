import pyxel
import constantes as cte


class Ingrediente:
    """
    Representa un ingrediente individual del juego (cebolla, tomate, huevo, etc.).
    Gestiona su tipo, su estado de corte (entero, cortado, triturado), su estado
    de cocción (crudo, cocinado) y su dibujo en pantalla.
    """

    # Ingredientes que deben cortarse antes de cocinarse o servirse
    __CORTABLES = ("cebolla", "tomate", "chorizo", "patata", "lechuga", "pimiento", "zanahoria", "espinaca")

    # Femenino/masculino para construir la clave exacta de cte.RECETAS (ej. "tomate_cortado" vs "cebolla_cortada")
    __GENERO_FEMENINO = ("cebolla", "patata", "lechuga", "zanahoria", "espinaca")

    def __init__(self, tipo: str):
        """
        Inicializa un ingrediente en su estado original: entero y crudo.

        Args:
            tipo (str): Nombre base del ingrediente en minúsculas (ej. 'cebolla', 'huevo', 'tomate').
        """
        # Todos los atributos son privados y se inicializan aquí
        self.__tipo = tipo
        self.__estado_corte = "entero"      # 'entero', 'cortado' o 'triturado'
        self.__estado_coccion = "crudo"     # 'crudo' o 'cocinado'

    # --- PROPIEDADES ---

    @property
    def tipo(self) -> str:
        """Devuelve el nombre del ingrediente."""
        return self.__tipo

    @property
    def estado_corte(self) -> str:
        """Devuelve el estado de corte ('entero', 'cortado' o 'triturado')."""
        return self.__estado_corte

    @property
    def estado_coccion(self) -> str:
        """Devuelve el estado de cocción ('crudo' o 'cocinado')."""
        return self.__estado_coccion

    # --- MÉTODOS DE COMPORTAMIENTO ---

    def se_puede_cortar(self) -> bool:
        """
        Indica si el ingrediente se puede cortar en la tabla de cortar.
        Solo se corta si pertenece a los ingredientes cortables, está entero y crudo.
        """
        return (
            self.__tipo in self.__CORTABLES
            and self.__estado_corte == "entero"
            and self.__estado_coccion == "crudo"
        )

    def cortar(self) -> bool:
        """
        Corta el ingrediente si es cortable.

        Returns:
            bool: True si se ha cortado, False en caso contrario.
        """
        if self.se_puede_cortar():
            self.__estado_corte = "cortado"
            return True
        return False

    def triturar(self):
        """Procesa el ingrediente en la batidora cambiando su corte a 'triturado'."""
        self.__estado_corte = "triturado"

    def cocinar(self):
        """Procesa el ingrediente en la sartén cambiando su cocción a 'cocinado'."""
        self.__estado_coccion = "cocinado"

    def etiqueta_receta(self) -> str:
        """
        Devuelve el identificador del ingrediente con el formato usado en cte.RECETAS
        (por ejemplo: 'huevo', 'tomate_cortado' o 'cebolla_cortada').
        """
        if self.__estado_corte == "cortado":
            terminacion = "cortada" if self.__tipo in self.__GENERO_FEMENINO else "cortado"
            return f"{self.__tipo}_{terminacion}"
        return self.__tipo

    # --- DIBUJADO ---

    def dibujar(self, x: int, y: int):
        """
        Dibuja el sprite de 16x16 píxeles del ingrediente en las coordenadas (x, y).
        Usa el sprite de 'cortado' o 'entero' según su estado actual.

        Args:
            x (int): Coordenada X en píxeles.
            y (int): Coordenada Y en píxeles.
        """
        # Si tenéis un diccionario SPRITES_INGREDIENTES en constantes.py, lo usa;
        # si aún no está definido, dibuja un indicador provisional de Sprint 1.
        if hasattr(cte, "SPRITES_INGREDIENTES") and self.__tipo in cte.SPRITES_INGREDIENTES:
            clave_estado = "cortado" if self.__estado_corte == "cortado" else "entero"
            u, v = cte.SPRITES_INGREDIENTES[self.__tipo][clave_estado]
            pyxel.blt(x, y, 0, u, v, cte.TAMANO_CASILLA, cte.TAMANO_CASILLA, 0)
        else:
            # Representación visual temporal hasta cargar el fichero .pyxres
            color = 10 if self.__estado_corte == "cortado" else 9
            pyxel.rect(x + 4, y + 4, 8, 8, color)