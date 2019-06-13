from urllib2 import install_opener

from flask import Flask, request, url_for, render_template
from flask_login import UserMixin, login_manager, login_user, current_user, login_required, logout_user, LoginManager
from flask_wtf import FlaskForm, Form
from werkzeug.security import generate_password_hash, check_password_hash
from werkzeug.utils import redirect
from wtforms import PasswordField, StringField
from wtforms.validators import InputRequired, Email, Length

app = Flask(__name__)
#app.config['SECRET_KEY'] = os.urandom(12).hex()

app.config['MONGODB_SETTINGS'] = {
    'db': 'Practica',
    'host': 'mongodb://localhost'
}

app.secret_key = 'xxxxyyyyyzzzzz'

login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = 'login'

class User(UserMixin):
    meta = {'collection': 'Usuraios'}
    email = "mig@mig.com"
    password = "mig"

    def __init__(self, email, password):
        self.email = email
        self.password = password

    def getEmail(self):
        return self.email

    def getPassword(self):
        return self.password

@login_manager.user_loader
def load_user(user_id):
    # Objects falla siempre, buscar una solucion
    # Error: "AttributeError: type object 'User' has no attribute 'object'"
    return User.objects(pk=user_id).first()


# Son las normas del formulario
class RegForm(FlaskForm):
    email = StringField('email', validators=[InputRequired(), Email(message='Invalid email'), Length(max=30)])
    password = PasswordField('password', validators=[InputRequired(), Length(min=1, max=20)])


@app.route('/register', methods=['GET', 'POST'])
def register():
    form = RegForm()
    print form.email.data
    print form.password.data
    if request.method == 'POST':
        # Si los datos del formulario son validos
        if form.validate():
            # No se que hace el metodo objects ni el metodo first
            existing_user = User.objects(email=form.email.data).first()
            if existing_user is None:
                hashpass = generate_password_hash(form.password.data, method='sha256')
                hey = User(form.email.data, hashpass)
                print "Hola"
                load_user(hey)
                return redirect(url_for('dashboard'))
    return render_template('register.html', form=form)


@app.route('/login', methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated == True:
        print "Estoy dentro"
        return redirect(url_for('dashboard'))
    form = RegForm()
    if request.method == 'POST':
        if form.validate():
            print "Estoy dentro"
            return redirect('/dashboard', code=302)
    return render_template('login2.html', form=form)


@app.route('/dashboard')
@login_required
def dashboard():
    return render_template('dashboard.html', name=current_user.email)


@app.route('/logout', methods = ['GET'])
@login_required
def logout():
    logout_user()
    return redirect(url_for('login'))


if __name__ == '__main__':
    app.debug = True
    app.run()