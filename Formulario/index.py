#from crypt import methods
from flask import Flask, render_template, request

app = Flask(__name__)

# Inicio


@app.route('/')
def home():
    return render_template("home.html")


@app.route('/home')
def home2():
    return render_template("home.html")

# Formulario 1


@app.route('/formulario1', methods=['GET', 'POST'])
def formulario():
    if request.method == 'POST':
        return f"nombre={request.form('nombre')} | email={request.form('correo')} | telefono={request.form('telefono')}"
    return render_template("form01.html")


if __name__ == '__main__':
    app.run(debug=True)
