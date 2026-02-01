import json
import os
import logging

# ---------------- CONFIGURACIÓN LOGGING ----------------
logging.basicConfig(
    filename="agenda.log",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

ARCHIVO_JSON = "agenda.json"


# ---------------- CLASE BASE ----------------
class Persona:
    def __init__(self, nombre):
        self.nombre = nombre


# ---------------- HERENCIA ----------------
class Contacto(Persona):
    def __init__(self, nombre, telefono, correo, cumpleaños):
        super().__init__(nombre)
        self.telefono = telefono
        self.correo = correo
        self.cumpleaños = cumpleaños

    def to_dict(self):
        """Convierte el objeto a diccionario para JSON"""
        return {
            "Nombre": self.nombre,
            "Teléfono": self.telefono,
            "Correo": self.correo,
            "Cumpleaños": self.cumpleaños
        }


# ---------------- AGENDA ----------------
class Agenda:
    def __init__(self):
        self.contactos = self.cargar_agenda()

    def cargar_agenda(self):
        if os.path.exists(ARCHIVO_JSON):
            try:
                with open(ARCHIVO_JSON, "r", encoding="utf-8") as archivo:
                    logging.info("Agenda cargada desde JSON")
                    return json.load(archivo)
            except json.JSONDecodeError:
                logging.error("Error al leer JSON")
        return []

    def guardar_agenda(self):
        with open(ARCHIVO_JSON, "w", encoding="utf-8") as archivo:
            json.dump(self.contactos, archivo, indent=4, ensure_ascii=False)
        logging.info("Agenda guardada")

    def agregar_contacto(self, contacto: Contacto):
        self.contactos.append(contacto.to_dict())
        self.guardar_agenda()
        logging.info(f"Contacto agregado: {contacto.nombre}")

    def buscar_contacto(self, nombre):
        for contacto in self.contactos:
            if contacto["Nombre"].lower() == nombre.lower():
                return contacto
        return None

    def eliminar_contacto(self, nombre):
        contacto = self.buscar_contacto(nombre)
        if contacto:
            self.contactos.remove(contacto)
            self.guardar_agenda()
            logging.info(f"Contacto eliminado: {nombre}")
            return True
        return False

    def mostrar_contactos(self):
        if not self.contactos:
            print("La agenda está vacía.")
            return

        for i, c in enumerate(self.contactos, start=1):
            print(f"\nContacto {i}")
            print("Nombre:", c["Nombre"])
            print("Teléfono:", c["Teléfono"])
            print("Correo:", c["Correo"])
            d, m, a = c["Cumpleaños"]
            print(f"Cumpleaños: {d:02d}/{m:02d}/{a}")


# ---------------- APLICACIÓN ----------------
class AgendaApp:
    def __init__(self):
        self.agenda = Agenda()

    def insertar_contacto(self):
        print("\n--- Nuevo contacto ---")
        nombre = input("Nombre: ")
        correo = input("Correo: ")

        try:
            telefono = int(input("Teléfono: "))
        except ValueError:
            print("Teléfono inválido")
            return

        try:
            dia, mes, año = map(int, input("Cumpleaños (DD/MM/AAAA): ").split("/"))
        except ValueError:
            print("Formato de fecha inválido")
            return

        contacto = Contacto(nombre, telefono, correo, [dia, mes, año])
        self.agenda.agregar_contacto(contacto)
        print("Contacto agregado correctamente")

    def buscar_contacto(self):
        nombre = input("Nombre a buscar: ")
        contacto = self.agenda.buscar_contacto(nombre)

        if contacto:
            print("\n--- Contacto encontrado ---")
            print("Nombre:", contacto["Nombre"])
            print("Teléfono:", contacto["Teléfono"])
            print("Correo:", contacto["Correo"])
        else:
            print("Contacto no encontrado")

    def eliminar_contacto(self):
        nombre = input("Nombre a eliminar: ")
        if self.agenda.eliminar_contacto(nombre):
            print("Contacto eliminado")
        else:
            print("Contacto no encontrado")

    def menu(self):
        while True:
            print("\n--- MENÚ ---")
            print("1. Insertar contacto")
            print("2. Buscar contacto")
            print("3. Eliminar contacto")
            print("4. Mostrar contactos")
            print("5. Salir")

            opcion = input("Opción: ")

            if opcion == "1":
                self.insertar_contacto()
            elif opcion == "2":
                self.buscar_contacto()
            elif opcion == "3":
                self.eliminar_contacto()
            elif opcion == "4":
                self.agenda.mostrar_contactos()
            elif opcion == "5":
                print("Saliendo...")
                break
            else:
                print("Opción inválida")


# ---------------- EJECUCIÓN ----------------
if __name__ == "__main__":
    app = AgendaApp()
    app.menu()