from opciones import ingresar, buscar, eliminar

while True:
    print("Menú principal")
    print("1.- Ingresar usuario.")
    print("2.- Buscar usuario.")
    print("3.- Eliminar usuario.")
    print("4.- Salir.")

    opcion = int(input("Elija una opción: "))

    if opcion == 1:
        ingresar()
    elif opcion == 2:
        buscar()
    elif opcion == 3:
        eliminar()
    elif opcion == 4:
        print("Hasta pronto!")
        break
    else:
        print("Debe elegir un número del 1 al 4, intentelo de nuevo.")