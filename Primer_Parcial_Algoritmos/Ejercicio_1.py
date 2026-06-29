#Ejercicio 1: Dado una lista simple de python (array) de 15 superheroes realizar dos funciones recursivas:
# a. funcion recursiva  para buscar, determinar si Capitan America esta en la lista.
# b. funcion recursiva para listar los superheroes de la lista.


from lista import List
from super_heroes_data import superheroes


def buscar_capitan_america(lista_heroes: List) -> bool:
    
    if lista_heroes.size() == 0:
        return False
    
    heroe_actual = lista_heroes[0]
    

    if heroe_actual.get('name') == 'Captain America' or heroe_actual.get('alias') == 'Captain America':
        return True
    
    
    resto_de_la_lista = List()
    resto_de_la_lista.extend(lista_heroes[1:])
    
    return buscar_capitan_america(resto_de_la_lista)



def listar_superheroes(lista_heroes: List) -> None:

    if lista_heroes.size() == 0:
        return
    
    heroe_actual = lista_heroes[0]
    print(f"Nombre: {heroe_actual.get('name')} | Alias: {heroe_actual.get('alias')}")
    
    resto_de_la_lista = List()
    resto_de_la_lista.extend(lista_heroes[1:])
 
    listar_superheroes(resto_de_la_lista)




print("Ejercicio 1:")
lista_simple_15 = superheroes[:15]

mis_heroes = List()
mis_heroes.extend(lista_simple_15)

print("\nLista de Superhéroes:")
listar_superheroes(mis_heroes)

print("\nBúsqueda del Capitán América:")
encontrado = buscar_capitan_america(mis_heroes)

if encontrado:
    print("El Capitán América se encuentra en la lista.")
else:
    print("No se encontró al Capitán América entre los superhéroes.")