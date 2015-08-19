__author__ = 'july'
from wtforms import Form, validators, IntegerField, TextAreaField


class Data(Form):
    url= TextAreaField('url', [validators.URL()])
    users_number= IntegerField ( 'users_number', [validators.InputRequired()])
