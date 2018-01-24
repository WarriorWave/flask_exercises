"""
this file contains the dataforms class that contains the base to process
forms in python by de easy way.
"""

# import forms and fields
from wtforms import Form
from wtforms import StringField, PasswordField
from wtforms import validators


# tjis class can accept Forms as parameters and process post methods
class LoginForm(Form):
    username = StringField('usuario',
                           [
                             validators.length(min=4, max=15, message='el número de carácteres debe ser entre 4 y 15'),
                             validators.DataRequired(message='Llene este campo')
                            ])
    password = PasswordField('Contraseña',
                             [
                                validators.length(min=8, max=30, message='solo se admiten de 8 a 30 carácteres'),
                                validators.DataRequired(message='Llene este campo')
                             ])
