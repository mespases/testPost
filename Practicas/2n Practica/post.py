from flask import Flask, request, render_template, redirect
from pymongo import MongoClient
import json
from io import open
from werkzeug.security import generate_password_hash, check_password_hash

app = Flask(__name__)

logueado = False

usuario_log = ""

# Conexion con mongo
cliente = MongoClient('localHost', 27017)
db = cliente.Practica
collection_usuarios = db['Usuarios']
collection_productos = db['Productos']

# Menu de login del usuario
@app.route('/')
def Login():
    print usuario_log
    return render_template('login.html')


# Menu para anadir a una persona
@app.route('/add', methods=['POST'])
def registro():
    return render_template('registro.html')


# Anade a una persona
@app.route('/adduser', methods=['POST'])
def adduser():
    # Recibe JSON
    usuario_recibido = request.form.to_dict()

    # Variable para saber el numero de resultados dentro de mongo
    num_results = collection_usuarios.find().count()

    # Convierte la contrasena a hash
    usuario_modificado = hashpass(usuario_recibido)

    # Transformamos el diccionario a JSON
    datos = json.dumps(usuario_modificado)

    # "existe_usuario" para saber si el usuario existe y "i" para saber que estamos en la ultima consulta de mongo
    existe_usuario = False
    i = 1

    if num_results == 0:
        collection_usuarios.insert_one(json.loads(datos))

    # Recorremos los registros de mongo, si el usuario no existe y el valor del email no es "", insertara el usuario
    for x in collection_usuarios.find():
        if x.get("Email") != usuario_modificado.get("Email") and usuario_modificado.get("Email") != "" and i == num_results and not existe_usuario:
            collection_usuarios.insert_one(json.loads(datos))

        elif x.get("Email") == usuario_modificado.get("Email"):
            existe_usuario = True
            print("El usuario ya existe, prueba con otro usuario")

        i += 1

    return redirect('/', code=302)


# Convierte la contrasena a hash
def hashpass(usuario_recibido):
    # Hash recibe la password, luego genera el hash de la contrasena y la guarda en modificado junto al email
    hash = usuario_recibido.get("Password")
    hash = generate_password_hash(hash)
    modificado = {"Email" : usuario_recibido.get("Email"), "Password" : hash.decode('utf-8')}

    return modificado


# Recibe la informacion del login
@app.route('/info_log', methods=['POST'])
def info_log():
    # Cogemos la variable global usuario_log
    global usuario_log

    # Recibimos el json
    usuario_log = request.form.to_dict()

    # Comprueba que el usuario existra en mongo
    comprobarUsuario(usuario_log)

    return redirect('/table', code=302)


# Comprueba si el usuario y la contrasena son correctos
def comprobarUsuario(usuario_log):
    global logueado

    # Recorre la collection usuarios, si coinciden el email y la password, dejara acceder a todos los sitios
    for usuario in collection_usuarios.find():
        if usuario.get("Email") == usuario_log.get("Email") and check_password_hash(usuario.get("Password"), usuario_log.get("Password")):
            logueado = True
        else:
            print("El usuario o la contrasena no coinciden")


def conectMongoDB(json_recibido):
    # Insertamos el JSON
    insertinMongo(json_recibido, collection_productos)


def insertinMongo(json_recibido, collection_productos):
    try:
        # Transformamos de tipo diccionario a JSON, luego hacemos un insert de los productos
        datos = json.dumps(json_recibido)
        collection_productos.insert_one(json.loads(datos))
    except:
        print("Error en el insert")


@app.route('/inf', methods=['POST'])
def information():
    # Recibe el JSON y se conecta a mongo
    json_recibido = request.form.to_dict()
    conectMongoDB(json_recibido)

    return redirect("/table", code=302)


@app.route('/delete')
def deleteProducto():
    return render_template('form_del.html')

@app.route('/inf_del')
def inf_del():
    collection_productos.find()
    return redirect('/table', code=302)


# Crea una tabla html con los productos que estan dentro de mongodb
@app.route('/table')
def table():
    # Si esta logueado permite el paso a la tabla, else: retorna a la pagina de registro
    if logueado:

        try:
            # Escirbe la collection en un documento
            writer(collection_productos)
        except:
            print("Problema en write")

        return render_template('p1.html', collection=collection_productos)
    else:
        return redirect('/', code=302)


# Escribe la informacion de mongo dentro de un documento de texto
@app.route('/write')
def writer(collection_productos):
    file = open('Productos.txt', 'w')
    try:
        for x in collection_productos.find():
            file.write(u"=======================================\n")
            file.write("La marca del producto es: " + x.get('Marca') + '\n')
            file.write("El modelo del producto es: " + x.get('Modelo') + '\n')
            file.write("El estado del producto es: " + x.get('Estado') + '\n')
            file.write("La cantidad del producto es: " + str(x.get('Cantidad')).decode('utf-8') + '\n')
            file.write("El activo del producto es: " + str(x.get('Activo')).decode('utf-8') + '\n')
            file.write(u"=======================================\n\n")
    except:
        print("Error")
    file.close()
    return redirect("/table", code=302)


# Formulario para anadir nuevos productos
@app.route('/form')
def formulario():
    # Si esta logueado permite el paso, else: retorna a la pagina de registro
    if logueado:
        return render_template('form.html')
    else:
        return redirect('/', code=302)


@app.route('/logout')
def logout():
    global logueado
    logueado = False
    return redirect('/', code=302)


if __name__ == '__main__':
    app.debug = True
    app.run(host='0.0.0.0', port=80)