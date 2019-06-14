from wtforms import Form, StringField, PasswordField, SelectField
from wtforms.validators import InputRequired, Email, Length

class RegForm(Form):
    """ RegForm son las reglas que va a seguir el formulario creado en html"""

    email = StringField('email', validators=[InputRequired(), Email(message='Invalid email'), Length(max=30)])
    password = PasswordField('password', validators=[InputRequired(), Length(min=1, max=20)])
    role = SelectField("role", choices=[("admin", "admin"), ("user", "user"), ("invited", "invited")])