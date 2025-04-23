from flask import Flask, render_template

app = Flask(__name__)

empleados = [
    {'nombre': 'Pedro Sanchez', 'email': 'Pedro123@gmailcom'},
    {'nombre': 'Karina Guzman', 'email': 'KarinaG_123@gmailcom'},
    {'nombre': 'Raul Vazquez', 'email': 'RaulVAZQZ_123@gmailcom'},
]

Horas_t = [
    {'Nombre':'Pedro Sanchez','Sueldo': 12, 'horas_Trabajadas': 45},
    {'Nombre':'Karina Guzma','Sueldo': 20, 'horas_Trabajadas': 50},
    {'Nombre':'Raul Vazquez','Sueldo': 30, 'horas_Trabajadas': 33},
]

@app.route('/')
def home():
    return render_template('home.html', empleados=empleados, Horas_t=Horas_t)

@app.route('/empleados')
def empleados_page():
    return render_template('empleados.html', empleados=empleados)

@app.route('/horas')
def horas_page():
    return render_template('horas.html', Horas_t=Horas_t)

if __name__ == '__main__':
    app.run(debug=True)
