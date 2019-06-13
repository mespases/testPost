from pprint import  pprint
from pymongo import MongoClient
from pymongo import ReturnDocument
from bson.objectid import ObjectId

class MongoDBManagement:

    def __init__(self):
        # Conexion con mongoDB
        self.cliente = MongoClient('localHost', 27017)
        self.db = self.cliente.Prueba1

        # Variables para cada collection
        self.collection_coche = self.db['Coches']
        self.collection_agencia = self.db['Agencia']
        self.collection_avalados = self.db['Avalados']
        self.collection_clientes = self.db['Clientes']

        # Abrimos el menu
        self.menu()


    # Inserta 1 regustro dentro de la collection seleccionada
    def insert_one_collection(self, collection):
        # Gestionamos exceptions
        try:
            # Insertamos en agencia
            if collection.title() == "Agencia":
                # Pedimos informacion
                nombre = raw_input("Inserta el nombre de la agencia: ")

                self.collection_agencia.insert_one({
                    "NombreAgencia": nombre
                })

            # Insertamos en avalados
            elif collection.title() == "Avalados":
                # Pedimos informacion
                idAval = raw_input("Introduce el id del aval: ")
                idClienteAval = raw_input("Introduce el id del cliente: ")
                idClienteAvalado = raw_input("Introduce la id del cliente avalado: ")
                avalado = raw_input("Introduce el avalado: ")

                self.collection_avalados.insert_one({
                    "IdAvala": idAval,
                    "IdClientesAvala": idClienteAval,
                    "IdClientesAvalado": idClienteAvalado,
                    "Avalado": avalado
                })

            # Insertamos en clientes
            elif collection.title() == "Clientes":
                # Pedimos informacion
                DNI = raw_input("Introduce el DNI del cliente: ")
                codigo = raw_input("Introduce el codigo del cliente: ")
                nombreCliente = raw_input("Introduce el nombre del cliente: ")
                apellidos = raw_input("Introduce los apellidos del cliente: ")
                direccion = raw_input("Introduce la direccion del cliente: ")
                telefono = raw_input("Introduce el telefono del cliente: ")

                self.collection_clientes.insert_one({
                  "DNI": DNI,
                  "CodigoUnico": codigo,
                  "Nombre": nombreCliente,
                  "Apellidos": apellidos,
                  "Direccion": direccion,
                  "Telefono": telefono
              })

            # Insertamos en coches
            elif collection.title() == "Coches":
                # Pedimos informacion
                matricula = raw_input("Introduce una matricula: ")
                marca = raw_input("Introduce la marca del coche: ")
                modelo = raw_input("Introduce el modelo del coche: ")
                color = raw_input("Introduce el color del coche: ")
                deposito = raw_input("Introduce la capacidad del deposito: ")
                precio = raw_input("Introduce el precio por dia de alquiler del coche: ")

                self.collection_coche.insert_one({
                    "Matricula": matricula,
                    "Marca": marca,
                    "Modelo": modelo,
                    "Color": color,
                    "Deposito": deposito,
                    "PrecioAlquiler": precio
                })

            # Muestra en caso de que la collection insertada no exista
            else:
                print("Collection introducida incorrecta")

        # Mostramos mensaje de exception
        except:
            print("Opcion introducida incorrecta")


    # Elimina una row de una collection
    def Delete(self, collection):
        # Gestionamos exceptions
        try:
            # Eliminamos en agencia
            if collection.title() == "Agencia":
                # Pedimos informacion
                nombre = raw_input("Inserta el nombre de la agencia: ")

                self.collection_agencia.deleteOne({
                "NombreAgencia" : nombre
                })

            # Eliminamos en avalados
            elif collection.title() == "Avalados":
                # Pedimos informacion
                idAval = raw_input("Introduce el id del aval: ")
                idClienteAval = raw_input("Introduce el id del cliente: ")
                idClienteAvalado = raw_input("Introduce la id del cliente avalado: ")
                avalado = raw_input("Introduce el avalado: ")

                self.collection_avalados.deleteOne({
                    "IdAvala" : idAval,
                    "IdClientesAvala" : idClienteAval,
                    "IdClientesAvalado" : idClienteAvalado,
                    "Avalado" : avalado
                })

            # Eliminamos en clientes
            elif collection.title() == "Clientes":
                # Pedimos informacion
                DNI = raw_input("Introduce el DNI del cliente: ")
                codigo = raw_input("Introduce el codigo del cliente: ")
                nombreCliente = raw_input("Introduce el nombre del cliente: ")
                apellidos = raw_input("Introduce los apellidos del cliente: ")
                direccion = raw_input("Introduce la direccion del cliente: ")
                telefono = raw_input("Introduce el telefono del cliente: ")

                self.collection_clientes.deleteOne({
                    "DNI": DNI,
                    "CodigoUnico": codigo,
                    "Nombre": nombreCliente,
                    "Apellidos": apellidos,
                    "Direccion": direccion,
                    "Telefono": telefono
                })

            # Eiminamos en coches
            elif collection.title() == "Coches":
                # Pedimos informacion
                matricula = raw_input("Introduce una matricula: ")
                marca = raw_input("Introduce la marca del coche: ")
                modelo = raw_input("Introduce el modelo del coche: ")
                color = raw_input("Introduce el color del coche: ")
                deposito = raw_input("Introduce la capacidad del deposito: ")
                precio = raw_input("Introduce el precio por dia de alquiler del coche: ")

                self.collection_coche.deleteOne({
                    "Color": color,
                    "Marca": marca,
                    "PrecioAlquiler": precio,
                    "Deposito": deposito,
                    "Modelo": modelo,
                    "Matricula": matricula
                })

            # Muestra en caso de que la collection insertada no exista
            else:
                print("Collection introducida incorrecta")

        # Mostramos mensaje de exception
        except:
            print("Opcion introducida incorrecta")

    # Menu, pediremos una tarea a realizar y luego pediremos en que collection quiere realizar esa tarea
    def menu(self):
        # id " i = insert, d = delete"
        id = raw_input("Elige una opcion, Insert o Delete: ")

        # Inserta datos dentro de una collection
        if id.title() == "Insert":
            opcion = raw_input("""
Collections disponibles en nuestra base de datos:
Agencia
Avalados
Clientes
Coches
Eliga una collection: """)
            self.insert_one_collection(opcion)

        # Borramos los datos de la tabla que nos indiquen
        elif id.title() == "Delete":
            opcion = raw_input("""
Collections disponibles en nuestra base de datos:
Agencia
Avalados
Clientes
Coches
Eliga una collection: """)

            self.Delete(opcion)

if __name__ == "__main__":
    mongoDB = MongoDBManagement()
    #mongoDB.insert_one_car()

# Queda por hacer "inserts" y eliminar, posteriormente crear un menu para gestionar todo