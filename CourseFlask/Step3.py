from flask import Flask
from flask import render_template_string

app = Flask(__name__)

@app.route('/')
def Hola():
    library_name = "Poe"
    html = """
    <html>
        <h1>Welcome to {{library}} library!</h1>
        <ul>
            {% for autor in autores %}
                <li>{{ autor }}</li>
            {% endfor %}
        </ul>
    </heml>
    """

    autores = ["Alan Poe", "Jorge L. Borges", "Mark Twain"]
    rendered_hmlt = render_template_string(html, library=library_name, autores = autores)

    return rendered_hmlt


if __name__ == '__main__':
    app.debug = True
    app.run()