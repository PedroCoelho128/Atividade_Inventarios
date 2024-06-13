// Inserir novo funcionário
db.funcionario.insertOne({
    cpf: '313.876.864-54',
    nome: 'Ana Maria Braga'
});

// Criar coleções
db.createCollection("notebook");
db.createCollection("monitor");
db.createCollection("monitor2");
db.createCollection('teclado');
db.createCollection('mouse');
db.createCollection('desktop');
db.createCollection('acessorios');
db.createCollection('nobreak');
db.createCollection('headset');
db.createCollection('celular');

// Inserir documentos nas coleções com CPF ajustado
db.notebook.insertOne({
    cpf: "313.876.864-54",
    tag: "xyz1234",
    modelo: "Acer",
    n_serie: "76178231T812",
    versao_so: "Windows 11 Pro",
    caracteristicas: 'Intel i7 16GB RAM 512GB SSD "14',
    observacoes: 'Possui riscos na tela'
});

db.monitor.insertOne({
    cpf: "313.876.864-54",
    modelo: "AOC",
    n_serie: "1242342343",
    observacoes: ""
});

db.teclado.insertOne({
    cpf: "313.876.864-54",
    modelo: "logitech",
    n_serie: "41232132",
    observacoes: ""
});

db.mouse.insertOne({
    cpf: "313.876.864-54",
    modelo: "logitech",
    n_serie: "12323234",
    observacoes: ""
});

db.desktop.insertOne({
    cpf: '313.876.864-54',
    modelo: 'Lenovo',
    tag: 'abc4321',
    n_serie: '4562342343',
    versao: 'Windows 11 Pro',
    caracteristicas: 'Intel i5 16GB RAM 1 TB SSD',
    observacoes: ''
});

db.acessorios.insertOne({
    cpf: '313.876.864-54',
    suporte_notebook: 1,
    mouse_pad: 1,
    observacoes: ''
});

db.nobreak.insertOne({
    cpf: "313.876.864-54",
    modelo: "Asus",
    n_serie: "9622985",
    observacoes: ""
});

db.headset.insertOne({
    cpf: "313.876.864-54",
    modelo: "logitech",
    n_serie: "1822325",
    observacoes: ""
});

db.celular.insertOne({
    cpf: "313.876.864-54",
    modelo: 'Samsung Galaxy A03',
    imei1: "19823712895",
    numero: "19982249772",
    observacoes: ""
});
