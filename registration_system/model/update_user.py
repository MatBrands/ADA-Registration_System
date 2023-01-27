def atualizar_usuario():
    id_a_atualizar = int(input("Insira o ID do usuário: "))

    for usuario in lista_de_usuarios:
        if usuario["id"] == id_a_atualizar:
            info_a_alterar = int(input("Qual informação deseja alterar?\n1 - Nome\n2 - Telefone\n3 - Endereço\n"))

            if info_a_alterar == 1:
                novo_nome = input("Insira o nome: ")
                usuario["nome"] = novo_nome
            elif info_a_alterar == 2:
                novo_telefone = input("Insina o telefone: ")
                usuario["telefone"] = novo_telefone
            elif info_a_alterar == 3:
                novo_endereco = input("Insira o endereço: ")
                usuario["endereco"] = novo_endereco
            else:
                #retornar ao menu principal
                ...