import json
import os
import logging

# ---------------- CONFIGURACIÓN LOGGING ----------------
logging.basicConfig(
    filename="agenda.log",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

# ---------------- JSON ----------------
ARCHIVO_JSON = "agenda.json"

def cargar_agenda():
    if os.path.exists(ARCHIVO_JSON):
        with open(ARCHIVO_JSON, "r", encoding="utf-8") as archivo:
            try:
                logging.info("Agenda cargada desde archivo JSON")
                return json.load(archivo)
            except json.JSONDecodeError:
                logging.error("Error al leer el archivo JSON")
                return []
    return []

def guardar_agenda(agenda):
    with open(ARCHIVO_JSON, "w", encoding="utf-8") as archivo:
        json.dump(agenda, archivo, indent=4, ensure_ascii=False)
    logging.info("Agenda guardada en archivo JSON")

# ---------------- AGENDA ----------------
agenda = cargar_agenda()

# ---------------- FUNCIONES ----------------
def insertar_elementos(agenda):
    print("\n--- Insertar nuevo contacto ---")

    nombre = input("Nombre: ")
    correo = input("Correo electrónico: ")

    try:
        tlf = int(input("Número de teléfono: "))
    except:
        print("Error: el teléfono debe ser un número.")
        logging.error("Teléfono inválido al insertar contacto")
        return agenda

    cumpleaños = input("Cumpleaños (DD/MM/AAAA): ")
    try:
        dia, mes, año = map(int, cumpleaños.split("/"))
    except:
        print("Error: el cumpleaños debe tener el formato DD/MM/AAAA.")
        logging.error("Formato de cumpleaños inválido")
        return agenda

    if nombre == "" or correo == "":
        print("Debe rellenar todos los campos.")
        logging.warning("Intento de insertar contacto con campos vacíos")
        return agenda

    contacto = {
        "Nombre": nombre,
        "Teléfono": tlf,
        "Correo": correo,
        "Cumpleaños": [dia, mes, año]
    }

    agenda.append(contacto)
    logging.info(f"Contacto agregado: {nombre}")
    print("Contacto agregado correctamente.")
    return agenda


def buscar_elementos(agenda):
    nombre_buscar = input("Ingrese el nombre del contacto a buscar: ")

    for contacto in agenda:
        if contacto["Nombre"].lower() == nombre_buscar.lower():
            print("\n--- Contacto encontrado ---")
            print("Nombre:", contacto["Nombre"])
            print("Teléfono:", contacto["Teléfono"])
            print("Correo:", contacto["Correo"])

            cumple = contacto["Cumpleaños"]
            print(f"Cumpleaños: {cumple[0]:02d}/{cumple[1]:02d}/{cumple[2]}")

            logging.info(f"Contacto encontrado: {contacto['Nombre']}")
            return agenda

    print("No se encontró el contacto.")
    logging.warning(f"Contacto no encontrado: {nombre_buscar}")
    return agenda


def modificar_elementos(agenda):
    nombre_modificar = input("Ingrese el nombre del contacto a modificar: ")

    for contacto in agenda:
        if contacto["Nombre"].lower() == nombre_modificar.lower():
            print("\nDatos actuales:")
            print("Teléfono:", contacto["Teléfono"])
            print("Correo:", contacto["Correo"])
            print("Cumpleaños:", contacto["Cumpleaños"])

            tlf = input("Nuevo número de teléfono (dejar vacío para no cambiar): ")
            if tlf:
                try:
                    contacto["Teléfono"] = int(tlf)
                except:
                    print("Error: El teléfono debe ser un número.")
                    logging.error("Teléfono inválido al modificar contacto")

            correo = input("Nuevo correo electrónico (dejar vacío para no cambiar): ")
            if correo:
                contacto["Correo"] = correo

            cumpleaños = input("Nuevo cumpleaños (DD/MM/AAAA) (dejar vacío para no cambiar): ")
            if cumpleaños:
                try:
                    dia, mes, año = map(int, cumpleaños.split("/"))
                    contacto["Cumpleaños"] = [dia, mes, año]
                except:
                    print("Error: El cumpleaños debe tener el formato DD/MM/AAAA.")
                    logging.error("Cumpleaños inválido al modificar contacto")

            logging.info(f"Contacto modificado: {contacto['Nombre']}")
            print("Contacto actualizado.")
            return agenda

    print("No se encontró el contacto.")
    logging.warning(f"Intento de modificar contacto inexistente: {nombre_modificar}")
    return agenda


def eliminar_elementos(agenda):
    nombre_eliminar = input("Ingrese el nombre del contacto a eliminar: ")

    for contacto in agenda:
        if contacto["Nombre"].lower() == nombre_eliminar.lower():
            agenda.remove(contacto)
            logging.info(f"Contacto eliminado: {nombre_eliminar}")
            print(f"Contacto {nombre_eliminar} eliminado correctamente.")
            return agenda

    print("No se encontró el contacto a eliminar.")
    logging.warning(f"Intento de eliminar contacto inexistente: {nombre_eliminar}")
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

    logging.info("Mostrados todos los contactos")
    return agenda

# ---------------- MENÚ ----------------
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
        guardar_agenda(agenda)
    elif opcion == "2":
        agenda = buscar_elementos(agenda)
    elif opcion == "3":
        agenda = modificar_elementos(agenda)
        guardar_agenda(agenda)
    elif opcion == "4":
        agenda = eliminar_elementos(agenda)
        guardar_agenda(agenda)
    elif opcion == "5":
        agenda = mostrar_todos(agenda)
    elif opcion == "6":
        print("Saliendo...")
        logging.info("Aplicación cerrada por el usuario")
        break
    else:
        print("Opción no válida. Intenta de nuevo.")
        logging.warning("Opción de menú inválida")