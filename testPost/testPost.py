from flask import Flask, request, render_template
from flask_login import login_user, LoginManager, login_required, logout_user
from werkzeug.utils import redirect
from werkzeug.security import generate_password_hash, check_password_hash
from pymongo import MongoClient
from regform import RegForm
from testUsers import User
import json

app = Flask(__name__)
app.secret_key = '123456'
login_manager = LoginManager()
login_manager.init_app(app)

usuario = User()


@app.route('/register', methods=['GET', 'POST'])
def register():
    global usuario
    form = RegForm(request.form)
    if form.validate():
        if not existenciaUsuario(form):
            hash_pass = generate_password_hash(form.password.data)
            usuario = User(form.email.data, hash_pass)
            login_user(usuario)
            return redirect('/table', code=302)
        else:
            print "El usuario ya existe"
    else:
        print form.validate()

    return render_template('register.html', form=form)


@app.route('/', methods=['GET', 'POST'])
def login():
    global usuario
    form = RegForm(request.form)
    try:
        if form.validate():
            if comprobarEmail(form.email.data, form.password.data):
                try:
                    u = User()
                    login_user(u)
                except:
                    print "Login user incorrect"
                return redirect('/table', code=302)
            else:
                print "No encuentro el usuario"
    except:
        pass

    return render_template('login.html', form=form)


@login_manager.user_loader
def load_user(user):
    # return User.objects(pk=user).first()  "No entiendo como funciona, porque no hay instancia de la class asi que no se como la pueden usar en los ejemplos"
    global usuario
    return usuario


@app.route('/table')
@login_required
def table():
    cliente = MongoClient('localHost', 27017)
    db = cliente.Practica
    collection_productos = db['Productos']
    return render_template('p1.html', collection=collection_productos)


@app.route('/form')
@login_required
def formulario():
    return render_template('form.html')


@app.route('/inf', methods=['POST'])
@login_required
def information():
    json_recibido = request.form.to_dict()
    insertinMongo(json_recibido)

    return redirect("/table", code=302)


def insertinMongo(json_recibido):
    try:
        cliente = MongoClient('localHost', 27017)
        db = cliente.Practica
        collection_productos = db['Productos']

        datos = json.dumps(json_recibido)
        collection_productos.insert_one(json.loads(datos))
    except:
        print("Error en el insert")


@app.route('/logout')
def logout():
    logout_user()
    return redirect('/')


def comprobarEmail(email, password):
    global usuario
    i = 0

    for x in usuario.email:
        if x == email and check_password_hash(usuario.password[i], password):
            return True
        i += 1
    return False


def existenciaUsuario(form):
    num_results = usuario.collection_usuarios.find().count()
    if num_results == 0:
        return False

    existe_usuario = False
    i = 1

    for x in usuario.email:
        if x != form.email.data and i == num_results and not existe_usuario:
            existe_usuario = False
        elif x == form.email.data:
            existe_usuario = True
        i += 1

    return existe_usuario


if __name__ == '__main__':
    app.debug = True
    app.run(host='0.0.0.0', port=80)