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


@app.route('/users', methods=['POST'])
def criar_usuario():
    novo_usuario = request.json
    id = max(usuario['id'] for usuario in usuarios) + 1
    novo_usuario['id'] = id
    usuarios.append(novo_usuario)
    return jsonify({'mensagem': 'Usuario cadastrado com sucesso'}), 201


@app.route('/users/<int:id>', methods=['PUT'])
def atualizar_usuario(id):
    atualizar_usuario = request.json
    for pos, usuario in enumerate(usuarios):
        if usuario['id'] == id:
            atualizar_usuario['id'] = id
            usuarios[pos] = atualizar_usuario
            return jsonify({'mensagem': atualizar_usuario}), 200
    return jsonify({'mensagem': 'Usuario nao encontrado'}), 404


@app.route('/users/<int:id>', methods=['DELETE'])
def deletar_usuario(id):
    for pos, usuario in enumerate(usuarios):
        if usuario['id'] == id:
            usuarios.pop(pos)
            return jsonify({'mensagem': 'Usuario deletado com sucesso'}), 200
    return jsonify({'mensagem': 'Usuario nao encontrado'}), 404


if __name__ == '__main__':
    app.run(host='localhost', port= 5000, debug= True)