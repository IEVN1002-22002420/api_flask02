from wtforms.validators import email
from flask import Flask, render_template,request 
import math
import forms

app = Flask(__name__)
@app.route('/')
def home():
    return "Helllo, world"

@app.route('/index')
def index():
    titulo = "Pagina de inicio"
    listado = ['Python','Flask','jinja2','HTML','CSS']
    return render_template('index.html',titulo=titulo, listado=listado)

@app.route('/calculos', methods=['GET','POST'])
def about():
    if request.method == 'POST':
        numero1 = request.form['numero1']
        numero2 = request.form['numero2']
        opcin = request.form['opcion']
        if opcin == 'suma':
            res = int(numero1) + int(numero2)
        if opcin == 'resta':
            res = int(numero1) - int(numero2)
        if opcin == 'multiplicacion':
            res = int(numero1) * int(numero2)
        if opcin == 'division':
            res = int(numero1) / int(numero2)
        return render_template('calculos.html', res=res, numero1=numero1, numero2=numero2)
    return render_template('calculos.html')



@app.route('/distancia', methods=['GET', 'POST'])
def distancia():
    if request.method == 'POST':
        
        x1 = float(request.form['x1'])
        y1 = float(request.form['y1'])
        x2 = float(request.form['x2'])
        y2 = float(request.form['y2'])
        
        operacion = math.sqrt((x2 - x1)**2 + (y2 - y1)**2)
        mostrar = round(operacion, 3)
        return render_template('distancia.html', distancia=mostrar,
                               x1=x1, y1=y1, x2=x2, y2=y2)
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

@app.route("/Alumnos",methods=['GET','POST'])
def alumnos():
    mat=0
    nom=""
    ape=""
    email=""
    alumno_clas=forms.UserForm(request.form)
    if request.method == 'POST' and alumno_clas.validate():
        mat=alumno_clas.matricula.data
        nom=alumno_clas.nombre.data
        ape=alumno_clas.apellido.data
        email=alumno_clas.correo.data
    
    return render_template('Alumnos.html',form=alumno_clas, mat=mat,nom=nom,ape=ape,email=email)


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