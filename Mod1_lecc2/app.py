from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/inf',methods=['GET'])
def inf():
    return jsonify({
        "Mensaje": "Mi servidor flask",
        "owner": "Jorge Arce"
    })

@app.route('/Nombres',methods=['POST'])
def nombres():
    data = request.json
    nombre = data.get("nombre","Usuario")
    return f"Hola, {nombre}"

if __name__ == "__main__":
    app.run(debug=True)
