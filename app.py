# app.py
from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hola mundo, prueba con Docker'

if __name__ == '__main__':
    app.run(debug=True)
