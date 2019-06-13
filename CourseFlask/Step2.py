from flask import Flask

app = Flask(__name__)

@app.route('/')
def Hola():
    html = """
    <html>
        <head>
            <title>Hola mundo</title>
        </head>
        <body>
            <h1>Welcome to our Library!</h1>
        </body>
    </heml>"""

    autores = ["Alan Poe", "Jorge L. Borges", "Mark Twain"]

    return html

@app.route('/autores')
def autores():
    html = """
    <html>
        <head>
            <title>Hola mundo</title>
        </head>
        <body>
            <h1>Welcome to our Library!</h1>
            <ul>
                <li>Edgar A. Poe</li>
                <li>Jorge L. Borges</li>
                <li>Mark Twain</li>
            </ul>
        </body>
    </heml>"""

    autores = ["Alan Poe", "Jorge L. Borges", "Mark Twain"]

    return html

@app.route('/autores2')
def autores2():
    autores = ["Alan A. Poe", "Jorge L. Borges", "Mark Twain"]

    autores_list = "<ul>"
    autores_list += "\n".join(["<li>{}</li>".format(i) for i in autores])
    autores_list += "</ul>"
    print (autores_list)

    html = """
    <html>
        <head>
            <title>Hola mundo</title>
        </head>
        <body>
            <h1>Welcome to our Library!</h1>
            {}
        </body>
    </heml>""".format(autores_list)

    return html


if __name__ == '__main__':
    app.debug = True
    app.run()