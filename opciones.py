usuarios_dic = []

def ingresar():
    while True:
        try:
            nombre = str(input("Ingrese el nombre del usuario: "))
        except:
            print("Debe ingresar un nombre con letras, intentelo de nuevo.")
            continue

        verifica_nombre = False
        for usu in usuarios_dic:
            if usu["Nombre"] == nombre:
                verifica_nombre = True
                break
        
        if verifica_nombre:
            print("Ya existe un usuario con ese nombre, intentelo de nuevo.")
        else:
            break

    while True:
        try:
            sexo = str(input("Ingrese el sexo del usuario (F/M): "))
        except:
            print("Debe ingresar el sexo ingresando F (femenino) o M (masculino), intentelo de nuevo.")

        if sexo != "F" and sexo != "M":
            print("Debe ingresar el sexo ingresando F (femenino) o M (masculino), intentelo de nuevo.")
        else:
            break

    while True:
        try:
            contraseña = input("Ingrese la contraseña del usuario: ")
        except:
            print("Debe ingresar una contraseña con minimo ocho caracteres, una letra, un número y sin espacio en blanco, intentelo de nuevo.")

        if len(contraseña) < 8:
            print("La contraseña debe tener minimo ocho caracteres.")
            continue
        

        verifica_letra = False
        for car in contraseña:
            if car.isalpha():
                verifica_letra = True
                break
        
        if verifica_letra:
            pass
        else:
            print("La contraseña debe tener minimo una letra, intentelo de nuevo.")
            continue

        
        verifica_numero = False
        for car in contraseña:
            if car.isdigit():
                verifica_numero = True
                break

        if verifica_numero:
            pass
        else:
            print("La contraseña debe tener minimo un número, intentelo de nuevo.")
            continue


        verifica_espacio = False
        for car in contraseña:
            if car.isspace():
                verifica_espacio = True
                break

        if verifica_espacio:
            print("La contraseña no debe tener ningún espacio, intentelo de nuevo.")
            continue
        else:
            break
        
    usuario_creado = {
        "Nombre": nombre,
        "Sexo": sexo,
        "Contraseña": contraseña
        } 

    usuarios_dic.append(usuario_creado)
    print("Usuario creado correctamente!")

def buscar():
    buscar_nombre = str(input("Ingrese el nombre a buscar: "))

    encontrados = []
    for usu in usuarios_dic:
        if usu["Nombre"] == buscar_nombre:
            encontrados.append(usu)

    if encontrados:
        print(f"El sexo del usuario es: {usu["Sexo"]} y la contraseña es: {usu["Contraseña"]}")
    else:
        print("El usuario no se encuentra.")

def eliminar():
    eliminar_nombre = str(input("Ingrese el nombre a eliminar: "))

    encontrados = []
    for usu in usuarios_dic:
        if usu["Nombre"] == eliminar_nombre:
            encontrados.append(usu)

    if encontrados:
        for usu in encontrados:
            usuarios_dic.remove(usu)
        print("Usuario eliminado con exito.")
    else:
        print("No se pudo eliminar el usuario.")
    