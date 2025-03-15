from flask import Flask, request, jsonify
from natural_numbers import NaturalNumbers

app = Flask(__name__)
nat_numbers = NaturalNumbers()

@app.route("/")
def home():
    # Mensaje de bienvenida
    return jsonify({"message": "Bienvenido a la API de numeros naturales"})

@app.route("/lost", methods=["GET"])
def lost():
    # Obtener los números faltantes
    lost_number = nat_numbers.lost()
    return jsonify({"lost_number": lost_number})

@app.route("/extract", methods=["POST"])
def extract():
    # Extraer un número de la lista
    data = request.json
    number = data.get("number")
    
    # Validar que el número sea un entero entre 1 y 100
    if not isinstance(number, int) or not (1 <= number <= 100):
        return jsonify({"error": "Numero invalido"}), 400
    
    # Extraer el número
    resp = nat_numbers.extract(number)
    # Si el número no está en la lista devolver un error
    if resp==-1:
        return jsonify({"message": "El numero ya no esta en la lista"}), 400
    # Devolver el número extraido
    return jsonify({"message": f"El numero extraido fue: {number}"})


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)