#Ejercicio 2: Dada una lista de personajes de marvel (usar el archivo adjunto) debe tener 100 o mas, resolver:
# a. Listado ordenado de manera ascendente por nombre de los personajes.
# b. Determinar en que posicion esta The Thing y Rocket Raccoon.
# c. Listar todos los villanos de la lista.
# d. Poner todos los villanos en una cola para determinar luego cuales aparecieron antes de 1980.
# e. Listar los superheores que comienzan con  Bl, G, My, y W.
# f. Listado de personajes ordenado por nombre real de manera ascendente de los personajes.
# g. Listado de superheroes ordenados por fecha de aparación.
# h. Modificar el nombre real de Ant Man a Scott Lang.
# i. Mostrar los personajes que en su biografia incluyan la palabra time-traveling o suit.
# j. Eliminar a Electro y Baron Zemo de la lista y mostrar su información si estaba en la lista.

from lista import List
from cola import Queue
from super_heroes_data import superheroes


def criterio_nombre(heroe):
    return heroe.get('name', '')


def criterio_nombre_real(heroe):
    nombre_real = heroe.get('real_name')
    
    if nombre_real is None:
        return heroe.get('name', '')
        
    return str(nombre_real)


def criterio_aparicion(heroe):
    return heroe.get('first_appearance', 0)


lista_marvel = List()
lista_marvel.extend(superheroes)

lista_marvel.add_criterion('por_nombre', criterio_nombre)
lista_marvel.add_criterion('por_nombre_real', criterio_nombre_real)
lista_marvel.add_criterion('por_aparicion', criterio_aparicion)




print("Ejercicio 2:")

print("\na. Personajes ordenados por nombre ascendente:")
lista_marvel.sort_by_criterion('por_nombre')
for p in lista_marvel:
    print(f"• {p.get('name')}")


print("\nb. Posición de The Thing y Rocket Raccoon:")
posicion_thing = lista_marvel.search('The Thing', criterion='por_nombre')
posicion_rocket = lista_marvel.search('Rocket Raccoon', criterion='por_nombre')

if posicion_thing is not None:
    print(f"• The Thing se encuentra en la posición: {posicion_thing}")
else:
    print("• The Thing no se encuentra en la lista.")

if posicion_rocket is not None:
    print(f"• Rocket Raccoon se encuentra en la posición: {posicion_rocket}")
else:
    print("• Rocket Raccoon no se encuentra en la lista.")



print("\nc. Listado de todos los villanos de la lista:")
for p in lista_marvel:
    if p.get('is_villain') == True:
        print(f"• Villano: {p.get('name')} (Alias: {p.get('alias')})")



print("\nd. Villanos con aparición antes de 1980:")
cola_villanos = Queue()

for p in lista_marvel:
    if p.get('is_villain') == True:
        cola_villanos.arrive(p)

tamanio_cola = cola_villanos.size()

for i in range(tamanio_cola):
    villano_actual = cola_villanos.attention()
    anio = villano_actual.get('first_appearance', 0)
    
    if anio < 1980:
        print(f"• {villano_actual.get('name')} ({anio})")
        
    cola_villanos.arrive(villano_actual)



print("\ne. Superhéroes que empiezan con Bl, G, My, o W")
iniciales = ('Bl', 'G', 'My', 'W')
for p in lista_marvel:
    if not p.get('is_villain'):
        nombre = p.get('name', '')
        if nombre.startswith(iniciales):
            print(f"• {nombre}")



print("\nf. Personajes ordenados por Nombre Real de manera ascendente:")
lista_marvel.sort_by_criterion('por_nombre_real')
for p in lista_marvel:
    print(f"• Nombre Real: {p.get('real_name')} | Personaje: {p.get('name')}")


print("\ng. Superhéroes ordenados por fecha de aparición:")
lista_marvel.sort_by_criterion('por_aparicion')
for p in lista_marvel:
    if not p.get('is_villain'):
        print(f"• Año: {p.get('first_appearance')} | Héroe: {p.get('name')}")



print("\nh. Modificacion del nombre real de Ant Man a Scott Lang: ")
posicion_antman = lista_marvel.search('Ant Man', criterion='por_nombre')
if posicion_antman is not None:
    lista_marvel[posicion_antman]['real_name'] = 'Scott Lang'
    print(f"Se modificaron los datos del personaje: {lista_marvel[posicion_antman]}")
else:
    posicion_antman = lista_marvel.search('Ant-Man', criterion='por_nombre')
    if posicion_antman is not None:
        lista_marvel[posicion_antman]['real_name'] = 'Scott Lang'
        print(f"Se modificaron los datos del personaje: {lista_marvel[posicion_antman]}")
    else:
        print("No se encontró a Ant Man en la lista.")


print("\ni. Personajes con 'time-traveling' o 'suit' en su biografía:")
for p in lista_marvel:
    biografia = p.get('short_bio', '').lower()
    if 'time-traveling' in biografia or 'suit' in biografia:
        print(f"• {p.get('name')}: {p.get('short_bio')}")



print("\nj. Eliminar a Electro y Baron Zemo:")
electro_eliminado = lista_marvel.delete_value('Electro', criterion='por_nombre')
baron_zemo_eliminado = lista_marvel.delete_value('Baron Zemo', criterion='por_nombre')

if electro_eliminado:
    print(f"• Se elimino a Electro de la lista. Sus datos eran: {electro_eliminado}")
else:
    print("• Electro no se encontraba en la lista.")

print("")

if baron_zemo_eliminado:
    print(f"• Se elimino a Baron Zemo de la lista. Sus datos eran: {baron_zemo_eliminado}")
else:
    print("• Baron Zemo no se encontraba en la lista.")