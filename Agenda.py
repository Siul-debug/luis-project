import json
import os
import logging


# =====================================================
# CONFIGURACIÓN LOGGING
# =====================================================

logging.basicConfig(
    filename="agenda.log",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

ARCHIVO_JSON = "agenda.json"


# =====================================================
# CLASE BASE
# =====================================================

class Contacto:

    def __init__(self, nombre, telefono, correo, cumpleaños):

        self.nombre = nombre
        self.telefono = telefono
        self.correo = correo
        self.cumpleaños = cumpleaños


    def mostrar(self):

        d, m, a = self.cumpleaños

        print("Nombre:", self.nombre)
        print("Teléfono:", self.telefono)
        print("Correo:", self.correo)
        print(f"Cumpleaños: {d:02d}/{m:02d}/{a}")


    def to_dict(self):

        return {

            "tipo": "normal",

            "nombre": self.nombre,
            "telefono": self.telefono,
            "correo": self.correo,
            "cumpleaños": self.cumpleaños
        }


    @staticmethod
    def from_dict(data):

        if data["tipo"] == "especial":

            return ContactoEspecial(
                data["nombre"],
                data["telefono"],
                data["correo"],
                data["cumpleaños"],
                data["alias"]
            )

        return Contacto(
            data["nombre"],
            data["telefono"],
            data["correo"],
            data["cumpleaños"]
        )


# =====================================================
# SUBCLASE
# =====================================================

class ContactoEspecial(Contacto):

    def __init__(self, nombre, telefono, correo, cumpleaños, alias):

        super().__init__(nombre, telefono, correo, cumpleaños)

        self.alias = alias


    def mostrar(self):

        super().mostrar()

        print("Alias:", self.alias)


    def to_dict(self):

        data = super().to_dict()

        data["tipo"] = "especial"

        data["alias"] = self.alias

        return data


# =====================================================
# AGENDA
# =====================================================

class Agenda:

    def __init__(self):

        self.contactos = self.cargar_agenda()


    def cargar_agenda(self):

        contactos = []

        if os.path.exists(ARCHIVO_JSON):

            try:

                with open(ARCHIVO_JSON, "r", encoding="utf-8") as archivo:

                    datos = json.load(archivo)

                    for d in datos:

                        contactos.append(Contacto.from_dict(d))

                logging.info("Agenda cargada")

            except:

                logging.error("Error cargando agenda")

        return contactos


    def guardar_agenda(self):

        datos = [c.to_dict() for c in self.contactos]

        with open(ARCHIVO_JSON, "w", encoding="utf-8") as archivo:

            json.dump(datos, archivo, indent=4, ensure_ascii=False)

        logging.info("Agenda guardada")


    def agregar_contacto(self, contacto):

        self.contactos.append(contacto)

        self.guardar_agenda()

        logging.info(f"Contacto agregado: {contacto.nombre}")


    def buscar_contacto(self, nombre):

        for c in self.contactos:

            if c.nombre.lower() == nombre.lower():

                return c

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

            print("Agenda vacía")

            return

        for i, c in enumerate(self.contactos, 1):

            print("\n------------------")

            print(f"Contacto {i}")

            print("------------------")

            c.mostrar()


# =====================================================
# APP
# =====================================================

class AgendaApp:

    def __init__(self):

        self.agenda = Agenda()


    # INSERTAR

    def insertar_contacto(self):

        print("\n==============================")
        print("     NUEVO CONTACTO")
        print("==============================")

        print("1. Contacto normal")
        print("2. Contacto especial")

        tipo = input("\nSeleccione tipo: ")


        nombre = input("Nombre: ")

        correo = input("Correo: ")


        try:

            telefono = int(input("Teléfono: "))

        except ValueError:

            print("Teléfono inválido")

            return


        try:

            dia, mes, año = map(
                int,
                input("Cumpleaños (DD/MM/AAAA): ").split("/")
            )

        except ValueError:

            print("Fecha inválida")

            return


        if tipo == "2":

            alias = input("Alias: ")

            contacto = ContactoEspecial(
                nombre,
                telefono,
                correo,
                [dia, mes, año],
                alias
            )

        else:

            contacto = Contacto(
                nombre,
                telefono,
                correo,
                [dia, mes, año]
            )


        self.agenda.agregar_contacto(contacto)

        print("\n✅ Contacto agregado correctamente")


    # BUSCAR

    def buscar_contacto(self):

        print("\n==============================")
        print("     BUSCAR CONTACTO")
        print("==============================")

        nombre = input("Nombre: ")

        contacto = self.agenda.buscar_contacto(nombre)

        if contacto:

            print("\nContacto encontrado:\n")

            contacto.mostrar()

        else:

            print("\n❌ Contacto no encontrado")


    # ELIMINAR

    def eliminar_contacto(self):

        print("\n==============================")
        print("    ELIMINAR CONTACTO")
        print("==============================")

        nombre = input("Nombre: ")

        if self.agenda.eliminar_contacto(nombre):

            print("\n✅ Contacto eliminado")

        else:

            print("\n❌ Contacto no encontrado")


    # MOSTRAR

    def mostrar_contactos(self):

        print("\n==============================")
        print("     LISTA DE CONTACTOS")
        print("==============================")

        self.agenda.mostrar_contactos()


    # MENU

    def menu(self):

        while True:

            print("\n=================================")
            print("         AGENDA PERSONAL")
            print("=================================")

            print("1. Insertar contacto")
            print("2. Buscar contacto")
            print("3. Eliminar contacto")
            print("4. Mostrar contactos")
            print("5. Salir")

            opcion = input("\nSeleccione una opción: ")


            if opcion == "1":

                self.insertar_contacto()

            elif opcion == "2":

                self.buscar_contacto()

            elif opcion == "3":

                self.eliminar_contacto()

            elif opcion == "4":

                self.mostrar_contactos()

            elif opcion == "5":

                print("\n👋 Cerrando agenda...")

                break

            else:

                print("\n❌ Opción inválida")


# =====================================================
# MAIN
# =====================================================

if __name__ == "__main__":

    app = AgendaApp()

    app.menu()