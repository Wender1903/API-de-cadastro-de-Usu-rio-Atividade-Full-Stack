from dados import usuarios
from flask import Flask, jsonify, request

app = Flask(__name__)

@app.route('/users', methods=['GET'])
def listar_usuarios():
    return jsonify(usuarios)

if __name__ == '__main__':
    app.run(host='localhost', port= 5000, debug= True)