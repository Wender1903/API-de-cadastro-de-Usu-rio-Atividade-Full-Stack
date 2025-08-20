from dados import usuarios
from flask import Flask, jsonify, request

app = Flask(__name__)

@app.route('/users', methods=['GET'])
def listar_usuarios():
    return jsonify(usuarios), 200

@app.route('/users/<int:id>', methods=['GET'])
def listar_usuario_por_id(id):
    for usuario in usuarios:
        if usuario['id'] == id:
            return jsonify(usuario), 200
    return jsonify({'mensagem': 'Usuario nao encontrado'}), 404


if __name__ == '__main__':
    app.run(host='localhost', port= 5000, debug= True)