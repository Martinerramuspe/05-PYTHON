# DICCIONARIO: SE INTEGRA SI O SI CON ELEMENTOS DE TIPO  CLAVE-VALOR.

# COMPLEJIDAD 1-------------------------------------------------------------------------------------
usuarios_1 = {"juan":3,"martin":"Tecnico","agustin": 11.3} #defincion de diccionario clave-valor
usuarios_1["martin"] 



# COMPLEJIDAD 2: Diccionario dentro del valor de las claves-----------------------------------------
usuarios_2 = {"juan": {"edad":44, "rol": "ingenierio"}, #definicion de diccionario clave-valor dentro de otro diccionario
            "martin": {"edad":34, "rol": "data_ciences"},
            "agustin": {"edad":14, "rol": "tecnico"}}
usuarios_2
usuarios_2["juan"]["edad"] # llamado de clave-valor

# COMPLEJDIAD 3: Lista dentro de diccionario1, y diccionario 1 dentro de diccionario 2---------------
usuarios_3 = {
    "juan": {"edad": 44, "roles": ["ingeniero", "analista"]},
    "martin": {"edad": 34, "roles": ["data_ciences", "desarrollador"]},
    "agustin": {"edad": 14, "roles": ["tecnico", "estudiante"]}
}
usuarios_3["juan"]["roles"] #llamado de clave-valor
type(usuarios_3["juan"]["roles"])

# COMPLEJIDAD 4-------------------------------------------------------------------------------------
usuarios_4 = {
    "juan": {"edad": 44, "roles": {"diurnos": ["ingeniero", "analista"], "nocturnos": ["soporte"]}},
    "martin": {"edad": 34, "roles": {"diurnos": ["data_ciences", "desarrollador"], "nocturnos": ["analista"]}},
    "agustin": {"edad": 14, "roles": {"diurnos": ["tecnico", "estudiante"], "nocturnos": ["profee"]}}
}
usuarios_4["juan"]

# OBSERVACION_001: No definior los diccionarios con ":", siempre con "=".

# LAS CLAVES, TIENEN QUE SER VALOREES UNICOS, QUE PASA SI NO SE CUMPLE ESO?
# agregamos otro juan.
usuarios = {"juan": {"edad":44, "rol": "ingenierio"},
            "martin": {"edad":34, "rol": "data_ciences"},
            "juan": {"edad":14, "rol": "tecnico"}}
print(f"Como podes ver el diccionario toma el ultimo juan{usuarios} ") # Designa la ultima clave definida.