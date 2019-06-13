from flask import Flask
from flask import render_template

app = Flask(__name__)

@app.route('/')
def hola():
    library_name = "Poe"
    return render_template('index.html', library_name=library_name)


if __name__ == '__main__':
    app.debug = True
    app.run()