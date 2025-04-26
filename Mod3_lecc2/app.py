from flask import Flask, redirect, url_for
from flask_login import LoginManager, UserMixin, login_user,logout_user,current_user,login_required
from flask_principal import Principal, Permission, RoleNeed, Identity, identity_changed, identity_loaded, AnonymousIdentity

app = Flask(__name__)
app.secret_key ="Secreto"

login_manager = LoginManager(app)
login_manager.login_view = "login"

principals = Principal(app)

roles_permisos = {
    "admin":["crear", "leer", "actualizar", "borrar"],
    "usuario":["leer"]

}

def tiene_permiso(role, persmiso):
    return persmiso in roles_permisos.get(role,[])


class Usuario(UserMixin):
    def __init__(self, id, nombreD_usuario ,roles):
        self.id = id
        self.nombreD_usuario = nombreD_usuario
        self.roles = roles

        def obtener_roles(self):
            return self.roles
        
usuarios ={
"Raul": Usuario(1, "Raul", ["admin","usuario"]),
"Pedro": Usuario( 2, "Pedro",["usuario"]),
"guest": Usuario( 3, "guest",["no tiene roles"])
}

@login_manager.user_loader
def cargar_usuario(user_id):
    for usuario in usuarios.values():
        if str(usuario.id) == user_id:
            return usuario
        return None
    
@identity_loaded.connect_via(app)
def usuario_cargado(sender,identity):
    identity.user = current_user
    if hasattr( current_user, 'obtener_roles'):
        for rol in current_user.obtener_roles():
            identity.provides.add(RoleNeed(rol))


@app.route("/login/<nombreD_usuario>")
def login(nombreD_usuario):
    usuario = usuarios.get(nombreD_usuario)
    if usuario:
        login_user(usuario)
        identity_changed.send( app, identity = Identity(usuario.id))
        return f" Bienvenido {current_user.nombreD_usuario}! sus roles son: {usuario.roles}"
    return  "No se encontró dicho usuario :( ",404

@app.route("/logout")
@login_required
def logout():
    logout_user()
    identity_changed.send( app, identity = AnonymousIdentity())
    return "Sesión cerrada"


@app.route("/dashboard")
@login_required
def dashboard():
    return f" Bienvenido a tu panel {current_user.nombreD_usuario}"


@app.route("/admin")
@login_required
def admin():
    if admin in current_user.obtener_roles() and tiene_permiso ("admin", "crear"):
        return f" Bienvenido al panel de administrador!"
    return f" No tiene acceso a este panel ",403

@app.route("/usuarioo")
@login_required
def user():
    if "usuario"in current_user.obtener_roles() and tiene_permiso ("usuario", "leer"):
        return f" Disponible solamente para usuarios ya registrados"
    return f" No tiene acceso a este panel",403

if __name__ == "__main__":
    app.run(debug=True)

