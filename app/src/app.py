from flask import Flask
app = Flask(__name__)

from db import set_modulos, get_modulos

set_modulos()

@app.route('/')
def index():
    modulos = "<h1>Full Cycle Modulos</h1>"
    try:
        modulos += "<ol>"
        for m in get_modulos():
            modulos += f"<li>{m[0]}</li>"
        modulos += "</ol>"
    except Exception as error:
        print(error)
    return modulos
