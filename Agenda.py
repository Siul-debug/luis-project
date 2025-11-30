agenda = []

def insertar_elementos(agenda):
    print("\n--- Insertar nuevo contacto ---")
    
    nombre = (input("Nombre: "))
    tlf = int(input("Número de teléfono: "))
    correo = (input("Correo electrónico: "))
    cumpleaños = (input("Cumpleaños (DD/MM/AAAA): "))
    dia, mes, año = map(int,cumpleaños.split("/"))
 
    contacto = {
        "Nombre:": nombre,
        "Teléfono:": tlf,
        "Correo:": correo,
        "Cumpleaños:": [dia,mes,año]
        }

    if nombre == "" or tlf == "" or correo == "" or cumpleaños == "":
        print("Debe rellenar todos los campos.")
    else:
        agenda.append(contacto)
        print("Contacto agregado correctamente.")
    
    return agenda


def buscar_elementos(agenda):
    nombre_buscar = input("Ingrese el nombre del contacto a buscar: ")

    for contacto in agenda:
        if contacto["Nombre"].lower() == nombre_buscar.lower():
            print("--- Contacto encontrado ---")
            print("Nombre: " + contacto["Nombre"])
            print("Teléfono: " + contacto["Teléfono"])
            print("Correo: " + contacto["Correo"])
            print("Cumpleaños: " + contacto["Cumpleaños"])
            return agenda
    
    print("No se encontró el contacto.")
    return agenda


def modificar_elementos(agenda):
    nombre_modificar = input("Ingrese el nombre del contacto a modificar: ")

    for contacto in agenda:
        if contacto["Nombre"].lower() == nombre_modificar.lower():
            print("Datos actuales de " + contacto["Nombre"] + ":")
            print("Teléfono: " + contacto["Teléfono"])
            print("Correo: " + contacto["Correo"])
            print("Cumpleaños: " + contacto["Cumpleaños"])

            tlf = input("Nuevo número de teléfono (dejar vacío para no cambiar): ")
            if tlf:
                contacto["Teléfono"] = tlf
            
            correo = input("Nuevo correo electrónico (dejar vacío para no cambiar): ")
            if correo:
                contacto["Correo"] = correo

            cumpleaños = input("Nuevo cumpleaños (DD/MM/AAAA) (dejar vacío para no cambiar): ")
            if cumpleaños:
                contacto["Cumpleaños"] = cumpleaños
            
            print("Contacto " + contacto["Nombre"] + " actualizado.")
            return agenda
    
    print("No se encontró el contacto a modificar.")
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
    nombre_eliminar = input("Ingrese el nombre del contacto a eliminar: ")

    for contacto in agenda:
        if contacto["Nombre"].lower() == nombre_eliminar.lower():
            agenda.remove(contacto)
            print("Contacto " + nombre_eliminar + " eliminado correctamente.")
            return agenda
    
    print("No se encontró el contacto a eliminar.")
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