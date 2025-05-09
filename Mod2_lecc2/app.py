from flask import Flask, render_template, request
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired, Length,Email

app = Flask(__name__)
app.config["SECRET_KEY"] = "mi_clave_secreta"

class RegistroForm(FlaskForm):
    username = StringField ('Nombre de usuario',validators=[DataRequired(message="obligatorio"),Length(min=3)])
    password = PasswordField('Contraseña',validators=[DataRequired("obligatorio"),Length(min=6)])
    correo = StringField ('Correo',validators=[DataRequired(message="obligatorio"),Email(message="invalido")])
    enviar = SubmitField("Registrarse")

@app.route('/registro', methods=["GET","POST"])

def registro():
    form = RegistroForm()
    mensaje= ""
    if form.validate_on_submit():
        mensaje = f"Usuario: {form.username.data} creado con exito"
    return render_template("registro.html.jinja",form = form, mensaje = mensaje)


if __name__ == "__main__":
    app.run(debug=True)