# Dimensiones de la pantalla y cuadrícula
ANCHO_PANTALLA = 192
ALTO_PANTALLA = 176
ALTO_TABLERO = 32
TAMANO_CASILLA = 16
FPS = 30
ESCALA_PANTALLA = 4


DURACION_SERVICIO_SEG = 180
MAX_FALLOS = 3

# Mapa de la cocina (9 filas x 12 columnas)
# SU=Suelo, EN=Encimera, PA=Pared, FR=Frigorífico, HO=Horno, LA=Lavadora, MI=Microondas, PS=Paso, BA=Basura
# C_CEB=Cebolla, C_TOM=Tomate, C_HUE=Huevo, C_CHO=Chorizo, C_LEC=Lechuga, C_PAT=Patata, C_PIM=Pimiento, C_ZAN=Zanahoria, C_ESP=Espinaca
# TAB_Tabla, BAT=Batidora, SA=Sartén, PLA=Platos, ENT=Entrega, 
MAPA_COCINA = [["C_CEB", "C_HUE", "C_CHO", "C_LEC", "TAB", "C_PIM", "BAT", "HO", "MI", "FR", "EN", "ENT"],
 ["SU"] * 12,
 ["SU"] * 12,
 ["SU"] * 12,
[ "PA", "PS", "PA", "PS", "PA", "BA", "PA", "PS", "PA", "PA", "PS", "PA"],
 ["SU"] * 12,
 ["SU"] * 12,
 ["SU"] * 12,
 ["C_TOM", "C_PAT", "C_ZAN", "C_ESP", "EN", "TAB", "EN", "SA", "EN", "PLA", "LA", "EN"]
]

# Diccionario de recetas
RECETAS = {
   "gazpacho": {
        "aparato": "BAT",
        "ingredientes": ["tomate_cortado", "cebolla_cortda"],
        "puntos": 10,
        "penalización": 5,
        "tiempo": 48
},
"tortilla": {
        "aparato": "SA",
        "ingredientes": ["patata_cortada", "cebolla_cortada", "huevo"],
        "puntos": 12,
        "penalización": 6,
        "tiempo": 60
},
"huevos_chorizo": {
        "aparato": "SA",
        "ingredientes": ["huevo", "patata_cortada", "chorizo_cortado"],
        "puntos": 12,
        "penalización": 6,
        "tiempo": 60
},
"ensalada_mixta": {
    "aparato": "TAB",
    "ingredientes": ["lechuga_cortada", "tomate_cortado", "cebolla_cortada"],
    "puntos": 11,
    "penalizacion": 5,
    "tiempo": 45
},
"pisto_manchego": {
    "aparato": "SA",
    "ingredientes": ["tomate_cortado", "pimiento_cortado","cebolla_cortada"],
    "puntos": 13,
    "penalizacion": 6,
    "tiempo": 55
},
"crema_espinacas": {
    "aparato": "BAT",
    "ingredientes": ["espinaca_cortada", "patata_cortada", "zanahoria_cortada"],
    "puntos": 14,
    "penalizacion": 7,
    "tiempo": 60

}}
