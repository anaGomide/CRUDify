from flask import Flask, jsonify, request
from flask_cors import CORS
from pymongo import MongoClient
from bson.objectid import ObjectId

app = Flask(__name__)
CORS(app)  # Permite requisições de outros domínios (importante para o front-end)

# Conecte-se ao MongoDB
client = MongoClient('mongodb://localhost:27017/')
db = client['crudify']
collection = db['users']

@app.route('/')
def index():
    return "API de Usuários - Back-end rodando!"

# Endpoint para obter todos os usuários
@app.route('/users', methods=['GET'])
def get_users():
    users = list(collection.find())
    for user in users:
        user['_id'] = str(user['_id'])
    return jsonify(users)

# Endpoint para obter um usuário individual
@app.route('/users/<id>', methods=['GET'])
def get_user(id):
    user = collection.find_one({'_id': ObjectId(id)})
    if user:
        user['_id'] = str(user['_id'])
        return jsonify(user)
    return jsonify({'error': 'Usuário não encontrado'}), 404

# Endpoint para criar um novo usuário
@app.route('/users', methods=['POST'])
def create_user():
    data = request.json
    result = collection.insert_one(data)
    return jsonify({'_id': str(result.inserted_id)}), 201

# Endpoint para atualizar um usuário existente
@app.route('/users/<id>', methods=['PUT'])
def update_user(id):
    data = request.json
    result = collection.update_one({'_id': ObjectId(id)}, {'$set': data})
    if result.modified_count:
        return jsonify({'message': 'Usuário atualizado!'})
    return jsonify({'error': 'Nenhum usuário atualizado!'}), 404

# Endpoint para deletar um usuário
@app.route('/users/<id>', methods=['DELETE'])
def delete_user(id):
    result = collection.delete_one({'_id': ObjectId(id)})
    if result.deleted_count:
        return jsonify({'message': 'Usuário deletado!'})
    return jsonify({'error': 'Usuário não encontrado'}), 404

if __name__ == '__main__':
    app.run(debug=True)
