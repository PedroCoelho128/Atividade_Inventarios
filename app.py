from flask import Flask, request, jsonify
from pymongo import MongoClient
from bson.objectid import ObjectId
from werkzeug.urls import quote

app = Flask(__name__)
client = MongoClient('mongodb://localhost:27017/')
db = client['Inventario']
colecao = db['funcionario']

# Rota para inserir um novo funcionário
@app.route('/funcionario', methods=['POST'])
def inserir_funcionario():
    data = request.json
    if not data.get('cpf'):
        return jsonify({'error': 'CPF é obrigatório'}), 400
    funcionario_id = colecao.insert_one(data).inserted_id
    return jsonify(str(funcionario_id)), 201

# Rota para excluir um funcionário
@app.route('/funcionario/<cpf>', methods=['DELETE'])
def excluir_funcionario(cpf):
    if db.notebook.find_one({'cpf': cpf}) or \
       db.monitor.find_one({'cpf': cpf}) or \
       db.monitor2.find_one({'cpf': cpf}) or \
       db.teclado.find_one({'cpf': cpf}) or \
       db.mouse.find_one({'cpf': cpf}) or \
       db.desktop.find_one({'cpf': cpf}) or \
       db.acessorios.find_one({'cpf': cpf}) or \
       db.nobreak.find_one({'cpf': cpf}) or \
       db.headset.find_one({'cpf': cpf}) or \
       db.celular.find_one({'cpf': cpf}):
        return jsonify({'error': 'Funcionário possui ativos, não pode ser excluído'}), 400

    result = colecao.delete_one({'cpf': cpf})
    if result.deleted_count == 0:
        return jsonify({'error': 'Funcionário não encontrado'}), 404

    db.notebook.delete_many({'cpf': cpf})
    db.monitor.delete_many({'cpf': cpf})
    db.monitor2.delete_many({'cpf': cpf})
    db.teclado.delete_many({'cpf': cpf})
    db.mouse.delete_many({'cpf': cpf})
    db.desktop.delete_many({'cpf': cpf})
    db.acessorios.delete_many({'cpf': cpf})
    db.nobreak.delete_many({'cpf': cpf})
    db.headset.delete_many({'cpf': cpf})
    db.celular.delete_many({'cpf': cpf})

    return '', 204

# Rota para listar todos os funcionários
@app.route('/funcionarios', methods=['GET'])
def listar_funcionarios():
    funcionarios = list(colecao.find({}, {'_id': 0, 'nome': 1, 'cpf': 1}))
    return jsonify(funcionarios)

# Rota para consultar o inventário completo de um funcionário pelo CPF
@app.route('/inventario/<cpf>', methods=['GET'])
def consultar_inventario(cpf):
    inventario = []
    inventario.extend(list(db.notebook.find({'cpf': cpf})))
    inventario.extend(list(db.monitor.find({'cpf': cpf})))
    inventario.extend(list(db.monitor2.find({'cpf': cpf})))
    inventario.extend(list(db.teclado.find({'cpf': cpf})))
    inventario.extend(list(db.mouse.find({'cpf': cpf})))
    inventario.extend(list(db.desktop.find({'cpf': cpf})))
    inventario.extend(list(db.acessorios.find({'cpf': cpf})))
    inventario.extend(list(db.nobreak.find({'cpf': cpf})))
    inventario.extend(list(db.headset.find({'cpf': cpf})))
    inventario.extend(list(db.celular.find({'cpf': cpf})))

    for item in inventario:
        item['_id'] = str(item['_id'])

    return jsonify(inventario)

# Rota para atualizar o nome de um funcionário pelo CPF
@app.route('/funcionario/<cpf>', methods=['PUT'])
def atualizar_funcionario(cpf):
    data = request.json
    result = colecao.update_one({'cpf': cpf}, {'$set': {'nome': data.get('nome')}})
    if result.matched_count == 0:
        return jsonify({'error': 'Funcionário não encontrado'}), 404
    return '', 204

# Rotas para atualizar informações de ativos específicos

@app.route('/ativo/notebook/<ativo_id>', methods=['PUT'])
def atualizar_notebook(ativo_id):
    data = request.json
    result = db.notebook.update_one({'_id': ObjectId(ativo_id)}, {'$set': data})
    if result.matched_count == 0:
        return jsonify({'error': 'Ativo não encontrado'}), 404
    return '', 204

@app.route('/ativo/monitor/<ativo_id>', methods=['PUT'])
def atualizar_monitor(ativo_id):
    data = request.json
    result = db.monitor.update_one({'_id': ObjectId(ativo_id)}, {'$set': data})
    if result.matched_count == 0:
        return jsonify({'error': 'Ativo não encontrado'}), 404
    return '', 204

@app.route('/ativo/teclado/<ativo_id>', methods=['PUT'])
def atualizar_teclado(ativo_id):
    data = request.json
    result = db.teclado.update_one({'_id': ObjectId(ativo_id)}, {'$set': data})
    if result.matched_count == 0:
        return jsonify({'error': 'Ativo não encontrado'}), 404
    return '', 204

@app.route('/ativo/mouse/<ativo_id>', methods=['PUT'])
def atualizar_mouse(ativo_id):
    data = request.json
    result = db.mouse.update_one({'_id': ObjectId(ativo_id)}, {'$set': data})
    if result.matched_count == 0:
        return jsonify({'error': 'Ativo não encontrado'}), 404
    return '', 204

@app.route('/ativo/desktop/<ativo_id>', methods=['PUT'])
def atualizar_desktop(ativo_id):
    data = request.json
    result = db.desktop.update_one({'_id': ObjectId(ativo_id)}, {'$set': data})
    if result.matched_count == 0:
        return jsonify({'error': 'Ativo não encontrado'}), 404
    return '', 204

@app.route('/ativo/acessorios/<ativo_id>', methods=['PUT'])
def atualizar_acessorios(ativo_id):
    data = request.json
    result = db.acessorios.update_one({'_id': ObjectId(ativo_id)}, {'$set': data})
    if result.matched_count == 0:
        return jsonify({'error': 'Ativo não encontrado'}), 404
    return '', 204

@app.route('/ativo/nobreak/<ativo_id>', methods=['PUT'])
def atualizar_nobreak(ativo_id):
    data = request.json
    result = db.nobreak.update_one({'_id': ObjectId(ativo_id)}, {'$set': data})
    if result.matched_count == 0:
        return jsonify({'error': 'Ativo não encontrado'}), 404
    return '', 204

@app.route('/ativo/headset/<ativo_id>', methods=['PUT'])
def atualizar_headset(ativo_id):
    data = request.json
    result = db.headset.update_one({'_id': ObjectId(ativo_id)}, {'$set': data})
    if result.matched_count == 0:
        return jsonify({'error': 'Ativo não encontrado'}), 404
    return '', 204

@app.route('/ativo/celular/<ativo_id>', methods=['PUT'])
def atualizar_celular(ativo_id):
    data = request.json
    result = db.celular.update_one({'_id': ObjectId(ativo_id)}, {'$set': data})
    if result.matched_count == 0:
        return jsonify({'error': 'Ativo não encontrado'}), 404
    return '', 204

# Rotas para excluir informações de ativos específicos

@app.route('/ativo/notebook/<ativo_id>', methods=['DELETE'])
def limpar_notebook(ativo_id):
    result = db.notebook.delete_one({'_id': ObjectId(ativo_id)})
    if result.deleted_count == 0:
        return jsonify({'error': 'Ativo não encontrado'}), 404
    return '', 204

@app.route('/ativo/monitor/<ativo_id>', methods=['DELETE'])
def limpar_monitor(ativo_id):
    result = db.monitor.delete_one({'_id': ObjectId(ativo_id)})
    if result.deleted_count == 0:
        return jsonify({'error': 'Ativo não encontrado'}), 404
    return '', 204

@app.route('/ativo/teclado/<ativo_id>', methods=['DELETE'])
def limpar_teclado(ativo_id):
    result = db.teclado.delete_one({'_id': ObjectId(ativo_id)})
    if result.deleted_count == 0:
        return jsonify({'error': 'Ativo não encontrado'}), 404
    return '', 204

@app.route('/ativo/mouse/<ativo_id>', methods=['DELETE'])
def limpar_mouse(ativo_id):
    result = db.mouse.delete_one({'_id': ObjectId(ativo_id)})
    if result.deleted_count == 0:
        return jsonify({'error': 'Ativo não encontrado'}), 404
    return '', 204

@app.route('/ativo/desktop/<ativo_id>', methods=['DELETE'])
def limpar_desktop(ativo_id):
    result = db.desktop.delete_one({'_id': ObjectId(ativo_id)})
    if result.deleted_count == 0:
        return jsonify({'error': 'Ativo não encontrado'}), 404
    return '', 204

@app.route('/ativo/acessorios/<ativo_id>', methods=['DELETE'])
def limpar_acessorios(ativo_id):
    result = db.acessorios.delete_one({'_id': ObjectId(ativo_id)})
    if result.deleted_count == 0:
        return jsonify({'error': 'Ativo não encontrado'}), 404
    return '', 204

@app.route('/ativo/nobreak/<ativo_id>', methods=['DELETE'])
def limpar_nobreak(ativo_id):
    result = db.nobreak.delete_one({'_id': ObjectId(ativo_id)})
    if result.deleted_count == 0:
        return jsonify({'error': 'Ativo não encontrado'}), 404
    return '', 204

@app.route('/ativo/headset/<ativo_id>', methods=['DELETE'])
def limpar_headset(ativo_id):
    result = db.headset.delete_one({'_id': ObjectId(ativo_id)})
    if result.deleted_count == 0:
        return jsonify({'error': 'Ativo não encontrado'}), 404
    return '', 204

@app.route('/ativo/celular/<ativo_id>', methods=['DELETE'])
def limpar_celular(ativo_id):
    result = db.celular.delete_one({'_id': ObjectId(ativo_id)})
    if result.deleted_count == 0:
        return jsonify({'error': 'Ativo não encontrado'}), 404
    return '', 204

if __name__ == '__main__':
    app.run(debug=True)
