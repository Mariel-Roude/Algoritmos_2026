"""
Ejercicio 2: Dado un grafo no dirigido con personajes de la saga Star Wars, implementar los algoritmos necesarios 
para resolver las siguientes tareas:
a. cada vértice debe almacenar el nombre de un personaje, las aristas representan la cantidad de episodios en los 
que aparecieron juntos ambos personajes que se relacionan;
b. hallar el árbol de expansión mínimo desde el vértice que contiene a: C-3PO, Yoda y Leia;
c. determinar cuál es el número máximo de episodio que comparten dos personajes, e indicar todos los pares de personajes 
que coinciden con dicho número;
d. cargue al menos los siguientes personajes: Luke Skywalker, Darth Vader, Yoda, Boba Fett, C-3PO, Leia, Rey, Kylo Ren, 
Chewbacca, Han Solo, R2-D2, BB-8;
e. calcule el camino mas ccorto desde: C-3PO a R2-D2 y desde Yoda a Darth Vader;
f. indicar qué personajes aparecieron en los nueve episodios de la saga.
"""

from grafo import Graph    
from pila import Stack     

Apariciones = {
    "C-3PO":          [1, 2, 3, 4, 5, 6, 7, 8, 9],
    "R2-D2":          [1, 2, 3, 4, 5, 6, 7, 8, 9],
    "Yoda":           [1, 2, 3, 5, 6, 8],
    "Luke Skywalker": [4, 5, 6, 7, 8, 9],
    "Darth Vader":    [3, 4, 5, 6],
    "Leia":           [4, 5, 6, 7, 8, 9],
    "Boba Fett":      [2, 5, 6],
    "Chewbacca":      [3, 4, 5, 6, 7, 8, 9],
    "Han Solo":       [4, 5, 6, 7],
    "Rey":            [7, 8, 9],
    "Kylo Ren":       [7, 8, 9],
    "BB-8":           [7, 8, 9],
}

Total_Episodios = 9
Nombres_Conocidos = list(Apariciones.keys())


# a / d. Construcción del grafo y carga de personajes
def construir_grafo():
    grafo = Graph(is_dir=False)
    for personaje in Apariciones:
        grafo.add_vertex(personaje)

    personajes = list(Apariciones.keys())
    for i in range(len(personajes)):
        for j in range(i + 1, len(personajes)):
            a = personajes[i]
            b = personajes[j]
            
            peso = 0
            for episodio in Apariciones[a]:
                if episodio in Apariciones[b]:
                    peso += 1
                    
            if peso > 0:
                grafo.add_edge(peso, a, b)
    return grafo



# b. MST (Kruskal)
def parsear_arista_kruskal(s, nombres):
    partes = s.split('-')
    if len(partes) < 3:
        return None
    try:
        peso = int(partes[-1])
    except ValueError:
        return None
    resto = partes[:-1]
    for i in range(1, len(resto)):
        a = '-'.join(resto[:i])
        b = '-'.join(resto[i:])
        if a in nombres and b in nombres:
            return a, b, peso
    return None


def mostrar_mst(grafo, origen):
    print(f"\n MST desde '{origen}'")
    salida = grafo.kruskal(origen)
    aristas = []
    peso_total = 0
    for item in salida.split(';'):
        parsed = parsear_arista_kruskal(item, Nombres_Conocidos)
        if parsed:
            a, b, w = parsed
            aristas.append((a, b, w))
            peso_total += w
            
    for a, b, w in aristas:
        print(f"  {a} - {b}   peso {w}")
    print(f"  Peso total del árbol: {peso_total}")
    return aristas



# c. Máximo de episodios compartidos y todos los pares que lo alcanzan
def max_episodios_compartidos(grafo):
    pares = {}       
    for vertice in grafo:
        for arista in vertice.edges:
            if vertice.value < arista.destination:
                par = (vertice.value, arista.destination)
            else:
                par = (arista.destination, vertice.value)
                
            if par not in pares:
                pares[par] = arista.weight
                
    max_peso = 0
    for peso in pares.values():
        if peso > max_peso:
            max_peso = peso
            
    resultado = []
    for clave, peso in pares.items():
        if peso == max_peso:
            a = clave[0]
            b = clave[1]
            resultado.append((a, b, peso))
            
    return max_peso, resultado



# e. Camino más corto (Dijkstra)
def camino_mas_corto(grafo, origen, destino):
    pila = grafo.dijkstra(origen)    
    costo = None
    camino = []
    objetivo = destino
    while pila.size() > 0:
        valor = pila.pop()
        if valor[0] == objetivo:
            if costo is None:
                costo = valor[1]
            camino.append(valor[0])
            objetivo = valor[2]
            if objetivo is None:
                break
    camino.reverse()
    return camino, costo



# f. Personajes que aparecieron en los 9 episodios
def personajes_en_los_9(grafo):
    resultado = []
    for vertice in grafo:
        max_incidente = 0
        for arista in vertice.edges:
            if arista.weight > max_incidente:
                max_incidente = arista.weight
                
        if max_incidente == Total_Episodios:
            resultado.append(vertice.value)
    return sorted(resultado)



# Prueba
if __name__ == "__main__":
    grafo = construir_grafo()

    print("d. Personajes cargados")
    for p in sorted(Apariciones.keys()):
        print(f"  ● {p}")
        
    total_aristas = 0
    for v in grafo:
        total_aristas += len(v.edges)
    total_aristas = total_aristas // 2
    
    print(f"\n  Total: {len(Apariciones)} personajes, {total_aristas} aristas.")

  
    print("\nb. Árbol de expansión mínimo")
    for origen in ("C-3PO", "Yoda", "Leia"):
        mostrar_mst(grafo, origen)

    
    print("\nc. Máximo de episodios compartidos")
    max_peso, pares = max_episodios_compartidos(grafo)
    print(f"  Número máximo de episodios compartidos: {max_peso}")
    print(f"  Pares de personajes que alcanzan ese máximo:")
    for a, b, _ in pares:
        print(f"    ● {a} y {b}")

    
    print("\ne. Caminos más cortos")
    for origen, destino in [("C-3PO", "R2-D2"), ("Yoda", "Darth Vader")]:
        camino, costo = camino_mas_corto(grafo, origen, destino)
        print(f"\n  De '{origen}' a '{destino}':")
        if camino:
            print(f"    Camino: {' → '.join(camino)}")
            print(f"    Costo total: {costo}")
        else:
            print("    No hay camino entre esos personajes.")

    
    print("\nf. Personajes que aparecieron en los 9 episodios")
    en_9 = personajes_en_los_9(grafo)
    for p in en_9:
        print(f"  ● {p}")