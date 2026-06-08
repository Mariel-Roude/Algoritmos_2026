#Ejercicio 10:
# Dada una cola con las notificaciones de las aplicaciones de redes sociales de un Smartphone,
#de las cual se cuenta con la hora de la notificación, la aplicación que la emitió y el mensaje,
#resolver las siguientes actividades:
#a. escribir una función que elimine de la cola todas las notificaciones de Facebook;
#b. escribir una función que muestre todas las notificaciones de Twitter, cuyo mensaje incluya
#la palabra ‘Python’, si perder datos en la cola;
#c. utilizar una pila para almacenar temporáneamente las notificaciones producidas entre las 11:43 y las 15:57, y determinar cuántas son.


from cola import Queue
from pila import Stack


# a. Función que elimine de la cola todas las notificaciones de Facebook.
def eliminar_notificaciones_facebook(cola_notificaciones: Queue) -> None:
    tamaño_inicial = cola_notificaciones.size()
    
    for i in range(tamaño_inicial):
        notificacion_actual = cola_notificaciones.on_front()
        
        if notificacion_actual["app"].lower() == "facebook":
            cola_notificaciones.attention()
        else:
            cola_notificaciones.move_to_end()


# b. Función que muestre todas las notificaciones de Twitter, cuyo mensaje incluya la palabra ‘Python’, sin perder datos en la cola.
def mostrar_twitter_python(cola_notificaciones: Queue) -> None:
    tamaño_inicial = cola_notificaciones.size()
    print("\n--- Notificaciones de Twitter sobre Python ---")
    
    for i in range(tamaño_inicial):
        notificacion = cola_notificaciones.move_to_end()
        
        es_twitter = notificacion["app"].lower() == "twitter"
        tiene_python = "python" in notificacion["mensaje"].lower()
        
        if es_twitter and tiene_python:
            print(f"[{notificacion['hora']}] {notificacion['app']}: {notificacion['mensaje']}")


# c. Utilizar una pila para almacenar temporáneamente las notificaciones producidas entre las 11:43 y las 15:57, y determinar cuántas son.
def filtrar_por_horario_con_pila(cola_notificaciones: Queue) -> int:
    pila_temporal = Stack()  
    tamaño_inicial = cola_notificaciones.size()
    
    limite_inferior = 11 * 60 + 43  
    limite_superior = 15 * 60 + 57  
    
    for i in range(tamaño_inicial):
        notificacion_actual = cola_notificaciones.on_front()
        
        partes_hora = notificacion_actual["hora"].split(":")
        minutos_totales = int(partes_hora[0]) * 60 + int(partes_hora[1])
        
        if limite_inferior <= minutos_totales <= limite_superior:
            notificacion = cola_notificaciones.attention()
            pila_temporal.push(notificacion)
        else:
            cola_notificaciones.move_to_end()
            
    cantidad_notificaciones = pila_temporal.size()
    return cantidad_notificaciones



# Prueba

if __name__ == "__main__":
    mis_notificaciones = Queue()
    
    mis_notificaciones.arrive({"hora": "10:15", "app": "Facebook", "mensaje": "Juan comentó tu foto"})
    mis_notificaciones.arrive({"hora": "11:50", "app": "Twitter", "mensaje": "Aprendiendo Python básico hoy!"}) 
    mis_notificaciones.arrive({"hora": "12:00", "app": "Instagram", "mensaje": "A alguien le gustó tu historia"}) 
    mis_notificaciones.arrive({"hora": "14:10", "app": "Facebook", "mensaje": "Te etiquetaron en un meme nuevo"})       
    mis_notificaciones.arrive({"hora": "15:30", "app": "Twitter", "mensaje": "El desarrollo en Java es genial"}) 
    mis_notificaciones.arrive({"hora": "16:45", "app": "Twitter", "mensaje": "Guía avanzada de Python"})        

    print("=== Cola original inicial ===")
    mis_notificaciones.show()

    mostrar_twitter_python(mis_notificaciones)

    cantidad_en_rango = filtrar_por_horario_con_pila(mis_notificaciones)
    print(f"\n--- Actividad C: Cantidad de notificaciones almacenadas en la Pila: {cantidad_en_rango} ---")

    eliminar_notificaciones_facebook(mis_notificaciones)
    
    print("\n=== Cola final ===")
    print("(No tiene elementos de Facebook ni los retenidos previamente en la pila)")
    mis_notificaciones.show()