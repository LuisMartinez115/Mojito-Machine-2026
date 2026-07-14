# config.py

TOKEN_SECRETO = "MiCocteleraPrivada2026"

# Mapeo de líquidos a pines GPIO
MOTORES = {
    "ron_blanco": {"pin": 4},
    "vodka": {"pin": 5},
    "blue_curacao": {"pin": 6},
    "vodka": {"pin": 12},
    "malibu_coco": {"pin": 13},
    "tequila": {"pin": 16},
    "agua_mineral": {"pin": 17},
    "volt": {"pin": 22},
    "sprite": {"pin": 23},
    "squirt": {"pin": 24},
    "ginger_ale": {"pin": 25},
    "jugo_naranja": {"pin": 26},
    "jugo_arandano": {"pin": 27},
    "jugo_piña": {"pin": 18},
    "jugo_limon": {"pin": 20},
    "granadina": {"pin": 21}
}

# Recetas (Tiempos de dosificación en segundos)
RECETAS = {
    "mojito": {
        "ron_blanco": 3, 
        "agua_mineral": 1, 
        "jugo_limon": 1.5
    },
    "sex_on_the_beach": {
        "vodka": 3, 
        "jugo_naranja": 5, 
        "jugo_arandano": 2,
        "granadina": 1
    },
    "azulito": {
        "blue_curacao": 2, 
        "volt": 4, 
        "sprite": 4,
        "jugo_limon": 1
    },
    "cantarito": {
        "tequila": 3, 
        "squirt": 5, 
        "jugo_naranja": 3, 
        "jugo_limon": 1
    },
    "shot turquesa":{
        "malibu_coco": 2,
        "blue_curacao": 2,
        "jugo_piña": 1
    },
    "tequila golpeado":{
        "tequila": 3,
        "sprite": 2
    },
    "upside down cake":{
        "vodka": 3,
        "jugo_piña": 3,
        "granadina": 1
    },
    "blue kamikase":{
        "vodka": 3,
        "blue_curacao": 2,
        "jugo_limon": 1
    },
    "lemmon drop":{
        "vodka": 3,
        "jugo_limon": 2    
    }
}