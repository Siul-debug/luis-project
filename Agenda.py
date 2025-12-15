agenda = []

def insertar_elementos(agenda):
    print("\n--- Insertar nuevo contacto ---")

    nombre = input("Nombre: ")
    correo = input("Correo electrónico: ")

    # Teléfono
    try:
        tlf = int(input("Número de teléfono: "))
    except:
        print("Error: el teléfono debe ser un número.")
        return agenda

    # Cumpleaños
    cumpleaños = input("Cumpleaños (DD/MM/AAAA): ")
    try:
        dia, mes, año = map(int, cumpleaños.split("/"))
    except:
        print("Error: el cumpleaños debe tener el formato DD/MM/AAAA.")
        return agenda

    # Comprobar campos vacíos
    if nombre == "" or correo == "":
        print("Debe rellenar todos los campos.")
        return agenda

    contacto = {
        "Nombre": nombre,
        "Teléfono": tlf,
        "Correo": correo,
        "Cumpleaños": [dia, mes, año]
    }

    agenda.append(contacto)
    print("Contacto agregado correctamente.")
    return agenda



def buscar_elementos(agenda):
    nombre_buscar = input("Ingrese el nombre del contacto a buscar: ")

    for contacto in agenda:
        if contacto["Nombre"].lower() == nombre_buscar.lower():
            print("--- Contacto encontrado ---")
            print("Nombre: " + contacto["Nombre"])
            print("Teléfono: " + str(contacto["Teléfono"]))  # Convertimos el teléfono a texto
            print("Correo: " + contacto["Correo"])

            # Imprimir cumpleaños con formato simple
            cumple = contacto["Cumpleaños"]
            print("Cumpleaños: {} / {2} / {}".format(cumple[0], cumple[1], cumple[2]))  # Día/Mes/Año
            
            return agenda
    
    print("No se encontró el contacto.")
    return agenda



def modificar_elementos(agenda):
    nombre_modificar = input("Ingrese el nombre del contacto a modificar: ")

    for contacto in agenda:
        if contacto["Nombre"].lower() == nombre_modificar.lower():
            print("Datos actuales de " + contacto["Nombre"] + ":")
            print("Teléfono:", contacto["Teléfono"])
            print("Correo:", contacto["Correo"])
            print("Cumpleaños:", contacto["Cumpleaños"])

            # Validar si el teléfono es vacío antes de intentar convertir
            tlf = input("Nuevo número de teléfono (dejar vacío para no cambiar): ")
            if tlf:  # Solo convertimos si no está vacío
                try:
                    contacto["Teléfono"] = int(tlf)  # Convertimos el teléfono a número
                except:
                    print("Error: El teléfono debe ser un número.")

            # Validar si el correo es vacío antes de cambiarlo
            correo = input("Nuevo correo electrónico (dejar vacío para no cambiar): ")
            if correo:  # Solo cambiamos si no está vacío
                contacto["Correo"] = correo

            # Validar si el cumpleaños es vacío antes de intentar convertirlo
            cumpleaños = input("Nuevo cumpleaños (DD/MM/AAAA) (dejar vacío para no cambiar): ")
            if cumpleaños:  # Solo convertimos si no está vacío
                try:
                    dia, mes, año = map(int, cumpleaños.split("/"))  # Intentamos dividir y convertir
                    contacto["Cumpleaños"] = [dia, mes, año]
                except:
                    print("Error: El cumpleaños debe tener el formato DD/MM/AAAA.")

            print("Contacto actualizado.")
            return agenda

    print("No se encontró el contacto.")
    return agenda

def eliminar_elementos(agenda):
    nombre_eliminar = input("Ingrese el nombre del contacto a eliminar: ")

    for contacto in agenda:
        if contacto["Nombre"].lower() == nombre_eliminar.lower():
            agenda.remove(contacto)
            print("Contacto " + nombre_eliminar + " eliminado correctamente.")
            return agenda
    
    print("No se encontró el contacto a eliminar.")
    return agenda

def mostrar_todos(agenda):
    print("\n--- Lista de contactos ---")

    if not agenda:
        print("La agenda está vacía.")
        return agenda

    for i, contacto in enumerate(agenda, start=1):
        print(f"\nContacto {i}")
        print("Nombre:", contacto["Nombre"])
        print("Teléfono:", contacto["Teléfono"])
        print("Correo:", contacto["Correo"])
        
        cumple = contacto["Cumpleaños"]
        print(f"Cumpleaños: {cumple[0]:02d}/{cumple[1]:02d}/{cumple[2]}")

    return agenda

while True:
    print("\n--- Menú ---")
    print("1. Insertar nuevo contacto")
    print("2. Buscar contacto")
    print("3. Modificar contacto")
    print("4. Eliminar contacto")
    print("5. Mostrar todos los contactos")
    print("6. Salir")

    opcion = input("Elige una opción: ")

    if opcion == "1":
        agenda = insertar_elementos(agenda)
    elif opcion == "2":
        agenda = buscar_elementos(agenda)
    elif opcion == "3":
        agenda = modificar_elementos(agenda)
    elif opcion == "4":
        agenda = eliminar_elementos(agenda)
    elif opcion == "5":
        agenda = mostrar_todos(agenda)
    elif opcion == "6":
        print("Saliendo...")
        break
    else:
        print("Opción no válida. Intenta de nuevo.")