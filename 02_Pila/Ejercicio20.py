from pila import Stack

def direccion_opuesta(direccion):

    opuestas = {
        "Norte": "Sur",
        "Sur": "Norte",
        "Este": "Oeste",
        "Oeste": "Este",
        "Noreste": "Suroeste",
        "Noroeste": "Sureste",
        "Sureste": "Noroeste",
        "Suroeste": "Noreste"
    }

    return opuestas[direccion]


movimientos = Stack()

movimientos.push((10, "Norte"))
movimientos.push((5, "Este"))
movimientos.push((3, "Sureste"))
movimientos.push((8, "Sur"))


print("Recorrido del Robot")
movimientos.show()


print("\nVolver al punto de partida")

while not movimientos.is_empty():
    pasos, direccion = movimientos.pop()
    print(f"Caminar {pasos} pasos hacia {direccion_opuesta(direccion)}")