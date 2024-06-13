import requests
import json

BASE_URL = 'http://127.0.0.1:5000'

def inserir_funcionario():
    # Função para inserir um novo funcionário através de uma requisição POST.
    cpf = input('CPF: ')
    nome = input('Nome: ')
    data = {'cpf': cpf, 'nome': nome}
    response = requests.post(f'{BASE_URL}/funcionario', json=data)
    print(response.json())

def excluir_funcionario():
    # Função para excluir um funcionário através de uma requisição DELETE.
    cpf = input('CPF: ')
    response = requests.delete(f'{BASE_URL}/funcionario/{cpf}')
    if response.status_code == 204:
        print('Funcionário excluído com sucesso')
    else:
        print(response.json())

def listar_funcionarios():
    # Função para listar todos os funcionários através de uma requisição GET.
    response = requests.get(f'{BASE_URL}/funcionarios')
    print(json.dumps(response.json(), indent=4))

def consultar_inventario():
    # Função para consultar o inventário de um funcionário através de uma requisição GET.
    cpf = input('CPF: ')
    response = requests.get(f'{BASE_URL}/inventario/{cpf}')
    print(json.dumps(response.json(), indent=4))

def atualizar_nome_funcionario():
    # Função para atualizar o nome de um funcionário através de uma requisição PUT.
    cpf = input('CPF: ')
    nome = input('Novo Nome: ')
    data = {'nome': nome}
    response = requests.put(f'{BASE_URL}/funcionario/{cpf}', json=data)
    if response.status_code == 204:
        print('Nome atualizado com sucesso')
    else:
        print(response.json())

def atualizar_ativo(ativo):
    # Função para atualizar informações de um ativo específico através de uma requisição PUT.
    ativo_id = input('ID do Ativo: ')
    campo = input('Campo para atualizar: ')
    valor = input('Novo valor: ')
    data = {campo: valor}
    response = requests.put(f'{BASE_URL}/ativo/{ativo}/{ativo_id}', json=data)
    if response.status_code == 204:
        print('Ativo atualizado com sucesso')
    else:
        print(response.json())

def limpar_ativo(ativo):
    # Função para excluir um ativo específico através de uma requisição DELETE.
    ativo_id = input('ID do Ativo: ')
    response = requests.delete(f'{BASE_URL}/ativo/{ativo}/{ativo_id}')
    if response.status_code == 204:
        print('Ativo excluído com sucesso')
    else:
        print(response.json())

def menu():
    # Função que exibe um menu interativo para o usuário.
    while True:
        print("\nMenu:")
        print("1. Inserir Funcionário")
        print("2. Excluir Funcionário")
        print("3. Listar Funcionários")
        print("4. Consultar Inventário de Funcionário")
        print("5. Atualizar Nome de Funcionário")
        print("6. Atualizar Ativo")
        print("7. Limpar Ativo")
        print("8. Sair")
        
        escolha = input("Escolha uma opção: ")
        
        if escolha == '1':
            inserir_funcionario()
        elif escolha == '2':
            excluir_funcionario()
        elif escolha == '3':
            listar_funcionarios()
        elif escolha == '4':
            consultar_inventario()
        elif escolha == '5':
            atualizar_nome_funcionario()
        elif escolha == '6':
            print("Escolha o tipo de ativo:")
            print("1. Notebook")
            print("2. Monitor")
            print("3. Teclado")
            print("4. Mouse")
            print("5. Nobreak")
            print("6. Desktop")
            print("7. Headset")
            print("8. Celular")
            print("9. Acessórios")
            ativo_escolha = input("Escolha uma opção: ")
            ativos = ['notebook', 'monitor', 'teclado', 'mouse', 'nobreak', 'desktop', 'headset', 'celular', 'acessorios']
            if ativo_escolha in map(str, range(1, 10)):
                atualizar_ativo(ativos[int(ativo_escolha) - 1])
            else:
                print("Opção inválida. Tente novamente.")
        elif escolha == '7':
            print("Escolha o tipo de ativo:")
            print("1. Notebook")
            print("2. Monitor")
            print("3. Teclado")
            print("4. Mouse")
            print("5. Nobreak")
            print("6. Desktop")
            print("7. Headset")
            print("8. Celular")
            print("9. Acessórios")
            ativo_escolha = input("Escolha uma opção: ")
            ativos = ['notebook', 'monitor', 'teclado', 'mouse', 'nobreak', 'desktop', 'headset', 'celular', 'acessorios']
            if ativo_escolha in map(str, range(1, 10)):
                limpar_ativo(ativos[int(ativo_escolha) - 1])
            else:
                print("Opção inválida. Tente novamente.")
        elif escolha == '8':
            break
        else:
            print("Opção inválida. Tente novamente.")

if __name__ == '__main__':
    menu()
