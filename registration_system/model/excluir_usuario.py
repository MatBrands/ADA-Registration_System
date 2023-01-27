def excluir_usuario():

    id = input('''2
    Digite um id para excluir: ''')
    while id not in users.keys():
        id = input('''Usuário não encontrado!

    Insira o ID do usuário: ''')
    users[id][3] = False
