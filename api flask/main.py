from flask import Flask, jsonify, request
from data import data

app =  Flask(__name__)

@app.route("/")
def index():
    return jsonify({
        "data": data,
        "message": "success"
    }),200
    # é usada para obter o nome da URL. Aqui, estamos primeiro buscando o nome
    #do planeta a partir do argumento URL.
    #http://127.0.0.1:5000/planet?name=
@app.route("/planet")
def planet():
    
    name = request.args.get("name")
    planet_data = next(item for item in data if item["name"] == name)
    return jsonify({
        "data": planet_data,
        "message": "success"
    }), 200

if __name__ == "__main__":
    app.run()