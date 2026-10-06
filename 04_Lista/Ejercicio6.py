from lista import List

class Superheroe:

    def __init__(self, nombre, anio_aparicion, casa, biografia):
        self.nombre = nombre
        self.anio_aparicion = anio_aparicion
        self.casa = casa
        self.biografia = biografia

    def __str__(self):
        return f"{self.nombre} | {self.anio_aparicion} | {self.casa} | {self.biografia}"


def por_nombre(h):
    return h.nombre


#a. Eliminar el nodo que contiene la información de Linterna Verde.
def eliminar_heroe(heroes, nombre):                      
    return heroes.delete_value(nombre, 'nombre')


#b. Mostrar el año de aparición de Wolverine
def mostrar_anio(heroes, nombre):                         
    pos = heroes.search(nombre, 'nombre')
    if pos is not None:
        print(f"{nombre} apareció en {heroes[pos].anio_aparicion}")
    else:
        print(f"No se encontró a {nombre}")


#c. Cambiar la casa de Dr. Strange a Marvel.
def cambiar_casa(heroes, nombre, nueva_casa):             
    pos = heroes.search(nombre, 'nombre')
    if pos is not None:
        heroes[pos].casa = nueva_casa
        print(f"{nombre} ahora pertenece a {nueva_casa}")
    else:
        print(f"No se encontró a {nombre}")


#d. Mostrar el nombre de aquellos superhéroes que en su biografía menciona la palabra “traje” o “armadura”.
def mostrar_por_biografia(heroes, palabras):              
    for h in heroes:
        bio = h.biografia.lower()
        if any(p in bio for p in palabras):
            print(h.nombre)


#e Mostrar el nombre y la casa de los superhéroes cuya fecha de aparición sea anterior a 1963.
def mostrar_anteriores_a(heroes, anio):                   
    for h in heroes:
        if h.anio_aparicion < anio:
            print(f"{h.nombre} - {h.casa}")


#f. Mostrar la casa a la que pertenece Capitana Marvel y Mujer Maravilla.
def mostrar_casa(heroes, nombre):                         
    pos = heroes.search(nombre, 'nombre')
    if pos is not None:
        print(f"{nombre} pertenece a {heroes[pos].casa}")
    else:
        print(f"No se encontró a {nombre}")


#g. Mostrar toda la información de Flash y Star-Lord.
def mostrar_info(heroes, nombre):                         
    pos = heroes.search(nombre, 'nombre')
    if pos is not None:
        print(heroes[pos])
    else:
        print(f"No se encontró a {nombre}")


#h. Listar los superhéroes que comienzan con la letra B, M y S.
def listar_comienzan_con(heroes, letras):                 
    for h in heroes:
        if h.nombre.startswith(tuple(letras)):
            print(h.nombre)


#i. Determinar cuántos superhéroes hay de cada casa de comic
def contar_por_casa(heroes):                              
    cantidades = {}
    for h in heroes:
        cantidades[h.casa] = cantidades.get(h.casa, 0) + 1
    return cantidades



# ---------- Programa principal ----------
heroes = List()
heroes.add_criterion('nombre', por_nombre)

heroes.append(Superheroe("Linterna Verde", 1940, "DC", "Usa un anillo de poder que crea construcciones con su traje verde"))
heroes.append(Superheroe("Wolverine", 1974, "Marvel", "Mutante con garras de adamantium y factor de curación"))
heroes.append(Superheroe("Dr. Strange", 1963, "DC", "Hechicero supremo de la Tierra"))
heroes.append(Superheroe("Capitana Marvel", 1968, "Marvel", "Piloto con poderes cósmicos"))
heroes.append(Superheroe("Mujer Maravilla", 1941, "DC", "Princesa amazona con lazo de la verdad y armadura"))
heroes.append(Superheroe("Flash", 1940, "DC", "El hombre más veloz del mundo"))
heroes.append(Superheroe("Star-Lord", 1976, "Marvel", "Mestizo terrícola-extraterrestre, líder de los Guardianes"))
heroes.append(Superheroe("Batman", 1939, "DC", "Millonario que usa un traje con forma de murciélago"))
heroes.append(Superheroe("Iron Man", 1963, "Marvel", "Genio que construyó una armadura de alta tecnología"))
heroes.append(Superheroe("Spider-Man", 1962, "Marvel", "Joven con poderes arácnidos"))
heroes.append(Superheroe("Superman", 1938, "DC", "Último hijo de Krypton"))
heroes.append(Superheroe("Hulk", 1962, "Marvel", "Científico que se transforma en un gigante verde"))

print("a) Eliminado:", eliminar_heroe(heroes, "Linterna Verde"))
print("\nb)"); mostrar_anio(heroes, "Wolverine")
print("\nc)"); cambiar_casa(heroes, "Dr. Strange", "Marvel")
print("\nd) Mencionan 'traje' o 'armadura':"); mostrar_por_biografia(heroes, ["traje", "armadura"])
print("\ne) Anteriores a 1963:"); mostrar_anteriores_a(heroes, 1963)
print("\nf)"); mostrar_casa(heroes, "Capitana Marvel"); mostrar_casa(heroes, "Mujer Maravilla")
print("\ng)"); mostrar_info(heroes, "Flash"); mostrar_info(heroes, "Star-Lord")
print("\nh) Comienzan con B, M o S:"); listar_comienzan_con(heroes, ["B", "M", "S"])
print("\ni) Por casa:", contar_por_casa(heroes))