from lista import List


class Pokemon:

    def __init__(self, nombre, nivel, tipo, subtipo):
        self.nombre = nombre
        self.nivel = nivel
        self.tipo = tipo
        self.subtipo = subtipo

    def __str__(self):
        return f"{self.nombre} (nivel {self.nivel}, {self.tipo}/{self.subtipo})"


class Entrenador:

    def __init__(self, nombre, torneos_ganados, batallas_perdidas, batallas_ganadas):
        self.nombre = nombre
        self.torneos_ganados = torneos_ganados
        self.batallas_perdidas = batallas_perdidas
        self.batallas_ganadas = batallas_ganadas

        self.pokemons = List()
        self.pokemons.add_criterion('nombre', por_nombre_pokemon)
        self.pokemons.add_criterion('nivel', por_nivel)

    def __str__(self):
        return (f"{self.nombre} | torneos: {self.torneos_ganados} | "
                f"perdidas: {self.batallas_perdidas} | ganadas: {self.batallas_ganadas}")



def por_nombre_entrenador(e):
    return e.nombre

def por_torneos(e):
    return e.torneos_ganados

def por_nombre_pokemon(p):
    return p.nombre

def por_nivel(p):
    return p.nivel



def buscar_entrenador(entrenadores, nombre):
    pos = entrenadores.search(nombre, 'nombre')
    return entrenadores[pos] if pos is not None else None


def tiene_pokemon(entrenador, nombre_pokemon):
    return entrenador.pokemons.search(nombre_pokemon, 'nombre') is not None




#a. Obtener la cantidad de Pokémons de un determinado entrenador.
def cantidad_pokemons(entrenadores, nombre):
    e = buscar_entrenador(entrenadores, nombre)
    return e.pokemons.size() if e else None


#b. Listar los entrenadores que hayan ganado más de tres torneos.
def entrenadores_mas_torneos(entrenadores, minimo=3):
    for e in entrenadores:
        if e.torneos_ganados > minimo:
            print(e)


#c. El Pokémon de mayor nivel del entrenador con mayor cantidad de torneos ganados.
def pokemon_mayor_nivel_del_mejor(entrenadores):
    if entrenadores.size() == 0:
        return None
    entrenadores.sort_by_criterion('torneos')
    mejor = entrenadores[-1]          
    if mejor.pokemons.size() == 0:
        return mejor, None
    mejor.pokemons.sort_by_criterion('nivel')
    return mejor, mejor.pokemons[-1]  


#d. Mostrar todos los datos de un entrenador y sus Pokémons.
def mostrar_entrenador(entrenadores, nombre):
    e = buscar_entrenador(entrenadores, nombre)
    if e:
        print(e)
        e.pokemons.show()
    else:
        print(f"No se encontró al entrenador {nombre}")


#e. Mostrar los entrenadores cuyo porcentaje de batallas ganados sea mayor al 79 %.
def porcentaje_victorias(e):
    total = e.batallas_ganadas + e.batallas_perdidas
    return e.batallas_ganadas / total * 100 if total else 0

def entrenadores_con_porcentaje(entrenadores, minimo=79):
    for e in entrenadores:
        pct = porcentaje_victorias(e)
        if pct > minimo:
            print(f"{e.nombre} - {pct:.1f}%")


#f. Los entrenadores que tengan Pokémons de tipo fuego y planta o agua/volador (tipo y subtipo).
def entrenadores_por_tipos(entrenadores):
    pares = [{'fuego', 'planta'}, {'agua', 'volador'}]
    for e in entrenadores:
        if any({p.tipo.lower(), p.subtipo.lower()} in pares for p in e.pokemons):
            print(e.nombre)


#g. El promedio de nivel de los Pokémons de un determinado entrenador.
def promedio_nivel(entrenadores, nombre):
    e = buscar_entrenador(entrenadores, nombre)
    if e is None or e.pokemons.size() == 0:
        return None
    return sum(p.nivel for p in e.pokemons) / e.pokemons.size()


#h. Determinar cuántos entrenadores tienen a un determinado Pokémon.
def cuantos_tienen(entrenadores, nombre_pokemon):
    return sum(1 for e in entrenadores if tiene_pokemon(e, nombre_pokemon))


#i. Mostrar los entrenadores que tienen Pokémons repetidos.
def entrenadores_con_repetidos(entrenadores):
    for e in entrenadores:
        nombres = [p.nombre for p in e.pokemons]
        if len(nombres) != len(set(nombres)):
            print(e.nombre)


#j. Determinar los entrenadores que tengan uno de los siguientes Pokémons: Tyrantrum, Terrakion o Wingull.
def entrenadores_con_alguno(entrenadores, buscados):
    for e in entrenadores:
        if any(tiene_pokemon(e, n) for n in buscados):
            print(e.nombre)


#k. Determinar si un entrenador “X” tiene al Pokémon “Y”, tanto el nombre del entrenador como del Pokémon deben ser ingresados;
# además si el entrenador tiene al Pokémon se deberán mostrar los datos de ambos.
def verificar_entrenador_pokemon(entrenadores, nom_entrenador, nom_pokemon):
    e = buscar_entrenador(entrenadores, nom_entrenador)
    if e is None:
        print("No se encontró al entrenador")
        return
    pos = e.pokemons.search(nom_pokemon, 'nombre')
    if pos is None:
        print(f"{e.nombre} no tiene a {nom_pokemon}")
    else:
        print(e)
        print(e.pokemons[pos])


# ---------- Programa principal ----------
entrenadores = List()
entrenadores.add_criterion('nombre', por_nombre_entrenador)
entrenadores.add_criterion('torneos', por_torneos)

def cargar(nombre, torneos, perdidas, ganadas, pokemons):
    e = Entrenador(nombre, torneos, perdidas, ganadas)
    for p in pokemons:
        e.pokemons.append(Pokemon(*p))
    entrenadores.append(e)

cargar("Ash", 5, 20, 80, [("Pikachu", 50, "electrico", "ninguno"), ("Charizard", 60, "fuego", "volador"),
                          ("Bulbasaur", 30, "planta", "veneno"), ("Pikachu", 20, "electrico", "ninguno")])
cargar("Misty", 2, 30, 70, [("Starmie", 45, "agua", "psiquico"), ("Wingull", 25, "agua", "volador")])
cargar("Brock", 4, 10, 90, [("Onix", 40, "roca", "tierra"), ("Terrakion", 70, "roca", "lucha")])
cargar("Gary", 1, 40, 60, [("Tyrantrum", 55, "roca", "dragon"), ("Growlithe", 35, "fuego", "planta")])

print("a) Pokémons de Ash:", cantidad_pokemons(entrenadores, "Ash"))
print("\nb) Más de 3 torneos:"); entrenadores_mas_torneos(entrenadores)
print("\nc)", pokemon_mayor_nivel_del_mejor(entrenadores)[1])
print("\nd)"); mostrar_entrenador(entrenadores, "Misty")
print("\ne) Más de 79% de victorias:"); entrenadores_con_porcentaje(entrenadores)
print("\nf) fuego/planta o agua/volador:"); entrenadores_por_tipos(entrenadores)
print("\ng) Promedio de nivel de Ash:", promedio_nivel(entrenadores, "Ash"))
print("\nh) Entrenadores con Pikachu:", cuantos_tienen(entrenadores, "Pikachu"))
print("\ni) Con pokémons repetidos:"); entrenadores_con_repetidos(entrenadores)
print("\nj) Tyrantrum, Terrakion o Wingull:"); entrenadores_con_alguno(entrenadores, ["Tyrantrum", "Terrakion", "Wingull"])
print("\nk)"); verificar_entrenador_pokemon(entrenadores, "Brock", "Onix")