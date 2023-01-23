# Sistema de Cadastro
Tua missão é construir um sistema de cadastro de pessoas. Ele precisará atender aos seguintes requisitos:

## Menu principal
Ao iniciar o programa o seguinte menu deve ser imprimido:

```
Boas vindas ao nosso sistema:

1 - Inserir usuário
2 - Excluir usuário
3 - Atualizar usuário
4 - Informações de um usuário
5 - Informações de todos os usuários
6 - Sair

```

### 1 - Inserir usuário
Você deverá receber as seguintes informações: _nome_, _tefone_ e _endereço_.

Detalhes... Em sistemas de cadastro é convencionado adicionar automaticamente as seguintes informações:
- _id_: um número inteiro aleatório ou incremental que identifica um usuário (o id não pode se repetir);
- _status_: um valor booleano que indica se o usuário está ativo ao não. Por padrão esse valor é True

### 2 - Excluir usuário
Bem aqui vamos usar o _id_ e o _status_. Em sistemas em produção é evitado ao máximo a aplicação de delete, remove ou qualquer outra função que apague em definitivo um dado. 

Para isso usamos o que é chamado de _Exclusão Lógica_. Que em síntese muda o _status_ do usuário de True para False.

Você receberá do usuário o _id_ de um outro usuário dentro da base, e por fim vai alterar o valor do _status_ de True para False.

Caso o _id_ digitado não estiver dentro da base imprima uma mensagem de erro e peça novamente o _id_. Exemplo:
```
Usuário não encontrado!

Insira o ID do usuário:
```

### 3 - Atualizar usuário
Ao selecionar essa opção você deverá pedir o _id_ de um usuário:

```
Insira o ID do usuário:
```

Caso o _id_ digitado não estiver dentro da base imprima uma mensagem de erro e peça novamente o _id_. Exemplo:
```
Usuário não encontrado!

Insira o ID do usuário:
```

Ao inseri um _id_ correto imprima o seguinte sub menu:
```
Qual informação deseja alterar?
1 - Nome
2 - Tefone
3 - Endereço
```
E ao escolher a opção peça a nova informação da seguinte forma:

```
1
Insira o nome:
```

### 4 - Exibir informações de um usuário
Ao selecionar essa opção imprima o seguinte sub menu:
```
4
Insira o ID do usuário:
```

E deverá ser inserido o _id_ do usuário que deseja imprimir.
Se o _id_ inserido não for encontrado na base imprima uma mensagem de erro e peça o _id_ novamente. Exemplo:
```
Usuário não encontrado!

Insira o ID do usuário:
```

No momento que inserir um ID válido imprimir:

```
Nome: Davi Nascimento
Tefone: 2345678
Endereço: Rua Boa
```

### 5 - Informações de todos os usuários
Ao selecionar essa opção imprima as informações de todos os usuários

```
ID: 1
Nome: Davi Nascimento
Tefone: 2345678
Endereço: Rua Boa

ID: 2
Nome: Alex Lima
Tefone: 2345678
Endereço: Rua Top

ID: 3
Nome: Ivisson Cesar
Tefone: 2345678
Endereço: MAIOBÃO
```

### 6 - Sair
Encerre o programa.

## Observações
- A cada vez que você encerrar uma operação do programa imprima novamente o menu principal.
- O sistema deverá iniciar com uma lista predefinida de CINCO (5) usuários . Ou seja, o programa não começará do zero, já deve iniciar com usuários no sistema.
- Usem somente estruturas e técnicas que vimos nas aulas

```py
menu_str = """
\nBoas vindas ao nosso sistema:

1 - Inserir usuário
2 - Excluir usuário
3 - Atualizar usuário
4 - Informações de um usuário
5 - Informações de todos os usuários
6 - Sair\n
"""

sub_menu = """
\nQual informação deseja alterar?
1 - Nome
2 - Tefone
3 - Endereço
\n
"""


users = [
    [1,"Ciclano Sauro",2345678,"Rua Boa",True],
    [2,"Fulano Silva",3478358235,"Rua Top",True],
    [3,"John Doe",3853385267,"MAIOBÃO",True]
]
```