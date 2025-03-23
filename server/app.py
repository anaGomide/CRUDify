from flask import Flask, jsonify, request
from flask_cors import CORS
from pymongo import MongoClient
from bson.objectid import ObjectId
from datetime import datetime

app = Flask(__name__)
CORS(app)

client = MongoClient('mongodb://localhost:27017/')
db = client['crudify']
collection = db['users']

@app.route('/')
def index():
    return "API is running!"

@app.route('/users/list', methods=['GET'])
def list_users():
    users = list(collection.find())
    for user in users:
        user['_id'] = str(user['_id'])
    return jsonify(users)

@app.route('/users/view/<id>', methods=['GET'])
def view_user(id):
    user = collection.find_one({'_id': ObjectId(id)})
    if user:
        user['_id'] = str(user['_id'])
        return jsonify(user)
    return jsonify({'error': 'User not found'}), 404

@app.route('/users/create', methods=['POST'])
def create_user():
    data = request.json
    data['created_ts'] = datetime.utcnow().timestamp()
    result = collection.insert_one(data)
    return jsonify({'_id': str(result.inserted_id)}), 201

@app.route('/users/update/<id>', methods=['PUT'])
def update_user(id):
    data = request.json
    data['updated_ts'] = datetime.utcnow().timestamp()
    result = collection.update_one({'_id': ObjectId(id)}, {'$set': data})
    if result.modified_count:
        return jsonify({'message': 'User updated!'})
    return jsonify({'error': 'No user updated!'}), 404

@app.route('/users/delete/<id>', methods=['DELETE'])
def delete_user(id):
    result = collection.delete_one({'_id': ObjectId(id)})
    if result.deleted_count:
        return jsonify({'message': 'User deleted!'})
    return jsonify({'error': 'User not found'}), 404

if __name__ == '__main__':
    app.run(debug=True)
