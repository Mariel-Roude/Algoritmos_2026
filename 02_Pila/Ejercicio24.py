from pila import Stack


personajes = Stack()


personajes.push(("Iron Man", 10))
personajes.push(("Rocket Raccoon", 4))
personajes.push(("Groot", 5))
personajes.push(("Black Widow", 8))
personajes.push(("Captain America", 11))
personajes.push(("Doctor Strange", 6))
personajes.push(("Gamora", 5))


aux = Stack()

posicion = 1


print("A) Posición de Rocket Raccoon y Groot\n")

while not personajes.is_empty():

    personaje = personajes.pop()

    nombre = personaje[0]
    peliculas = personaje[1]

    if nombre == "Rocket Raccoon":
        print("Rocket Raccoon está en posición:", posicion)

    if nombre == "Groot":
        print("Groot está en posición:", posicion)

    aux.push(personaje)

    posicion += 1



while not aux.is_empty():
    personajes.push(aux.pop())



print("\nB) Personajes con más de 5 películas\n")


while not personajes.is_empty():

    personaje = personajes.pop()

    nombre = personaje[0]
    peliculas = personaje[1]

    if peliculas > 5:
        print(nombre, "-", peliculas, "películas")

    aux.push(personaje)


while not aux.is_empty():
    personajes.push(aux.pop())



print("\nC) Películas de Black Widow\n")


while not personajes.is_empty():

    personaje = personajes.pop()

    nombre = personaje[0]
    peliculas = personaje[1]

    if nombre == "Black Widow":
        print("Black Widow participó en", peliculas, "películas")

    aux.push(personaje)


while not aux.is_empty():
    personajes.push(aux.pop())



print("\nD) Personajes que empiezan con C, D y G\n")


while not personajes.is_empty():

    personaje = personajes.pop()

    nombre = personaje[0]

    inicial = nombre[0]

    if inicial in ["C", "D", "G"]:
        print(nombre)

    aux.push(personaje)


while not aux.is_empty():
    personajes.push(aux.pop())