from flask_login import UserMixin
from pymongo import MongoClient
import json


class User(UserMixin):
    """ Clase Users con herencia de UserMixin, la clase esta preparada para usarse
        con mongodb. Clase preparada para login de usuarios mediante flask-WTForms"""

    # Conexion con mongo
    cliente = MongoClient('localHost', 27017)
    db = cliente.Practica
    collection_usuarios = db['Usuarios']

    email = []
    password = []
    role = []

    def __init__(self, email="", password="", role=""):
        self.loadUsers()
        if email != "" and password != "":
            self.email.append(email)
            self.password.append(password)
            self.role.append(role)
            self.saveUser()


    def loadUsers(self):
        for usuario in self.collection_usuarios.find():
            self.email.append(usuario.get("Email"))
            self.password.append(usuario.get("Password"))
            self.role.append(usuario.get("Role"))


    def saveUser(self):
        datos_json = {
            "Email": self.email[-1],
            "Password": self.password[-1],
            "Role": self.role[-1]
        }

        datos_json = json.dumps(datos_json)
        self.collection_usuarios.insert_one(json.loads(datos_json))


    def get_id(self):
        return self.email


    def is_anonymous(self):
        return False

    def is_authenticated(self):
        return True