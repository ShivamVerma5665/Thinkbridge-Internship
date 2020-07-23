from flask_wtf import Form
from wtforms import SubmitField, RadioField,SelectField, FloatField
from wtforms import validators, ValidationError

class CurrencyForm(Form):
    curInput = FloatField("Enter your currency", [validators.InputRequired("Please enter an integer")])

    lang = SelectField('Languages', choices=[('english','English'), ('hindi', 'Hindi'), ('marathi', "Marathi")])

    submit = SubmitField("Confirm")