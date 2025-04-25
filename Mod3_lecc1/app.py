from flask import Flask, render_template, redirect, url_for, request,flash
from flask_login import LoginManager, UserMixin, login_user, login_required, logout_user, current_user
from werkzeug.security import generate_password_hash, check_password_hash
from flask_wtf import FlaskForm
from wtforms.validators import DataRequired,Length
from wtforms import StringField, SubmitField,PasswordField
app = Flask(__name__)
app.secret_key = 'clave_secreta'

login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view ='login'

#base de datos 

usuarios = {
'Editor':{'Nombre':'Raul','password':generate_password_hash('12345'), 'Rol':'Editor'},
'Admin':{'Nombre':'Pedro','password':generate_password_hash('54321'), 'Rol':'Admin'},

}

class loginForm(FlaskForm):
    username = StringField('Usuario', validators=[DataRequired(),Length(min=3,max=10)])
    password = PasswordField('Contraseña',validators=[DataRequired(),Length(min=5)])
    enviar = SubmitField('Iniciar Sesión')



#clase usuario

class Usuario(UserMixin):
    def __init__(self,username,rol):
        self.id = username
        self.rol = rol
        

@login_manager.user_loader
def load_user(user_id):
    if user_id in usuarios:
        return Usuario(user_id, usuarios[user_id]['Rol'])
    return None




@app.route('/')
@login_required
def home():
    D_usuario= usuarios.get(current_user.id)
    N_usuario= D_usuario['Nombre'] if D_usuario else current_user.id
    rol_usuario= D_usuario['Rol'] if D_usuario else 'No tiene acceso'

    return render_template('home.html.jinja2',nombre = N_usuario, rol=rol_usuario)

@app.route('/login',methods=['GET','POST'])
def login():
    form = loginForm()

    if request.method == 'POST':
        username = form.username.data
        password = form.password.data

        user = usuarios.get(username)

        if user and check_password_hash(user['password'],password):
            login_user(Usuario(username, user['Rol']))
            return redirect(url_for('home'))
        
        return render_template('error.html.jinja2', message='informacion inválida'),401
    return render_template('login.html.jinja2', form = form)

@app.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('login'))




if __name__ == "__main__":
    app.run(debug=True)