#5. Cargar el esquema de red de la siguiente figura en un grafo e implementar los algoritmos necesarios para resolver las tareas, listadas a continuación:
#a. cada nodo además del nombre del equipo deberá almacenar su tipo: pc, notebook, servidor, router, switch, impresora;
#b. realizar un barrido en profundidad y amplitud partiendo desde la tres notebook: Red Hat, Debian, Arch;
#c. encontrar el camino más corto para enviar a imprimir un documento desde la pc: Manjaro, Red Hat, Fedora hasta la impresora;
#d. encontrar el árbol de expansión mínima;
#e. determinar desde que pc (no notebook) es el camino más corto hasta el servidor “Guaraní”;
#f. indicar desde que computadora del switch 01 es el camino más corto al servidor “MongoDB”;
#g. cambiar la conexión de la impresora al router 02 y vuelva a resolver el punto b;
#h. debe utilizar un grafo no dirigido.


from grafo import Graph
from pila import Stack


# a: Cargar el esquema de red (Grafo no dirigido)
g = Graph(is_dir=False) # Es no dirigido (Punto h)


g.add_vertex("Red Hat", "notebook")
g.add_vertex("Debian", "notebook")
g.add_vertex("Arch", "notebook")
g.add_vertex("Ubuntu", "pc")
g.add_vertex("Mint", "pc")
g.add_vertex("Manjaro", "pc")
g.add_vertex("Fedora", "pc")
g.add_vertex("Parrot", "pc")
g.add_vertex("Guaraní", "servidor")
g.add_vertex("MongoDB", "servidor")
g.add_vertex("Router 1", "router")
g.add_vertex("Router 2", "router")
g.add_vertex("Router 3", "router")
g.add_vertex("Switch 1", "switch")
g.add_vertex("Switch 2", "switch")
g.add_vertex("Impresora", "impresora")


g.add_edge(25, "Router 2", "Red Hat")
g.add_edge(9, "Router 2", "Guaraní")
g.add_edge(50, "Router 2", "Router 3")
g.add_edge(37, "Router 2", "Router 1")
g.add_edge(17, "Debian", "Switch 1")
g.add_edge(18, "Ubuntu", "Switch 1")
g.add_edge(22, "Impresora", "Switch 1")
g.add_edge(80, "Mint", "Switch 1")
g.add_edge(29, "Switch 1", "Router 1")
g.add_edge(43, "Router 1", "Router 3")
g.add_edge(40, "Manjaro", "Switch 2")
g.add_edge(61, "Router 3", "Switch 2")
g.add_edge(12, "Parrot", "Switch 2")
g.add_edge(5, "Switch 2", "MongoDB")
g.add_edge(56, "Arch", "Switch 2")
g.add_edge(3, "Fedora", "Switch 2")


# Función auxiliar para Dijkstra
def obtener_camino_y_peso(nodo_origen, nodo_destino):
    """Usa Dijkstra y reconstruye el camino y el peso total."""
    if not g.exist_path(nodo_origen, nodo_destino):
        return None, None
    
    paths = g.dijkstra(nodo_origen)
    destino_actual = nodo_destino
    peso_total = None
    camino = []
    
    while paths.size() > 0:
        value = paths.pop()
        if value[0] == destino_actual:
            if peso_total is None:
                peso_total = value[1]
            camino.append(value[0])
            destino_actual = value[2]
            
    camino.reverse()
    return camino, peso_total


# b: Barrido en profundidad y amplitud desde las notebooks
print("\nb: Barridos desde Notebooks")
notebooks = ["Red Hat", "Debian", "Arch"]
for nb in notebooks:
    print(f"\nBarrido en profundidad desde {nb}:")
    g.deep_show(nb)
    print(f"\nBarrido en amplitud desde {nb}:")
    g.amplitude_show(nb)


# c: Camino más corto a la impresora desde PCs
print("\nc: Camino más corto a Impresora")
pcs_a_imprimir = ["Manjaro", "Red Hat", "Fedora"]
for pc in pcs_a_imprimir:
    camino, peso = obtener_camino_y_peso(pc, "Impresora")
    if camino:
        print(f"Desde {pc} a Impresora: {' -> '.join(camino)} (Costo: {peso})")
    else:
        print(f"No hay camino desde {pc} a Impresora.")


# d: Árbol de Expansión Mínima (Kruskal)
print("\nd: Árbol de Expansión Mínima")
min_tree_str = g.kruskal("Router 1")
print(f"Árbol de expansión (formato origen-destino-peso):\n{min_tree_str}")


# e: Camino más corto a Guaraní desde una PC
print("\ne: PC más cercana a Guaraní")
pc_vertices = ["Ubuntu", "Mint", "Manjaro", "Fedora", "Parrot"]
mejor_pc = None
mejor_camino = None
mejor_peso = float('inf')

for pc in pc_vertices:
    camino, peso = obtener_camino_y_peso(pc, "Guaraní")
    if camino and peso < mejor_peso:
        mejor_peso = peso
        mejor_pc = pc
        mejor_camino = camino

if mejor_pc:
    print(f"La PC más cercana a Guaraní es {mejor_pc} con costo {mejor_peso}")
    print(f"Camino: {' -> '.join(mejor_camino)}")


# f: Computadora del Switch 1 más cercana a MongoDB
print("\nf: Computadora del Switch 1 más cercana a MongoDB")
comps_switch1 = ["Ubuntu", "Mint", "Debian"] 
mejor_comp = None
mejor_camino_f = None
mejor_peso_f = float('inf')

for comp in comps_switch1:
    camino, peso = obtener_camino_y_peso(comp, "MongoDB")
    if camino and peso < mejor_peso_f:
        mejor_peso_f = peso
        mejor_comp = comp
        mejor_camino_f = camino

if mejor_comp:
    print(f"La computadora del Switch 1 más cercana a MongoDB es {mejor_comp} con costo {mejor_peso_f}")
    print(f"Camino: {' -> '.join(mejor_camino_f)}")


#g: Cambiar impresora al Router 2 y repetir barrido
print("\ng: Reconectar Impresora al Router 2")

g.delete_edge("Impresora", "Switch 1")

g.add_edge(15, "Impresora", "Router 2")

print("Grafo actualizado. Repetimos barrido desde notebooks:")
for nb in notebooks:
    print(f"\nBarrido en profundidad desde {nb} (con nueva conexión):")
    g.deep_show(nb)