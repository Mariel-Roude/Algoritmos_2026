# Ejercicio_22:
#Se tienen una cola con personajes de Marvel Cinematic Universe (MCU), de los cuales se conoce el nombre del personaje, 
# el nombre del superhéroe y su género (Masculino M y Femenino F) –por ejemplo {Tony Stark, Iron Man, M}, 
# {Steve Rogers, Capitán América, M}, {Natasha Romanoff, Black Widow, F}, etc., desarrollar un algoritmo 
# que resuelva las siguientes actividades:
#a. determinar el nombre del personaje de la superhéroe Capitana Marvel;
#b. mostrar los nombre de los superhéroes femeninos;
#c. mostrar los nombres de los personajes masculinos;
#d. determinar el nombre del superhéroe del personaje Scott Lang;
#e. mostrar todos datos de los superhéroes o personaje cuyos nombres comienzan con la letra S;
#f. determinar si el personaje Carol Danvers se encuentra en la cola e indicar su nombre de superhéroes.


from cola import Queue


#a. Determinar el nombre del personaje de la superheroína Capitana Marvel.
def buscar_personaje_capitana_marvel(cola_mcu: Queue) -> None:
    tamaño_inicial = cola_mcu.size()
    encontrado = False
    
    for i in range(tamaño_inicial):
        actual = cola_mcu.move_to_end()
        
        if actual["heroe"].lower() == "capitana marvel":
            print(f"\n[A] El nombre real de Capitana Marvel es: {actual['personaje']}")
            encontrado = True
            
    if not encontrado:
        print("\n[A] Capitana Marvel no se encuentra en la cola.")


# b. Nombres de los superhéroes femeninos.
def mostrar_superheroes_femeninos(cola_mcu: Queue) -> None:
    tamaño_inicial = cola_mcu.size()
    print("\n[B] --- Superhéroes Femeninos ---")
    
    for i in range(tamaño_inicial):
        actual = cola_mcu.move_to_end()
        if actual["genero"].upper() == "F":
            print(f"- {actual['heroe']}")


#c. Nombres de los personajes masculinos.
def mostrar_personajes_masculinos(cola_mcu: Queue) -> None:
    tamaño_inicial = cola_mcu.size()
    print("\n[C] --- Personajes Masculinos (Nombres Reales) ---")
    
    for i in range(tamaño_inicial):
        actual = cola_mcu.move_to_end()
        if actual["genero"].upper() == "M":
            print(f"- {actual['personaje']}")


#d. Determinar el nombre del superhéroe del personaje Scott Lang.
def buscar_heroe_scott_lang(cola_mcu: Queue) -> None:
    tamaño_inicial = cola_mcu.size()
    encontrado = False
    
    for i in range(tamaño_inicial):
        actual = cola_mcu.move_to_end()
        
        if actual["personaje"].lower() == "scott lang":
            print(f"\n[D] El nombre de superhéroe de Scott Lang es: {actual['heroe']}")
            encontrado = True
            
    if not encontrado:
        print("\n[D] Scott Lang no se encuentra en la cola.")


# e. Mostrar todos los datos de los superhéroes o personajes cuyos nombres comienzan con la letra S.
def mostrar_datos_con_letra_s(cola_mcu: Queue) -> None:
    tamaño_inicial = cola_mcu.size()
    print("\n[E] --- Datos de personajes/superhéroes que empiezan con 'S' ---")
    
    for i in range(tamaño_inicial):
        actual = cola_mcu.move_to_end()
       
        empieza_personaje_s = actual["personaje"].lower().startswith("s")
        empieza_heroe_s = actual["heroe"].lower().startswith("s")
        
        if empieza_personaje_s or empieza_heroe_s:
            print(f"- Personaje: {actual['personaje']} | Héroe: {actual['heroe']} | Género: {actual['genero']}")


# f. Determinar si el personaje Carol Danvers se encuentra en la cola e indicar su nombre de superhéroe.
def verificar_carol_danvers(cola_mcu: Queue) -> None:
    tamaño_inicial = cola_mcu.size()
    encontrado = False
    
    for i in range(tamaño_inicial):
        actual = cola_mcu.move_to_end()
        if actual["personaje"].lower() == "carol danvers":
            print(f"\n[F] Carol Danvers está en la cola. Su nombre de superhéroe es: {actual['heroe']}")
            encontrado = True
            
    if not encontrado:
        print("\n[F] Carol Danvers no se encuentra en la cola.")



# Prueba
if __name__ == "__main__":
    cola_marvel = Queue()
    
    cola_marvel.arrive({"personaje": "Tony Stark", "heroe": "Iron Man", "genero": "M"})
    cola_marvel.arrive({"personaje": "Steve Rogers", "heroe": "Capitán América", "genero": "M"})  
    cola_marvel.arrive({"personaje": "Natasha Romanoff", "heroe": "Black Widow", "genero": "F"})
    cola_marvel.arrive({"personaje": "Carol Danvers", "heroe": "Capitana Marvel", "genero": "F"}) 
    cola_marvel.arrive({"personaje": "Scott Lang", "heroe": "Ant-Man", "genero": "M"})            
    cola_marvel.arrive({"personaje": "Wanda Maximoff", "heroe": "Scarlet Witch", "genero": "F"})   

    print("=== Cola original inicial ===")
    cola_marvel.show()

    buscar_personaje_capitana_marvel(cola_marvel) 
    mostrar_superheroes_femeninos(cola_marvel)
    mostrar_personajes_masculinos(cola_marvel)
    buscar_heroe_scott_lang(cola_marvel)
    mostrar_datos_con_letra_s(cola_marvel)
    verificar_carol_danvers(cola_marvel)