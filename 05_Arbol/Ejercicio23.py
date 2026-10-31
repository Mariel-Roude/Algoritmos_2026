#23. Implementar un algoritmo que permita generar un árbol con los datos de la siguiente tabla y resuelva las siguientes consultas:
#a. listado inorden de las criaturas y quienes la derrotaron;
#b. se debe permitir cargar una breve descripción sobre cada criatura;
#c. mostrar toda la información de la criatura Talos;
#d. determinar los 3 héroes o dioses que derrotaron mayor cantidad de criaturas;
#e. listar las criaturas derrotadas por Heracles;
#f. listar las criaturas que no han sido derrotadas;
#g. además cada nodo debe tener un campo “capturada” que almacenará el nombre del héroe o dios que la capturo;
#h. modifique los nodos de las criaturas Cerbero, Toro de Creta, Cierva Cerinea y Jabalí de Erimanto indicando que Heracles las atrapó;
#i. se debe permitir búsquedas por coincidencia;
#j. eliminar al Basilisco y a las Sirenas;
#k. modificar el nodo que contiene a las Aves del Estínfalo, agregando que Heracles derroto a varias;
#l. modifique el nombre de la criatura Ladón por Dragón Ladón;
#m. realizar un listado por nivel del árbol;
#n. muestre las criaturas capturadas por Heracles.



from arbol import BinaryTree


# Datos de la tabla (Criatura, Derrotado por, Descripción)
datos_tabla = [
    ("Ceto", None, "Diosa marina primordial, madre de monstruos marinos."),
    ("Tifón", "Zeus", "Monstruo gigante con cien cabezas de dragón y alas."),
    ("Equidna", "Argos Panoptes", "Mitad mujer, mitad serpiente, madre de varios monstruos."),
    ("Dino", None, "Una de las Grayas, hermana de Enio y Pefredo."),
    ("Pefredo", None, "Una de las Grayas, de cabellos grises y un solo ojo compartido."),
    ("Enio", None, "Una de las Grayas, hermana de Dino y Pefredo."),
    ("Escila", None, "Monstruo marino con seis cabezas que devoraba marineros."),
    ("Caribdis", None, "Remolino marino monstruoso que tragaba barcos."),
    ("Euríale", None, "Una de las Gorgonas, hermana de Medusa y Esteno."),
    ("Esteno", None, "Una de las Gorgonas, hermana de Medusa y Euríale."),
    ("Medusa", "Perseo", "Gorgona con serpientes en el cabello; su mirada petrifica."),
    ("Ladón", "Heracles", "Dragón de cien cabezas que custodiaba las manzanas de las Hespérides."),
    ("Águila del Cáucaso", None, "Ave que devoraba el hígado de Prometeo cada día."),
    ("Quimera", "Belerofonte", "Monstruo con cabeza de león, cuerpo de cabra y cola de serpiente."),
    ("Hidra de Lerna", "Heracles", "Serpiente de muchas cabezas; al cortar una, brotaban dos."),
    ("León de Nemea", "Heracles", "León de piel impenetrable, primer trabajo de Heracles."),
    ("Esfinge", "Edipo", "Ser con cuerpo de león, alas de águila y rostro de mujer; planteaba acertijos."),
    ("Dragón de la Cólquida", None, "Dragón que custodiaba el Vellocino de Oro."),
    ("Cerbero", None, "Perro de tres cabezas que custodiaba el Hades."),
    ("Cerda de Cromión", "Teseo", "Jabalí gigante que asolaba la región de Cromión."),
    ("Orto", "Heracles", "Perro de dos cabezas, hermano de Cerbero."),
    ("Toro de Creta", "Teseo", "Toro monstruoso del rey Minos."),
    ("Jabalí de Calidón", "Atalanta", "Jabalí gigante enviado por Artemisa."),
    ("Carcinos", None, "Cangrejo gigante enviado por Hera para atacar a Heracles."),
    ("Gerión", "Heracles", "Gigante de tres cuerpos, dueño de un rebaño de bueyes."),
    ("Cloto", None, "Una de las Moiras; hilaba el hilo de la vida."),
    ("Láquesis", None, "Una de las Moiras; medía el hilo de la vida."),
    ("Átropos", None, "Una de las Moiras; cortaba el hilo de la vida."),
    ("Minotauro de Creta", "Teseo", "Ser con cabeza de toro y cuerpo humano, encerrado en el laberinto."),
    ("Harpías", None, "Aves con rostro de mujer que atormentaban a los mortales."),
    ("Argos Panoptes", "Hermes", "Gigante de cien ojos, guardián de Io."),
    ("Aves del Estínfalo", None, "Aves con plumas de bronce y pico afilado."),
    ("Talos", "Medea", "Autómata de bronce que protegía la isla de Creta."),
    ("Sirenas", None, "Criaturas marinas cuyo canto atraía a los navegantes."),
    ("Pitón", "Apolo", "Serpiente gigante que custodiaba el oráculo de Delfos."),
    ("Cierva de Cerinea", None, "Cierva de cuernos de oro, consagrada a Artemisa."),
    ("Basilisco", None, "Serpiente gigante cuya mirada mataba."),
    ("Jabalí de Erimanto", None, "Jabalí gigante que asolaba el monte Erimanto.")
]


# a, b, g. Generar el árbol con los datos, descripción y capturada
arbol = BinaryTree()

for criatura, derrotado_por, descripcion in datos_tabla:
    # g. Campo capturada
    info_extra = {
        "derrotado_por": derrotado_por,
        "descripcion": descripcion,
        "capturada": None
    }
    arbol.insert_node(criatura, info_extra)


# a. Listado inorden de las criaturas y quienes las derrotaron
print("a. Listado inorden (Criatura - Derrotado por)")
def inorden_criaturas(tree):
    def __inorden(root):
        if root is not None:
            __inorden(root.left)
            derrotador = root.other_values.get("derrotado_por") or "Nadie"
            print(f"{root.value} - Derrotada por: {derrotador}")
            __inorden(root.right)
    __inorden(tree.root)
inorden_criaturas(arbol)
print()


# c. Mostrar toda la información de la criatura Talos
print("c. Información de Talos")
def mostrar_info(tree, nombre):
    nodo = tree.search(nombre)
    if nodo is not None:
        print(f"Criatura: {nodo.value}")
        print(f"Derrotada por: {nodo.other_values.get('derrotado_por') or 'Nadie'}")
        print(f"Descripción: {nodo.other_values.get('descripcion')}")
        print(f"Capturada por: {nodo.other_values.get('capturada') or 'Nadie'}")
    else:
        print(f"{nombre} no encontrado.")

mostrar_info(arbol, "Talos")
print()


# d. Los 3 héroes/dioses que derrotaron mayor cantidad de criaturas
print("d. Top 3 héroes/dioses que más criaturas derrotaron")
def top_derrotadores(tree):
    conteo = {}
    def __recorrer(root):
        if root is not None:
            __recorrer(root.left)
            derrotador = root.other_values.get("derrotado_por")
            if derrotador:
                conteo[derrotador] = conteo.get(derrotador, 0) + 1
            __recorrer(root.right)
    __recorrer(tree.root)
    
    # Ordenar por cantidad de mayor a menor y tomar los 3 primeros
    top = sorted(conteo.items(), key=lambda x: x[1], reverse=True)[:3]
    for heroe, cant in top:
        print(f"{heroe}: {cant} criaturas")
top_derrotadores(arbol)
print()


# e. Listar las criaturas derrotadas por Heracles
print("e. Criaturas derrotadas por Heracles")
def listar_por_derrotador(tree, heroe):
    def __recorrer(root):
        if root is not None:
            __recorrer(root.left)
            if root.other_values.get("derrotado_por") == heroe:
                print(root.value)
            __recorrer(root.right)
    __recorrer(tree.root)
listar_por_derrotador(arbol, "Heracles")
print()


# f. Listar las criaturas que no han sido derrotadas
print("f. Criaturas NO derrotadas")
def listar_no_derrotadas(tree):
    def __recorrer(root):
        if root is not None:
            __recorrer(root.left)
            if not root.other_values.get("derrotado_por"):
                print(root.value)
            __recorrer(root.right)
    __recorrer(tree.root)
listar_no_derrotadas(arbol)
print()


# h. Modificar nodos: Cerbero, Toro de Creta, Cierva Cerinea, Jabalí de Erimanto, indicando que Heracles las atrapó
print("h. Modificando capturadas por Heracles")
criaturas_capturadas = ["Cerbero", "Toro de Creta", "Cierva de Cerinea", "Jabalí de Erimanto"]
for nombre in criaturas_capturadas:
    nodo = arbol.search(nombre)
    if nodo is not None:
        nodo.other_values["capturada"] = "Heracles"
        print(f"{nombre} -> capturada por Heracles")
print()


# i. Búsqueda por coincidencia (substring)
print("i. Búsqueda por coincidencia: 'Creta'")
def busqueda_coincidencia(tree, texto):
    def __recorrer(root):
        if root is not None:
            __recorrer(root.left)
            if texto.lower() in str(root.value).lower():
                print(root.value)
            __recorrer(root.right)
    __recorrer(tree.root)
busqueda_coincidencia(arbol, "Creta")
print()


# j. Eliminar Basilisco y Sirenas
print("j. Eliminando Basilisco y Sirenas")
for nombre in ["Basilisco", "Sirenas"]:
    eliminado, _ = arbol.delete_node(nombre)
    if eliminado:
        print(f"Eliminado: {eliminado}")
print()


# k. Modificar Aves del Estínfalo (Heracles derrotó a varias)
print("k. Modificando Aves del Estínfalo")
nodo_aves = arbol.search("Aves del Estínfalo")
if nodo_aves is not None:
    nodo_aves.other_values["derrotado_por"] = "Heracles (varias)"
    print("Aves del Estínfalo actualizado.")
print()


# l. Modificar nombre: Ladón -> Dragón Ladón (eliminar e insertar por cambio de clave)
print("l. Modificando nombre de Ladón a Dragón Ladón")
nodo_ladon = arbol.search("Ladón")
if nodo_ladon is not None:
    info_vieja = nodo_ladon.other_values
    arbol.delete_node("Ladón")
    arbol.insert_node("Dragón Ladón", info_vieja)
    print("Ladón renombrado a Dragón Ladón.")
print()


# m. Listado por nivel del árbol
print("m. Listado por nivel")
arbol.by_level()
print()


# n. Mostrar criaturas capturadas por Heracles
print("n. Criaturas capturadas por Heracles")
def listar_capturadas(tree, heroe):
    def __recorrer(root):
        if root is not None:
            __recorrer(root.left)
            if root.other_values.get("capturada") == heroe:
                print(root.value)
            __recorrer(root.right)
    __recorrer(tree.root)
listar_capturadas(arbol, "Heracles")
print()