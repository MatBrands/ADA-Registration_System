import os
import platform
from model.Registration import *

def clear() -> None:
    so = platform.system()
    if so == 'Windows':
        os.system('cls')
    else:
        os.system('clear')

def initialize() -> bool | None:
    title = 'Boas vindas ao nosso sistema:'
    menu_options = [
        '1 - Inserir usuário',
        '2 - Excluir usuário',
        '3 - Atualizar usuário',
        '4 - Informações de um usuário',
        '5 - Informações de todos os usuários',
        '6 - Sair'
    ]
    registration = Registration()
    
    while True:
        clear() 
        print(title)
        for item in menu_options:
            print(item)
        
        option = input()
        if option == '1':
            menu_create(registration)
        elif option == '2':
            menu_delete(registration)
        elif option == '3':
            menu_update(registration)
        elif option == '4':
            menu_info(registration)
        elif option == '5':
            menu_all_info(registration)
        elif option == '6':
            return False

def menu_create(registration: Registration) -> None:
    clear() 
    print("Cadastrar usuário")
    
    id = str(registration.number_users()+1)
    name = input("Nome completo: ")
    telephone = input("Telefone com DDD (Apenas os números): ").zfill(11)
    address = input("Endereço completo: ")
    
    telephone = f"+55 ({telephone[:2]}) {telephone[2:7]}-{telephone[7:]}"
    
    user = {
        'id': id,
        'name': name,
        'telephone': telephone,
        'address': address
    }
    
    if registration.create_user(**user):
        input('Cadastro realizado com sucesso !\n')
    else:
        input('Erro\n')
    
    return

def menu_delete(registration: Registration) -> None:
    while True:
        clear() 
        print("Excluir usuário")

        id = input("Insira o ID do usuário (-1 para Sair): ")
        
        if id == '-1':
            break
        
        if registration.delete_user(id):
            input("Exclusão bem-sucedida\n")
            break
        else:
            input("Usuário não encontrado!\n")
            
    return

def menu_update(registration: Registration) -> None:
    while True:
        clear() 
        print("Atualizar dados do usuário")
        
        id = input("Insira o ID do usuário (-1 para Sair): ")
        
        if id == '-1':
            break
        
        user = registration.info_user(id)
        if not user:
            input("Usuário não encontrado!\n")
        else:
            break
        
    user['id'] = id
    option = input("Qual informação deseja alterar ?\n1 - Nome\n2 - Telefone\n3 - Endereço\n")
    if option == '1':
        user['name'] = input("Nome completo: ")
    elif option == '2':
        telephone = input("Telefone com DDD (Apenas os números): ").zfill(11)
        telephone = f"+55 ({telephone[:2]}) {telephone[2:7]}-{telephone[7:]}"
        user['telephone'] = telephone
    elif option == '3':
        user['address'] = input("Endereço completo: ")
    else:
        input("Opção inválida\n")
        return

    if registration.update_user(**user):
        input("Atualização bem sucedida\n")
    else:
        input("Erro\n")
        
    return

def menu_info(registration: Registration) -> None:
    while True:
        clear() 
        print("Exibir informações do usuário")

        id = input("Insira o ID do usuário (-1 para Sair): ")
        
        if id == '-1':
            return
        
        user = registration.info_user(id)
        if not user:
            input("Usuário não encontrado!\n")
        else:
            break
    
    print(f"Nome: {user['name']}")
    print(f"Telefone: {user['telephone']}")
    input(f"Endereço: {user['address']}\n")
    
    return

def menu_all_info(registration: Registration) -> None:
    clear() 
    print("Exibir informações de todos os usuários")
    
    all_users = registration.all_info_users()
    
    if not all_users:
        input("Erro\n")
        return
    
    for id, user in all_users.items():
        print(f"ID: {id}")
        print(f"Nome: {user['name']}")
        print(f"Telefone: {user['telephone']}")
        print(f"Endereço: {user['address']}", end='\n\n')
        
    input()
    
    return