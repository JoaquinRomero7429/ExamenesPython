# Crea una lista vacia llamada tareas donde guardara las tareas que ingrese el usuario
tareas = []

# Bucle infinito que muetra las opciones 
while True:
    # Se imprime el menú de opciones
    print("****************************")
    print("        MENÚ DE OPCIONES    ")
    print("****************************")
    print("1: Añadir tarea")
    print("2: Ver tareas")
    print("3: Completar tarea")
    print("4: Salir")
    print("****************************")
    
    # le pide al usuario que ingrese una opcion
    opcion = input("Elige una opción: ")

    # Si elige 1 se añade una tarea a la lista
    if opcion == "1":
        tarea = input("Nombre o descripcion de la tarea: ")
        tareas.append(tarea)  # Se agrega la tarea a la lista

    # Si elige 1 se muestran las tareas en pantalla
    elif opcion == "2":
        if tareas:
            # Se recorren las tareas y se muestran con su número correspondiente
            for i in range(1, 999):  # es el limite de tareas 
                if i <= len(tareas):  
                    print(f"{i}. {tareas[i - 1]}")
                else:
                    break  # se cierra el bucle si ya se mostarron las tareas
        else:
            print("No hay tareas.")  # Si la lista esta vacia muestra este mensaje

    # Si el usuario elije 3 marca como completada la tarea , la elimina 
    elif opcion == "3":
        if tareas:
            num = int(input("Ingrese el numero de la tarea que desea marcar como completada: ")) - 1 
            if num >= 0 and num < 999:  # se asegura que el umero este dentro de los limites 
                if num < len(tareas):  
                    tareas.pop(num)  # Elimina la tarea con el numero que ingrese el usuario usando el metodo pop
                else:
                    print("Número inválido.")  # muestra el menasaje si el numero no cumple la anterior condicion
            else:
                print("Número inválido.")  # muestra el mensaje si el numero es negativo o demaciado grande
        else:
            print("No hay tareas para completar.")  # muestra el mensaje si no hay tareas 

    # Si el usuario elige 4 se cierra el programa
    elif opcion == "4":
        print("Gracias por utilizar este programa")
        break  # sale del bucle del menu y cierra el programa
