"""
this file contains the dataforms class that contains the base to process
forms in python by de easy way.
"""

# import forms and fields
from wtforms import Form
from wtforms import StringField, TextField
from wtforms.fields.html5 import EmailField
from wtforms import validators


# tjis class can accept Forms as parameters and process post methods
class CommentForm(Form):
    username=StringField('usuario',
                         [
                             validators.length(min=4, max=15, message='el número de carácteres debe ser entre 4 y 15')
                         ])
    email=EmailField('correo electronico')
    comment=TextField('comentario')
