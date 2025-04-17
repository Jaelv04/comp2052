from flask import Flask, jsonify, request

app = Flask(__name__)

@app.route('/info',methods=["GET"])
def informacion():
        return jsonify({"Cursos actuales": ["COMP2025","COMP2400","COMP2800","MATH1512"]})

@app.route('/crear_usuario',methods=["POST"])
def crear():
      data=request.json
      nombre=data.get("nombre")
      correo = data.get("correo")
      if not nombre or not correo:
            return jsonify({'hubo un error':'Faltan los datos "nombre y/o "correo"'})
      return jsonify({
            "Accion completada":"El usuario fue creado con exito",
            "usuario":{
                  "nombre":nombre,
                  "correo":correo
            }



      }),201
      

@app.route('/usuarios',methods=["GET"])
def usuarios():
      return jsonify({"Usuarios":["Jorge","Raul","Pedro","Carla","Juan"]})

if __name__== "__main__":
    app.run(debug=True)