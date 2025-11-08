from wtforms import Form
from wtforms import StringField, PasswordField, EmailField, BooleanField, SubmitField, IntegerField
from wtforms import SelectField
from wtforms import validators 

class UserForm(Form):
    matricula=IntegerField("Matricula",[
        validators.DataRequired(message='El campo es requerido')
    ])
    nombre=StringField("Nombre",[
        validators.DataRequired(message='El dato es requerido')])
    apellido=StringField("Apellido",[
        validators.DataRequired(message='El dato es requerido')])
    correo=StringField("Correo",[
        validators.Email(message='ingrese correo valido')])
    
class PizzaForm(Form):
    nombre_cliente=StringField("Nombre Completo",[
        validators.DataRequired(message='El nombre es requerido')])
    direccion=StringField("Dirección",[
        validators.DataRequired(message='La dirección es requerida')])
    telefono=StringField("Teléfono",[
        validators.DataRequired(message='El teléfono es requerido')])
    fecha=StringField("Fecha (dd-mm-aaaa)",[
        validators.DataRequired(message='La fecha es requerida')])
    
    tamano=SelectField("Tamaño",[
        validators.DataRequired(message='Seleccione un tamaño')],
        choices=[('','Seleccione'),('Chica','Chica - $50'),('Mediana','Mediana - $80'),('Grande','Grande - $120')])
    
    ingredientes=StringField("Ingredientes",[
        validators.DataRequired(message='Los ingredientes son requeridos')])
    
    numero_pizzas=IntegerField("Número de Pizzas",[
        validators.DataRequired(message='El número es requerido')])