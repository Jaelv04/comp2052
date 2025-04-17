from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/platillos')
def platillos():
    lista_platillos = [
        {'Nombre': 'Mofongo', 'Precio': 12.99},
        {'Nombre': 'Arepas', 'Precio': 8.75},
        {'Nombre': 'Tacos', 'Precio': 6.99}
    ]    
    return render_template('platillos.html', platillos=lista_platillos)

@app.route('/Origen')
def Origen():
    Origen_platos = ['Puerto Rico  🇵🇷', 'Colombia 🇨🇴 ', 'Mexico 🇲🇽']    
    return render_template('origen.html', Origen=Origen_platos)

if __name__ == '__main__':
    app.run(debug=True)
