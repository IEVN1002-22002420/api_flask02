from flask import Flask, render_template
app = Flask(__name__)
@app.route('/')
def home():
    return "Helllo, world"

@app.route('/index')
def index():
    titulo = "Pagina de inicio"
    listado = ['Python','Flask','jinja2','HTML','CSS']
    return render_template('index.html',titulo=titulo, listado=listado)

@app.route('/calculos')
def about():
    return render_template('calculos.html')

@app.route('/distancia')
def distancia():
    return render_template('distancia.html')

@app.route("/numero/<int:num>")
def funct(num):
    return f"El numero es :{num}"

@app.route("/suma/<int:num1>/<int:num2>")
def suma(num1, num2):
    return f"la suma es: {num1 + num2}"

@app.route("/user/<int:id>/<string:username>")
def username(id,username):
    return "ID: {} nombre: {}".format(id,username)

@app.route("/suma/<int:n1>/<float:n2>")
def func1(n1,n2):
    return "la suma es: {}".format(n1+n2)

@app.route("/default/")
@app.route("/default/<string:dft>")
def func2(dft="sss"):
    return "el valor de dft es:"+dft

@app.route("/prueba")
def func4():
    return'''<html>
<head>
<title>Pagina de prueba</title>
</head>
<body>
<h1>Hola esta es una pagina</h1>
<p>soy una prueba</p>
</body>
'''


if __name__== '__main__':
    app.run(debug=True)