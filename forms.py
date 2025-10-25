from wtforms import Form
from wtforms import StringField, PasswordField, EmailField, BooleanField, SubmitField, IntegerField
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