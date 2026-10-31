#5. Dado un árbol con los nombre de los superhéroes y villanos de la saga Marvel Cinematic Universe (MCU), desarrollar un algoritmo que contemple lo siguiente:
#a. además del nombre del superhéroe, en cada nodo del árbol se almacenará un campo booleano que indica si es un héroe o un villano, True y False respectivamente;
#b. listar los villanos ordenados alfabéticamente;
#c. mostrar todos los superhéroes que empiezan con C;
#d. determinar cuántos superhéroes hay el árbol;
#e. Doctor Strange en realidad está mal cargado. Utilice una búsqueda por proximidad para encontrarlo en el árbol y modificar su nombre;
#f. listar los superhéroes ordenados de manera descendente;
#g. generar un bosque a partir de este árbol, un árbol debe contener a los superhéroes y otro a los villanos, luego resolver las siguiente tareas:
#   I. determinar cuántos nodos tiene cada árbol;
#   II. realizar un barrido ordenado alfabéticamente de cada árbol.


from arbol import BinaryTree


# Datos iniciales (nombre, es_villano)
personajes = [
    ("Iron Man", False),
    ("Thanos", True),
    ("Captain America", False),
    ("Loki", True),
    ("Doctor Strange", False),
    ("Hulk", False),
    ("Ultron", True),
    ("Captain Marvel", False),
    ("Black Widow", False),
    ("Red Skull", True),
    ("Spider-Man", False),
    ("Doctor Doom", True),   
    ("Crimson Dynamo", True),
    ("Cyclops", False),      
    ("Colossus", False),     
]


# a. Cargar el árbol con nombre + booleano
arbol = BinaryTree()
for nombre, es_villano in personajes:
    arbol.insert_node(nombre, {"is_villain": es_villano})

print("Árbol cargado (inorden)")
arbol.inorden()
print()


# b. Listar villanos ordenados alfabéticamente
print("b. Villanos ordenados alfabéticamente")
arbol.inorden_villain()
print()

# c. Superhéroes que empiezan con C
print("c. Superhéroes que empiezan con 'C'")
arbol.inorden_hero_star_with("C")
print()


# d. Cuántos superhéroes hay en el árbol
print("d. Cantidad de superhéroes")
print(f"Total superhéroes: {arbol.count_heroes()}")
print()


# e. Doctor Strange mal cargado -> búsqueda por proximidad
print("e. Buscar 'Doctor Strange' por proximidad y corregir")

def buscar_por_proximidad(tree, substring):
    """Devuelve el primer nodo cuyo value contenga substring (case-insensitive)."""
    resultado = [None]
    def __buscar(root):
        if root is not None and resultado[0] is None:
            __buscar(root.left)
            if resultado[0] is None and substring.lower() in str(root.value).lower():
                resultado[0] = root
            __buscar(root.right)
    __buscar(tree.root)
    return resultado[0]

nodo_ds = buscar_por_proximidad(arbol, "Strange")
if nodo_ds is not None:
    nombre_viejo = nodo_ds.value
    other_viejo = nodo_ds.other_values
    print(f"Encontrado nodo mal cargado: '{nombre_viejo}'")

    arbol.delete_node(nombre_viejo)
    arbol.insert_node("Doctor Strange", other_viejo)
    print("Corregido a 'Doctor Strange'")
else:
    print("No se encontró 'Strange' en el árbol")
print()


# f. Superhéroes ordenados de manera descendente
print("f. Superhéroes en orden descendente")
def heroes_descendente(tree):
    def __desc(root):
        if root is not None:
            __desc(root.right)
            if root.other_values and not root.other_values.get('is_villain'):
                print(root.value)
            __desc(root.left)
    __desc(tree.root)

heroes_descendente(arbol)
print()


# g. Generar bosque: un árbol de héroes y otro de villanos
print("g. Generando bosque (árbol de héroes y árbol de villanos)")
arbol_heroes = BinaryTree()
arbol_villanos = BinaryTree()

def generar_bosque(tree, heroes, villanos):
    def __recorrer(root):
        if root is not None:
            __recorrer(root.left)
            if root.other_values and root.other_values.get('is_villain'):
                villanos.insert_node(root.value, root.other_values)
            else:
                heroes.insert_node(root.value, root.other_values)
            __recorrer(root.right)
    __recorrer(tree.root)

generar_bosque(arbol, arbol_heroes, arbol_villanos)

# g.I. Determinar cuántos nodos tiene cada árbol
def contar_nodos(tree):
    def __contar(root):
        if root is None:
            return 0
        return 1 + __contar(root.left) + __contar(root.right)
    return __contar(tree.root)

print(f"g.I. Nodos en árbol de héroes: {contar_nodos(arbol_heroes)}")
print(f"     Nodos en árbol de villanos: {contar_nodos(arbol_villanos)}")
print()

# g.II. Barrido ordenado alfabéticamente de cada árbol
print("g.II. Héroes ordenados alfabéticamente:")
arbol_heroes.inorden()
print()
print("g.II. Villanos ordenados alfabéticamente:")
arbol_villanos.inorden()