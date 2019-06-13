from flask import Flask
from flask import render_template

app = Flask(__name__)

autor_info = {
    "poe" : {
        "Nombre" : "Edgar Alan Poe",
        "Nacionalidad" : "US",
        "Fecha_de_nacimiento" : "Enero 19, 1809",
    },
    "borges" : {
        "Nombre" : "Jorge Luis Borges",
        "Nacionalidad" : "Argentina",
        "Fecha_de_nacimiento" : "Agosto 24, 1899",
    }
}

@app.route('/')
def hola():
    library_name = "Poe"
    return render_template('autor.html', library_name=library_name)

@app.route('/autor/<autor_nombre>')
def welcome(autor_nombre):
    if autor_nombre == "poe":
        return render_template('autor2.html', autor = autor_info[autor_nombre])
    else:
        return render_template('autor3.html', autor=autor_info[autor_nombre])


if __name__ == '__main__':
    app.debug = True
    app.run()

