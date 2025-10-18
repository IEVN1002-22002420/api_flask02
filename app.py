from flask import Flask
app = Flask(__name__)
@app.route('/')
def home():
    return "Helllo, world"

@app.route('/hola')
def about():
    return "Hola"

@app.route('/user/<string:user>')
def user(user):
    return f"Hello, {user}!"

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



if __name__== '__main__':
    app.run(debug=True)