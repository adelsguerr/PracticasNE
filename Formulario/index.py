
"""Módulos"""
from flask import Flask, render_template, request

app = Flask(__name__)

# Inicio


@app.route('/')
def home():
    """Devuelve Inicio"""
    return render_template("home.html")


@app.route('/home')
def home2():
    """Devuelve Inicio"""
    return render_template("home.html")

# Formulario 1


@app.route('/formulario1', methods=['GET', 'POST'])
def formulario():
    """Obtiene los datos del formulario"""

    if request.method == 'POST':
        return f"nombre = {request.form.get('nombre')} | email = {request.form.get('correo')} | telefono = {request.form.get('telefono')}"
    return render_template("form01.html")
    # if request.method == 'GET':
    #     return render_template("form01.html")
    # elif request.method == 'POST':
    #     data = request.form.to_dict()
    #     print(data)
    #     return f"nombre = {request.form.get('nombre')}, email = {request.form.get('correo')}, telefono = {request.form.get('telefono')}"
    # else:
    #     return "Formulario no recibido"


if __name__ == '__main__':
    app.run(debug=True)
