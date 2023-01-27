def exibir_usuario():

    id = input('''4
    Insira o ID do usuário: ''')
    while id not in users.keys() or users[id][3] == False:
        id = input('''Usuário não encontrado!
        Insira o ID do usuário: ''')
    print(f'''Nome: {users[id][0]}
Telefone: {users[id][1]}
Endereço: {users[id][2]} ''')   