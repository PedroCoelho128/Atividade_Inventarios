# Sistema de Gerenciamento de Funcionários e Ativos

Este repositório contém um sistema de gerenciamento de funcionários e seus ativos, desenvolvido em Python utilizando Flask para a construção da API e MongoDB como banco de dados NoSQL para armazenamento dos dados.

# Requisitos do Sistema

Para executar o sistema localmente, você precisa garantir que seu ambiente atenda aos seguintes requisitos:

1. Python 3.x: Versão 3.7 ou superior.
   
2. Flask: Framework web para Python. Instale com o seguinte comando:
   
   pip install Flask
   
   
3. MongoDB: Banco de dados NoSQL. Certifique-se de ter o MongoDB instalado e em execução localmente. Você pode baixá-lo em [MongoDB Download](https://www.mongodb.com/try/download/community).
   
4. PyMongo: Driver Python para MongoDB. Instale com o seguinte comando:
   
   pip install pymongo
   

5. Python Requests: Biblioteca HTTP para fazer requisições para APIs externas. Instale com:
   
   pip install requests
   

# Configuração do Ambiente

1. Instalação das Dependências Python:
   - Crie um ambiente virtual para isolar as dependências do projeto (opcional, mas recomendado):

     python -m venv venv
     -No Windows: venv\Scripts\activate
     -No Unix ou MacOS: source venv/bin/activate


2. Configuração do MongoDB:
   - Certifique-se de que o MongoDB está instalado e em execução na porta padrão `27017`.

# Configuração do Banco

Copie o código em 'db.js' e adicione o banco no MongoDB

# Executando o Sistema

1. Iniciar o Servidor Flask:

   - Execute o arquivo `app.py` para iniciar o servidor Flask:

     python app.py

   - O servidor Flask será iniciado em modo de depuração (`debug=True`), adequado para ambiente de desenvolvimento.

2. Executar o Menu da Aplicação:

   - Após iniciar o servidor Flask, execute o arquivo `menu.py` para iniciar a interface de linha de comando (CLI) do sistema:

     python menu.py

   - O menu oferece diversas opções para gerenciar funcionários e ativos, interagindo com a API Flask que você iniciou previamente.

# Funcionalidades Implementadas

- Inserir Funcionário: Adiciona um novo funcionário ao sistema.
- Excluir Funcionário: Remove um funcionário do sistema, garantindo que não possua ativos associados.
- Listar Funcionários: Retorna uma lista de todos os funcionários cadastrados.
- Consultar Inventário de Funcionário: Exibe todos os ativos associados a um funcionário específico.
- Atualizar Nome de Funcionário: Altera o nome de um funcionário existente.
- Atualizar Ativo: Permite atualizar informações específicas de um tipo de ativo (notebook, monitor, etc.).
- Limpar Ativo: Remove um ativo específico do sistema.

# Considerações Finais

- Este sistema foi desenvolvido com o objetivo de demonstrar o uso de Python com Flask, MongoDB (utilizando PyMongo) e Requests para gerenciamento de dados.
- Certifique-se de que todas as dependências estão corretamente instaladas e configuradas antes de iniciar a aplicação.
- Para cenários de produção, considere ajustar as configurações de segurança e performance conforme necessário.

Com essas instruções, você estará pronto para configurar, iniciar e utilizar o sistema de gerenciamento de funcionários e ativos localmente.
