#14. Implementar sobre un grafo no dirigido los algoritmos necesario para dar solución a las siguientes tareas:
#a. cada vértice representar un ambiente de una casa: cocina, comedor, cochera, quincho, baño 1, baño 2, habitación 1, habitación 2, sala de estar, terraza, patio;
#b. cargar al menos tres aristas a cada vértice, y a dos de estas cárguele cinco, el peso de la arista es la distancia entre los ambientes, se debe cargar en metros;
#c. obtener el árbol de expansión mínima y determine cuantos metros de cables se necesitan para conectar todos los ambientes;
#d. determinar cuál es el camino más corto desde la habitación 1 hasta la sala de estar para determinar cuántos metros de cable de red se necesitan para conectar el router con el Smart Tv.


from grafo import Graph


# a y b: Cargar el grafo no dirigido
g = Graph(is_dir=False)

# a: Cargar los vértices (ambientes de la casa)
ambientes = [
    "cocina", "comedor", "cochera", "quincho", "baño 1",
    "baño 2", "habitación 1", "habitación 2", "sala de estar",
    "terraza", "patio"
]

for amb in ambientes:
    g.add_vertex(amb, "ambiente")

# b: Cargar aristas
g.add_edge(5, "cocina", "comedor")         
g.add_edge(5, "habitación 1", "baño 1")    


g.add_edge(3, "cocina", "patio")
g.add_edge(4, "comedor", "sala de estar")
g.add_edge(6, "comedor", "habitación 1")
g.add_edge(8, "cochera", "patio")
g.add_edge(10, "cochera", "quincho")
g.add_edge(2, "cochera", "terraza")
g.add_edge(9, "quincho", "terraza")
g.add_edge(7, "quincho", "baño 2")
g.add_edge(4, "baño 1", "habitación 2")
g.add_edge(3, "baño 2", "habitación 2")
g.add_edge(6, "habitación 1", "sala de estar")
g.add_edge(4, "habitación 2", "sala de estar") 
g.add_edge(4, "sala de estar", "patio")
g.add_edge(7, "terraza", "patio")
g.add_edge(6, "patio", "baño 1")
g.add_edge(9, "baño 1", "baño 2")


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


# c: Árbol de Expansión Mínima y total de metros de cable
print("c: Árbol de Expansión Mínima (Kruskal)")
min_tree_str = g.kruskal("cocina")
print(f"Árbol obtenido (origen-destino-peso):\n{min_tree_str}")


peso_total_cable = 0
print("\nAristas del árbol de expansión:")
for edge in min_tree_str.split(';'):
    
    partes = edge.split('-')
 
    if len(partes) == 3:
        origen, destino, peso = partes
        print(f"  {origen} -> {destino} : {peso} metros")
        peso_total_cable += int(peso)

print(f"\nTotal de metros de cable necesarios para conectar todos los ambientes: {peso_total_cable} metros.")



#d: Camino más corto desde habitación 1 a sala de estar
print("\nd: Router (Habitación 1) -> Smart TV (Sala de estar)")
camino, peso = obtener_camino_y_peso("habitación 1", "sala de estar")

if camino:
    print(f"Camino más corto: {' -> '.join(camino)}")
    print(f"Metros de cable de red necesarios: {peso} metros.")
else:
    print("No existe camino entre la habitación 1 y la sala de estar.")