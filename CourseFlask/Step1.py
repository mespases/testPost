from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello_world():
    return "Welcome to out Library!"



if __name__ == '__main__':
    app.debug = True
    app.run()