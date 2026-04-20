def usar_la_fuerza(mochila, indice=0):
    if indice >= len(mochila):
        return False, indice
    
    if mochila[indice] == "sable de luz":
        return True, indice + 1
    
    return usar_la_fuerza(mochila, indice + 1)


mi_mochila = ["comida", "botiquín", "sable de luz", "capa"]
encontrado, cantidad = usar_la_fuerza(mi_mochila)

if encontrado:
    print(f"Se encontró el sable de luz tras sacar {cantidad} objetos.")
else:
    print("No hay sables de luz en la mochila.")