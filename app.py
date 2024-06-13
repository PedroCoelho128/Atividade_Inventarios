from flask import Flask, request, jsonify
from pymongo import MongoClient
from bson.objectid import ObjectId

app = Flask(__name__)
client = MongoClient('mongodb://localhost:27017/')
db = client['Inventario']
colecao = db['funcionario']

# Rota para inserir um novo funcionário
@app.route('/funcionario', methods=['POST'])
def inserir_funcionario():
    # Insere um novo funcionário no banco de dados.
    # Espera receber um JSON com os dados do funcionário, sendo 'cpf' obrigatório.
    # Retorna o ID gerado para o novo funcionário.
    data = request.json
    if not data.get('cpf'):
        return jsonify({'error': 'CPF é obrigatório'}), 400
    funcionario_id = colecao.insert_one(data).inserted_id
    return jsonify(str(funcionario_id)), 201

# Rota para excluir um funcionário
@app.route('/funcionario/<cpf>', methods=['DELETE'])
def excluir_funcionario(cpf):
    # Exclui um funcionário do banco de dados, verificando se há ativos associados.
    # Se o funcionário possui ativos, retorna um erro 400.
    # Se o funcionário não é encontrado, retorna um erro 404.
    # Caso contrário, exclui o funcionário e seus ativos associados.
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
    
    # Remove documentos das coleções específicas de ativos associados ao funcionário.
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
    # Lista todos os funcionários cadastrados, retornando apenas nome e cpf.
    funcionarios = list(colecao.find({}, {'_id': 0, 'nome': 1, 'cpf': 1}))
    return jsonify(funcionarios)

# Rota para consultar o inventário completo de um funcionário pelo CPF
@app.route('/inventario/<cpf>', methods=['GET'])
def consultar_inventario(cpf):
    # Consulta o inventário completo de um funcionário pelo CPF.
    # Retorna uma lista de todos os ativos associados ao funcionário.
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
    # Atualiza o nome de um funcionário pelo CPF.
    # Espera receber um JSON com o novo nome do funcionário.
    # Retorna um código 204 se atualizado com sucesso ou erro 404 se o funcionário não for encontrado.
    data = request.json
    result = colecao.update_one({'cpf': cpf}, {'$set': {'nome': data.get('nome')}})
    if result.matched_count == 0:
        return jsonify({'error': 'Funcionário não encontrado'}), 404
    return '', 204

# Rotas para atualizar informações de ativos específicos

@app.route('/ativo/notebook/<ativo_id>', methods=['PUT'])
def atualizar_notebook(ativo_id):
    # Atualiza as informações de um notebook específico pelo ID.
    # Espera receber um JSON com os novos dados do notebook.
    # Retorna um código 204 se atualizado com sucesso ou erro 404 se o notebook não for encontrado.
    data = request.json
    result = db.notebook.update_one({'_id': ObjectId(ativo_id)}, {'$set': data})
    if result.matched_count == 0:
        return jsonify({'error': 'Ativo não encontrado'}), 404
    return '', 204

@app.route('/ativo/monitor/<ativo_id>', methods=['PUT'])
def atualizar_monitor(ativo_id):
    # Atualiza as informações de um monitor específico pelo ID.
    # Espera receber um JSON com os novos dados do monitor.
    # Retorna um código 204 se atualizado com sucesso ou erro 404 se o monitor não for encontrado.
    data = request.json
    result = db.monitor.update_one({'_id': ObjectId(ativo_id)}, {'$set': data})
    if result.matched_count == 0:
        return jsonify({'error': 'Ativo não encontrado'}), 404
    return '', 204

@app.route('/ativo/teclado/<ativo_id>', methods=['PUT'])
def atualizar_teclado(ativo_id):
    # Atualiza as informações de um teclado específico pelo ID.
    # Espera receber um JSON com os novos dados do teclado.
    # Retorna um código 204 se atualizado com sucesso ou erro 404 se o teclado não for encontrado.
    data = request.json
    result = db.teclado.update_one({'_id': ObjectId(ativo_id)}, {'$set': data})
    if result.matched_count == 0:
        return jsonify({'error': 'Ativo não encontrado'}), 404
    return '', 204

@app.route('/ativo/mouse/<ativo_id>', methods=['PUT'])
def atualizar_mouse(ativo_id):
    # Atualiza as informações de um mouse específico pelo ID.
    # Espera receber um JSON com os novos dados do mouse.
    # Retorna um código 204 se atualizado com sucesso ou erro 404 se o mouse não for encontrado.
    data = request.json
    result = db.mouse.update_one({'_id': ObjectId(ativo_id)}, {'$set': data})
    if result.matched_count == 0:
        return jsonify({'error': 'Ativo não encontrado'}), 404
    return '', 204

@app.route('/ativo/desktop/<ativo_id>', methods=['PUT'])
def atualizar_desktop(ativo_id):
    # Atualiza as informações de um desktop específico pelo ID.
    # Espera receber um JSON com os novos dados do desktop.
    # Retorna um código 204 se atualizado com sucesso ou erro 404 se o desktop não for encontrado.
    data = request.json
    result = db.desktop.update_one({'_id': ObjectId(ativo_id)}, {'$set': data})
    if result.matched_count == 0:
        return jsonify({'error': 'Ativo não encontrado'}), 404
    return '', 204

@app.route('/ativo/acessorios/<ativo_id>', methods=['PUT'])
def atualizar_acessorios(ativo_id):
    # Atualiza as informações de um acessório específico pelo ID.
    # Espera receber um JSON com os novos dados do acessório.
    # Retorna um código 204 se atualizado com sucesso ou erro 404 se o acessório não for encontrado.
    data = request.json
    result = db.acessorios.update_one({'_id': ObjectId(ativo_id)}, {'$set': data})
    if result.matched_count == 0:
        return jsonify({'error': 'Ativo não encontrado'}), 404
    return '', 204

@app.route('/ativo/nobreak/<ativo_id>', methods=['PUT'])
def atualizar_nobreak(ativo_id):
    # Atualiza as informações de um nobreak específico pelo ID.
    # Espera receber um JSON com os novos dados do nobreak.
    # Retorna um código 204 se atualizado com sucesso ou erro 404 se o nobreak não for encontrado.
    data = request.json
    result = db.nobreak.update_one({'_id': ObjectId(ativo_id)}, {'$set': data})
    if result.matched_count == 0:
        return jsonify({'error': 'Ativo não encontrado'}), 404
    return '', 204

@app.route('/ativo/headset/<ativo_id>', methods=['PUT'])
def atualizar_headset(ativo_id):
    # Atualiza as informações de um headset específico pelo ID.
    # Espera receber um JSON com os novos dados do headset.
    # Retorna um código 204 se atualizado com sucesso ou erro 404 se o headset não for encontrado.
    data = request.json
    result = db.headset.update_one({'_id': ObjectId(ativo_id)}, {'$set': data})
    if result.matched_count == 0:
        return jsonify({'error': 'Ativo não encontrado'}), 404
    return '', 204

@app.route('/ativo/celular/<ativo_id>', methods=['PUT'])
def atualizar_celular(ativo_id):
    # Atualiza as informações de um celular específico pelo ID.
    # Espera receber um JSON com os novos dados do celular.
    # Retorna um código 204 se atualizado com sucesso ou erro 404 se o celular não for encontrado.
    data = request.json
    result = db.celular.update_one({'_id': ObjectId(ativo_id)}, {'$set': data})
    if result.matched_count == 0:
        return jsonify({'error': 'Ativo não encontrado'}), 404
    return '', 204

# Rotas para excluir informações de ativos específicos

@app.route('/ativo/notebook/<ativo_id>', methods=['DELETE'])
def limpar_notebook(ativo_id):
    # Exclui as informações de um notebook específico pelo ID.
    # Retorna um código 204 se excluído com sucesso ou erro 404 se o notebook não for encontrado.
    result = db.notebook.delete_one({'_id': ObjectId(ativo_id)})
    if result.deleted_count == 0:
        return jsonify({'error': 'Ativo não encontrado'}), 404
    return '', 204

@app.route('/ativo/monitor/<ativo_id>', methods=['DELETE'])
def limpar_monitor(ativo_id):
    # Exclui as informações de um monitor específico pelo ID.
    # Retorna um código 204 se excluído com sucesso ou erro 404 se o monitor não for encontrado.
    result = db.monitor.delete_one({'_id': ObjectId(ativo_id)})
    if result.deleted_count == 0:
        return jsonify({'error': 'Ativo não encontrado'}), 404
    return '', 204

@app.route('/ativo/teclado/<ativo_id>', methods=['DELETE'])
def limpar_teclado(ativo_id):
    # Exclui as informações de um teclado específico pelo ID.
    # Retorna um código 204 se excluído com sucesso ou erro 404 se o teclado não for encontrado.
    result = db.teclado.delete_one({'_id': ObjectId(ativo_id)})
    if result.deleted_count == 0:
        return jsonify({'error': 'Ativo não encontrado'}), 404
    return '', 204

@app.route('/ativo/mouse/<ativo_id>', methods=['DELETE'])
def limpar_mouse(ativo_id):
    # Exclui as informações de um mouse específico pelo ID.
    # Retorna um código 204 se excluído com sucesso ou erro 404 se o mouse não for encontrado.
    result = db.mouse.delete_one({'_id': ObjectId(ativo_id)})
    if result.deleted_count == 0:
        return jsonify({'error': 'Ativo não encontrado'}), 404
    return '', 204

@app.route('/ativo/desktop/<ativo_id>', methods=['DELETE'])
def limpar_desktop(ativo_id):
    # Exclui as informações de um desktop específico pelo ID.
    # Retorna um código 204 se excluído com sucesso ou erro 404 se o desktop não for encontrado.
    result = db.desktop.delete_one({'_id': ObjectId(ativo_id)})
    if result.deleted_count == 0:
        return jsonify({'error': 'Ativo não encontrado'}), 404
    return '', 204

@app.route('/ativo/acessorios/<ativo_id>', methods=['DELETE'])
def limpar_acessorios(ativo_id):
    # Exclui as informações de um acessório específico pelo ID.
    # Retorna um código 204 se excluído com sucesso ou erro 404 se o acessório não for encontrado.
    result = db.acessorios.delete_one({'_id': ObjectId(ativo_id)})
    if result.deleted_count == 0:
        return jsonify({'error': 'Ativo não encontrado'}), 404
    return '', 204

@app.route('/ativo/nobreak/<ativo_id>', methods=['DELETE'])
def limpar_nobreak(ativo_id):
    # Exclui as informações de um nobreak específico pelo ID.
    # Retorna um código 204 se excluído com sucesso ou erro 404 se o nobreak não for encontrado.
    result = db.nobreak.delete_one({'_id': ObjectId(ativo_id)})
    if result.deleted_count == 0:
        return jsonify({'error': 'Ativo não encontrado'}), 404
    return '', 204

@app.route('/ativo/headset/<ativo_id>', methods=['DELETE'])
def limpar_headset(ativo_id):
    # Exclui as informações de um headset específico pelo ID.
    # Retorna um código 204 se excluído com sucesso ou erro 404 se o headset não for encontrado.
    result = db.headset.delete_one({'_id': ObjectId(ativo_id)})
    if result.deleted_count == 0:
        return jsonify({'error': 'Ativo não encontrado'}), 404
    return '', 204

@app.route('/ativo/celular/<ativo_id>', methods=['DELETE'])
def limpar_celular(ativo_id):
    # Exclui as informações de um celular específico pelo ID.
    # Retorna um código 204 se excluído com sucesso ou erro 404 se o celular não for encontrado.
    result = db.celular.delete_one({'_id': ObjectId(ativo_id)})
    if result.deleted_count == 0:
        return jsonify({'error': 'Ativo não encontrado'}), 404
    return '', 204

if __name__ == '__main__':
    app.run(debug=True)
