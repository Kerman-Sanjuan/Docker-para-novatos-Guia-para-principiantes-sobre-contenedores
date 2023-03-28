from flask import Flask, abort, jsonify, request

app = Flask(__name__)

# Crear una lista de objetos Bluetabers
bluetabers = [
    {
        "id": 1,
        "name": "Bluetaber_1",
        "puesto": "Technician"
    },
    {
        "id": 2,
        "name": "Bluetaber_2",
        "puesto": "Project Manager"
    },
    {
        "id": 3,
        "name": "Bluetaber_3",
        "puesto": "Technical Architect"
    }
]

# Crear una ruta para obtener todos los objetos Bluetaber


@app.route('/bluetabers', methods=['GET'])
def get_bluetabers():
    """ Obtener todos los bluetabers"""
    return jsonify({'bluetabers': bluetabers})

# Crear una ruta para obtener un objeto Bluetaber por ID


@app.route('/bluetabers/<int:bluetaber_id>', methods=['GET'])
def get_bluetaber(bluetaber_id):
    """ Obtener los bluetabers con el id asignado"""
    bluetaber = [
        bluetaber for bluetaber in bluetabers if bluetaber['id'] == bluetaber_id]
    if len(bluetaber) == 0:
        print("Error 404, nothing found")
    return jsonify({'bluetaber': bluetaber[0]})


# Ejecutar la aplicación
if __name__ == '__main__':
    app.run(debug=True)
