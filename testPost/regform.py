from wtforms import Form, StringField, PasswordField
from wtforms.validators import InputRequired, Email, Length

class RegForm(Form):
    email = StringField('email', validators=[InputRequired(), Email(message='Invalid email'), Length(max=30)])
    password = PasswordField('password', validators=[InputRequired(), Length(min=1, max=20)])