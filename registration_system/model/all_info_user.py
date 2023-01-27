def usuariosAtivos(a:dict) -> dict:
    ativos = []
    for i in range(len(a)):
        if (a[i][4]):
            ativos.append(a[i])
    return ativos