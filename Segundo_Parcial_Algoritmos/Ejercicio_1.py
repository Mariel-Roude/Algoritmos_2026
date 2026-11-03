"""
Ejercicio 1: Se tiene los datos de Pokémons de las 9 generaciones cargados de manera aleatoria (1025 en total) de los 
cuales se conoce su nombre, número, tipo/tipos, debilidad frente a tipo/tipos, si tiene mega evolucion (bool) y si tiene 
forma gigamax (bool) para el cual debemos construir tres árboles para acceder de manera eficiente a los datos contemplando 
lo siguiente:
a. los índices de cada uno de los árboles deben ser nombre, número y tipo;
b. mostrar todos los datos de un Pokémon a partir de su número y nombre –para este último, la búsqueda debe ser por proximidad, 
es decir si busco “bul” se deben mostrar todos los Pokémons cuyos nombres comiencen o contengan dichos caracteres–;
c. mostrar todos los nombres de los Pokémons de un determinado tipo: fantasma, fuego, acero y eléctrico;
d. realizar un listado en orden ascendente por número y nombre de Pokémon, y además un listado por nivel por nombre;
e. mostrar todos los Pokémons que son débiles frente a Jolteon, Lycanroc y Tyrantrum;
f. mostrar todos los tipos de Pokémons y cuántos hay de cada tipo;
g. determinar cuantos Pokémons tienen megaevolucion.
h. determinar cuantos Pokémons tiene forma gigamax.
i. cargue al menos 100 Pokémons.
"""

import random

from arbol import BinaryTree  
from cola import Queue


Debilidades_Por_Tipo = {
    "Normal":    ["Lucha"],
    "Fuego":     ["Agua", "Tierra", "Roca"],
    "Agua":      ["Planta", "Eléctrico"],
    "Planta":    ["Fuego", "Hielo", "Veneno", "Volador", "Bicho"],
    "Eléctrico": ["Tierra"],
    "Hielo":     ["Fuego", "Lucha", "Roca", "Acero"],
    "Lucha":     ["Volador", "Psíquico", "Hada"],
    "Veneno":    ["Tierra", "Psíquico"],
    "Tierra":    ["Agua", "Planta", "Hielo"],
    "Volador":   ["Eléctrico", "Hielo", "Roca"],
    "Psíquico":  ["Bicho", "Fantasma", "Siniestro"],
    "Bicho":     ["Fuego", "Volador", "Roca"],
    "Roca":      ["Agua", "Planta", "Lucha", "Tierra", "Acero"],
    "Fantasma":  ["Fantasma", "Siniestro"],
    "Dragón":    ["Hielo", "Dragón", "Hada"],
    "Siniestro": ["Lucha", "Bicho", "Hada"],
    "Acero":     ["Fuego", "Lucha", "Tierra"],
    "Hada":      ["Veneno", "Acero"],
}


def calcular_debilidades(tipos):
    debilidades = []
    for t in tipos:
        for deb in Debilidades_Por_Tipo.get(t, []):
            if deb not in debilidades:
                debilidades.append(deb)
    debilidades.sort()
    return debilidades


Datos_Pokemons = [
    (1,   "Bulbasaur",   ["Planta", "Veneno"],              False, False),
    (2,   "Ivysaur",     ["Planta", "Veneno"],              False, False),
    (3,   "Venusaur",    ["Planta", "Veneno"],              True,  True),
    (4,   "Charmander",  ["Fuego"],                         False, False),
    (5,   "Charmeleon",  ["Fuego"],                         False, False),
    (6,   "Charizard",   ["Fuego", "Volador"],              True,  True),
    (7,   "Squirtle",    ["Agua"],                          False, False),
    (8,   "Wartortle",   ["Agua"],                          False, False),
    (9,   "Blastoise",   ["Agua"],                          True,  True),
    (10,  "Caterpie",    ["Bicho"],                         False, False),
    (11,  "Metapod",     ["Bicho"],                         False, False),
    (12,  "Butterfree",  ["Bicho", "Volador"],              False, True),
    (13,  "Weedle",      ["Bicho", "Veneno"],               False, False),
    (14,  "Kakuna",      ["Bicho", "Veneno"],               False, False),
    (15,  "Beedrill",    ["Bicho", "Veneno"],               True,  False),
    (16,  "Pidgey",      ["Normal", "Volador"],             False, False),
    (17,  "Pidgeotto",   ["Normal", "Volador"],             False, False),
    (18,  "Pidgeot",     ["Normal", "Volador"],             True,  False),
    (19,  "Rattata",     ["Normal"],                        False, False),
    (20,  "Raticate",    ["Normal"],                        False, False),
    (21,  "Spearow",     ["Normal", "Volador"],             False, False),
    (22,  "Fearow",      ["Normal", "Volador"],             False, False),
    (23,  "Ekans",       ["Veneno"],                        False, False),
    (24,  "Arbok",       ["Veneno"],                        False, False),
    (25,  "Pikachu",     ["Eléctrico"],                     False, True),
    (26,  "Raichu",      ["Eléctrico"],                     False, False),
    (27,  "Sandshrew",   ["Tierra"],                        False, False),
    (28,  "Sandslash",   ["Tierra"],                        False, False),
    (29,  "Nidoran-F",   ["Veneno"],                        False, False),
    (30,  "Nidorina",    ["Veneno"],                        False, False),
    (31,  "Nidoqueen",   ["Veneno", "Tierra"],              False, False),
    (32,  "Nidoran-M",   ["Veneno"],                        False, False),
    (33,  "Nidorino",    ["Veneno"],                        False, False),
    (34,  "Nidoking",    ["Veneno", "Tierra"],              False, False),
    (35,  "Clefairy",    ["Hada"],                          False, False),
    (36,  "Clefable",    ["Hada"],                          False, False),
    (37,  "Vulpix",      ["Fuego"],                         False, False),
    (38,  "Ninetales",   ["Fuego"],                         False, False),
    (39,  "Jigglypuff",  ["Normal", "Hada"],                False, False),
    (40,  "Wigglytuff",  ["Normal", "Hada"],                False, False),
    (41,  "Zubat",       ["Veneno", "Volador"],             False, False),
    (42,  "Golbat",      ["Veneno", "Volador"],             False, False),
    (43,  "Oddish",      ["Planta", "Veneno"],              False, False),
    (44,  "Gloom",       ["Planta", "Veneno"],              False, False),
    (45,  "Vileplume",   ["Planta", "Veneno"],              False, False),
    (46,  "Paras",       ["Bicho", "Planta"],               False, False),
    (47,  "Parasect",    ["Bicho", "Planta"],               False, False),
    (48,  "Venonat",     ["Bicho", "Veneno"],               False, False),
    (49,  "Venomoth",    ["Bicho", "Veneno"],               False, False),
    (50,  "Diglett",     ["Tierra"],                        False, False),
    (51,  "Dugtrio",     ["Tierra"],                        False, False),
    (52,  "Meowth",      ["Normal"],                        False, True),
    (53,  "Persian",     ["Normal"],                        False, False),
    (54,  "Psyduck",     ["Agua"],                          False, False),
    (55,  "Golduck",     ["Agua"],                          False, False),
    (56,  "Mankey",      ["Lucha"],                         False, False),
    (57,  "Primeape",    ["Lucha"],                         False, False),
    (58,  "Growlithe",   ["Fuego"],                         False, False),
    (59,  "Arcanine",    ["Fuego"],                         False, False),
    (60,  "Poliwag",     ["Agua"],                          False, False),
    (61,  "Poliwhirl",   ["Agua"],                          False, False),
    (62,  "Poliwrath",   ["Agua", "Lucha"],                 False, False),
    (63,  "Abra",        ["Psíquico"],                      False, False),
    (64,  "Kadabra",     ["Psíquico"],                      False, False),
    (65,  "Alakazam",    ["Psíquico"],                      True,  False),
    (66,  "Machop",      ["Lucha"],                         False, False),
    (67,  "Machoke",     ["Lucha"],                         False, False),
    (68,  "Machamp",     ["Lucha"],                         False, True),
    (69,  "Bellsprout",  ["Planta", "Veneno"],              False, False),
    (70,  "Weepinbell",  ["Planta", "Veneno"],              False, False),
    (71,  "Victreebel",  ["Planta", "Veneno"],              False, False),
    (72,  "Tentacool",   ["Agua", "Veneno"],                False, False),
    (73,  "Tentacruel",  ["Agua", "Veneno"],                False, False),
    (74,  "Geodude",     ["Roca", "Tierra"],                False, False),
    (75,  "Graveler",    ["Roca", "Tierra"],                False, False),
    (76,  "Golem",       ["Roca", "Tierra"],                False, False),
    (77,  "Ponyta",      ["Fuego"],                         False, False),
    (78,  "Rapidash",    ["Fuego"],                         False, False),
    (79,  "Slowpoke",    ["Agua", "Psíquico"],              False, False),
    (80,  "Slowbro",     ["Agua", "Psíquico"],              True,  False),
    (81,  "Magnemite",   ["Eléctrico", "Acero"],            False, False),
    (82,  "Magneton",    ["Eléctrico", "Acero"],            False, False),
    (83,  "Farfetchd",   ["Normal", "Volador"],             False, False),
    (84,  "Doduo",       ["Normal", "Volador"],             False, False),
    (85,  "Dodrio",      ["Normal", "Volador"],             False, False),
    (86,  "Seel",        ["Agua"],                          False, False),
    (87,  "Dewgong",     ["Agua", "Hielo"],                 False, False),
    (88,  "Grimer",      ["Veneno"],                        False, False),
    (89,  "Muk",         ["Veneno"],                        False, False),
    (90,  "Shellder",    ["Agua"],                          False, False),
    (91,  "Cloyster",    ["Agua", "Hielo"],                 False, False),
    (92,  "Gastly",      ["Fantasma", "Veneno"],            False, False),
    (93,  "Haunter",     ["Fantasma", "Veneno"],            False, False),
    (94,  "Gengar",      ["Fantasma", "Veneno"],            True,  True),
    (95,  "Onix",        ["Roca", "Tierra"],                False, False),
    (96,  "Drowzee",     ["Psíquico"],                      False, False),
    (97,  "Hypno",       ["Psíquico"],                      False, False),
    (98,  "Krabby",      ["Agua"],                          False, False),
    (99,  "Kingler",     ["Agua"],                          False, True),
    (100, "Voltorb",     ["Eléctrico"],                     False, False),
    (101, "Electrode",   ["Eléctrico"],                     False, False),
    (102, "Exeggcute",   ["Planta", "Psíquico"],            False, False),
    (103, "Exeggutor",   ["Planta", "Psíquico"],            False, False),
    (104, "Cubone",      ["Tierra"],                        False, False),
    (105, "Marowak",     ["Tierra"],                        False, False),
    (106, "Hitmonlee",   ["Lucha"],                         False, False),
    (107, "Hitmonchan",  ["Lucha"],                         False, False),
    (108, "Lickitung",   ["Normal"],                        False, False),
    (109, "Koffing",     ["Veneno"],                        False, False),
    (110, "Weezing",     ["Veneno"],                        False, False),
    (111, "Rhyhorn",     ["Tierra", "Roca"],                False, False),
    (112, "Rhydon",      ["Tierra", "Roca"],                False, False),
    (113, "Chansey",     ["Normal"],                        False, False),
    (114, "Tangela",     ["Planta"],                        False, False),
    (115, "Kangaskhan",  ["Normal"],                        True,  False),
    (116, "Horsea",      ["Agua"],                          False, False),
    (117, "Seadra",      ["Agua"],                          False, False),
    (118, "Goldeen",     ["Agua"],                          False, False),
    (119, "Seaking",     ["Agua"],                          False, False),
    (120, "Staryu",      ["Agua"],                          False, False),
    (121, "Starmie",     ["Agua", "Psíquico"],              False, False),
    (122, "Mr. Mime",    ["Psíquico", "Hada"],              False, False),
    (123, "Scyther",     ["Bicho", "Volador"],              False, False),
    (124, "Jynx",        ["Hielo", "Psíquico"],             False, False),
    (125, "Electabuzz",  ["Eléctrico"],                     False, False),
    (126, "Magmar",      ["Fuego"],                         False, False),
    (127, "Pinsir",      ["Bicho"],                         True,  False),
    (128, "Tauros",      ["Normal"],                        False, False),
    (129, "Magikarp",    ["Agua"],                          False, False),
    (130, "Gyarados",    ["Agua", "Volador"],               True,  False),
    (131, "Lapras",      ["Agua", "Hielo"],                 False, True),
    (132, "Ditto",       ["Normal"],                        False, False),
    (133, "Eevee",       ["Normal"],                        False, True),
    (134, "Vaporeon",    ["Agua"],                          False, False),
    (135, "Jolteon",     ["Eléctrico"],                     False, False),
    (136, "Flareon",     ["Fuego"],                         False, False),
    (137, "Porygon",     ["Normal"],                        False, False),
    (138, "Omanyte",     ["Roca", "Agua"],                  False, False),
    (139, "Omastar",     ["Roca", "Agua"],                  False, False),
    (140, "Kabuto",      ["Roca", "Agua"],                  False, False),
    (141, "Kabutops",    ["Roca", "Agua"],                  False, False),
    (142, "Aerodactyl",  ["Roca", "Volador"],               True,  False),
    (143, "Snorlax",     ["Normal"],                        False, True),
    (144, "Articuno",    ["Hielo", "Volador"],              False, False),
    (145, "Zapdos",      ["Eléctrico", "Volador"],          False, False),
    (146, "Moltres",     ["Fuego", "Volador"],              False, False),
    (147, "Dratini",     ["Dragón"],                        False, False),
    (148, "Dragonair",   ["Dragón"],                        False, False),
    (149, "Dragonite",   ["Dragón", "Volador"],             False, False),
    (150, "Mewtwo",      ["Psíquico"],                      True,  False),
    (151, "Mew",         ["Psíquico"],                      False, False),
    (152, "Chikorita",   ["Planta"],                        False, False),
    (158, "Totodile",    ["Agua"],                          False, False),
    (252, "Treecko",     ["Planta"],                        False, False),
    (255, "Torchic",     ["Fuego"],                         False, False),
    (258, "Mudkip",      ["Agua"],                          False, False),
    (387, "Turtwig",     ["Planta"],                        False, False),
    (390, "Chimchar",    ["Fuego"],                         False, False),
    (393, "Piplup",      ["Agua"],                          False, False),
    (495, "Snivy",       ["Planta"],                        False, False),
    (498, "Tepig",       ["Fuego"],                         False, False),
    (501, "Oshawott",    ["Agua"],                          False, False),
    (650, "Chespin",     ["Planta"],                        False, False),
    (653, "Fennekin",    ["Fuego"],                         False, False),
    (656, "Froakie",     ["Agua"],                          False, False),
    (697, "Tyrantrum",   ["Roca", "Dragón"],                False, False),
    (722, "Rowlet",      ["Planta", "Volador"],             False, False),
    (725, "Litten",      ["Fuego"],                         False, False),
    (728, "Popplio",     ["Agua"],                          False, False),
    (745, "Lycanroc",    ["Roca"],                          False, False),
    (810, "Grookey",     ["Planta"],                        False, False),
    (813, "Scorbunny",   ["Fuego"],                         False, False),
    (816, "Sobble",      ["Agua"],                          False, False),
    (906, "Sprigatito",  ["Planta"],                        False, False),
    (909, "Fuecoco",     ["Fuego"],                         False, False),
    (912, "Quaxly",      ["Agua"],                          False, False),
]


class GestorPokemons:
    def __init__(self):
        self.arbol_nombre = BinaryTree()  
        self.arbol_numero = BinaryTree()    
        self.arbol_tipo = BinaryTree()    

    def cargar_pokemons(self):
        datos = list(Datos_Pokemons)
        random.shuffle(datos)                     
        for numero, nombre, tipos, mega, gigamax in datos:
            pokemon = {
                "numero": numero,
                "nombre": nombre,
                "tipos": tipos,
                "debilidades": calcular_debilidades(tipos),
                "mega": mega,
                "gigamax": gigamax,
            }
            self._agregar_pokemon(pokemon)

    def _agregar_pokemon(self, pokemon):
        self.arbol_nombre.insert_node(pokemon["nombre"], pokemon)
        self.arbol_numero.insert_node(pokemon["numero"], pokemon)
        for t in pokemon["tipos"]:
            nodo = self.arbol_tipo.search(t)
            if nodo is not None:
                nodo.other_values.append(pokemon)
            else:
                self.arbol_tipo.insert_node(t, [pokemon])

    def _imprimir_pokemon(self, p):
        print(f"N° {p['numero']}  {p['nombre']}")
        print(f"   Tipos:        {', '.join(p['tipos'])}")
        print(f"   Debilidades:  {', '.join(p['debilidades'])}")
        
        if p['mega']:
            texto_mega = "Sí"
        else:
            texto_mega = "No"
            
        if p['gigamax']:
            texto_gigamax = "Sí"
        else:
            texto_gigamax = "No"

        print(f"   Mega:         {texto_mega}")
        print(f"   Gigamax:      {texto_gigamax}")
        print()


    # b. Datos por número y por nombre (proximidad)
    def mostrar_por_numero(self, numero):
        print(f"Pokémon con número {numero}")
        nodo = self.arbol_numero.search(numero)
        if nodo is not None:
            self._imprimir_pokemon(nodo.other_values)
        else:
            print("No se encontró un Pokémon con ese número.")

    def mostrar_por_nombre(self, subcadena):
        print(f"\nPokémons cuyo nombre contiene '{subcadena}'")
        
        nombre_buscado = subcadena.lower()
        encontrados = []

        def _recorrer(root):
            if root is not None:
                _recorrer(root.left)
                if nombre_buscado in root.value.lower():
                    encontrados.append(root.other_values)
                _recorrer(root.right)

        _recorrer(self.arbol_nombre.root)
        if not encontrados:
            print("No se encontraron coincidencias.")
        else:
            def obtener_numero(p):
                return p["numero"]
                
            for p in sorted(encontrados, key=obtener_numero):
                self._imprimir_pokemon(p)

    # c. Nombres por tipo
    def mostrar_nombres_por_tipo(self, tipo):
        print(f"\nPokémons de tipo {tipo}")
        nodo = self.arbol_tipo.search(tipo)
        if nodo is None or not nodo.other_values:
            print("No hay Pokémons de ese tipo.")
            return
            
        def obtener_nombre(p):
            return p["nombre"]
            
        for p in sorted(nodo.other_values, key=obtener_nombre):
            print(f"● {p['nombre']}")
        print(f"  total: {len(nodo.other_values)}")

    # d. Listados ordenados
    def listar_por_numero_asc(self):
        print("\nListado ascendente por número")
        
        def _recorrer(root):
            if root is not None:
                _recorrer(root.left)
                print(f"● {root.value} - {root.other_values['nombre']}")
                _recorrer(root.right)
                
        _recorrer(self.arbol_numero.root)

    def listar_por_nombre_asc(self):
        print("\nListado ascendente por nombre")
        
        def _recorrer(root):
            if root is not None:
                _recorrer(root.left)
                print(f"● {root.value}")
                _recorrer(root.right)
                
        _recorrer(self.arbol_nombre.root)

    def listar_por_nivel_nombre(self):
        print("\nListado por nivel (por nombre)")
        cola = Queue()
        
        if self.arbol_nombre.root is not None:
            cola.arrive(self.arbol_nombre.root)
            
            while cola.size() > 0:
                nodo = cola.attention()
                print(f"● {nodo.value}")
                
                if nodo.left is not None:
                    cola.arrive(nodo.left)
                if nodo.right is not None:
                    cola.arrive(nodo.right)

    # e. Débiles frente a Jolteon, Lycanroc y Tyrantrum
    def mostrar_debiles_contra(self, nombres_referencia):
        tipos_referencia = []
        
        for nombre in nombres_referencia:
            nodo = self.arbol_nombre.search(nombre)
            if nodo is not None:
                for tipo in nodo.other_values["tipos"]:
                    if tipo not in tipos_referencia:
                        tipos_referencia.append(tipo)
            else:
                print(f"  (Aviso: no se encontró a '{nombre}')")

        if len(tipos_referencia) == 0:
            print("No se pudieron determinar los tipos de referencia.")
            return

        tipos_referencia.sort()
        print(f"Tipos de referencia: {tipos_referencia}\n")

        resultados = []

        def _recorrer(root):
            if root is not None:
                _recorrer(root.left)
                p = root.other_values
                coincidencias = []
                for t in p["debilidades"]:
                    if t in tipos_referencia:
                        coincidencias.append(t)
                coincidencias.sort()
                
                if len(coincidencias) > 0:
                    resultados.append((p, coincidencias))
                _recorrer(root.right)

        _recorrer(self.arbol_numero.root)
        
        def obtener_numero_de_tupla(item):
            return item[0]["numero"]
            
        for p, coincidencias in sorted(resultados, key=obtener_numero_de_tupla):
            print(f"● {p['nombre']} débil ante: {', '.join(coincidencias)}")
        print(f"\n  total: {len(resultados)}")

    # f. Tipos y cantidad
    def mostrar_tipos_y_cantidades(self):
        def _recorrer(root):
            if root is not None:
                _recorrer(root.left)
                print(f"● {root.value}: {len(root.other_values)}")
                _recorrer(root.right)

        _recorrer(self.arbol_tipo.root)

    # g / h. Conteos
    def contar_mega(self):
        contador = 0

        def _recorrer(root):
            nonlocal contador
            if root is not None:
                _recorrer(root.left)
                if root.other_values["mega"]:
                    contador += 1
                _recorrer(root.right)

        _recorrer(self.arbol_numero.root)
        return contador

    def contar_gigamax(self):
        contador = 0

        def _recorrer(root):
            nonlocal contador
            if root is not None:
                _recorrer(root.left)
                if root.other_values["gigamax"]:
                    contador += 1
                _recorrer(root.right)

        _recorrer(self.arbol_numero.root)
        return contador


# Prueba
if __name__ == "__main__":
    gestor = GestorPokemons()
    gestor.cargar_pokemons()  

    print("b. Mostrar datos por número y por nombre")
    gestor.mostrar_por_numero(6)
    gestor.mostrar_por_nombre("bul")


    print("\nc. Mostrar nombres por tipo")
    for tipo in ("Fantasma", "Fuego", "Acero", "Eléctrico"):
        gestor.mostrar_nombres_por_tipo(tipo)


    print("\nd. Listados ordenados")
    gestor.listar_por_numero_asc()
    gestor.listar_por_nombre_asc()
    gestor.listar_por_nivel_nombre()


    print("\ne. Débiles frente a Jolteon, Lycanroc y Tyrantrum")
    gestor.mostrar_debiles_contra(["Jolteon", "Lycanroc", "Tyrantrum"])


    print("\nf. Tipos y cantidad de Pokémons")
    gestor.mostrar_tipos_y_cantidades()


    print("\ng. Conteo de Mega Evolución")
    print(f"● Pokémons con mega evolución: {gestor.contar_mega()}")


    print("\nh. Conteo de Gigamax")
    print(f"● Pokémons con gigamax: {gestor.contar_gigamax()}")