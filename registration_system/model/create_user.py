def criar_usuario():
    nome = input("Insira o nome: ")
    telefone = input("Insira o telefone: ")
    endereco = input("Insira o endereço: ")


    usuario = dict(
        nome = nome,
        telefone = telefone,
        endereco = endereco,
        id = len(lista_de_usuarios) + 1,
        status = True
    )

    lista_de_usuarios.append(usuario)