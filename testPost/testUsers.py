from flask_login import UserMixin
from pymongo import MongoClient
import json


class User(UserMixin):
    # Conexion con mongo
    cliente = MongoClient('localHost', 27017)
    db = cliente.Practica
    collection_usuarios = db['Usuarios']

    email = []
    password = []

    def __init__(self, email="", password=""):
        self.cargarUsuarios()
        if email != "" and password != "":
            self.email.append(email)
            self.password.append(password)
            self.saveUser()

    def get_id(self):
        return self.email

    def cargarUsuarios(self):
        for usuario in self.collection_usuarios.find():
            self.email.append(usuario.get("Email"))
            self.password.append(usuario.get("Password"))

    def is_anonymous(self):
        return False

    def is_authenticated(self):
        return True

    def saveUser(self):
        datos_json = {
            "Email": self.email[-1],
            "Password": self.password[-1]
        }

        datos_json = json.dumps(datos_json)
        self.collection_usuarios.insert_one(json.loads(datos_json))