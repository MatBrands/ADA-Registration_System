# ADA - Registration System
![Build Status](https://travis-ci.org/joemccann/dillinger.svg?branch=master)

- Instituição: Let's Code
- Curso: Data4All
- Disciplina: Lógica de Programação I
- Professores: Henrique Assis Cordeiro & Wenderson Alexandre de Sousa Silva
- Alunos: Matheus Carvalho de Brito, Matheus Miranda Brandão, Roberto Bruno Pontes dos Santos & Wendrik de Oliveira Santana.

Este projeto tem como objetivo a conclusão do módulo I do curso Data4All. Ela consiste em um sistema simples de cadastro de pessoas.

A especificação completa do projeto pode ser encontrada em: [Projeto Final](https://github.com/MatBrands/ADA-Registration_System/blob/master/Projeto%20Final.ipynb)

## Conteúdo

- Integrantes
- Tecnologias
- Instalação
- Organização do projeto
- Contribuições

## Integrantes
Projeto desenvolvido pelos Devs:

- [Matheus Carvalho de Brito](https://github.com/mateuscbrito)
- [Matheus Miranda Brandão](https://github.com/MatBrands)
- [Roberto Bruno Pontes dos Santos](https://github.com/robertopnts)
- [Wendrik de Oliveira Santana](https://github.com/Wendr1k)

## Tecnologias


## Instalação

### Conda
No desenvolvimento foi utilizado o gerenciador de pacotes e ambientes [Conda](https://conda.io/). Portanto para prosseguir necessita-se de sua [instalação](https://conda.io/projects/conda/en/latest/user-guide/install/index.html).

- Navegar até a pasta de destino
```sh
cd utils
```

- Instalar dependências
```sh
conda env create environment.yml
```

- Ativar
```sh
conda activate registration_system_venv
```

- Desativar
```sh
conda deactivate
```

### Requirements
Pode-se utilizar o arquivo requiremets.txt para criar o ambiente virtual.

- Navegar até a pasta de destino
```sh
cd utils
```

- Criar ambiente virtual
```sh
python -m venv registration_system_venv
```

- Ativar
```sh
source ./registration_system_venv/bin/activate
```

- Instalar dependências
```sh
pip install -r requirements.txt
```

- Desativar
```sh
deactivate
```


## Organização do projeto
```sh
├── ADA-Registration_System
│   ├── LICENSE
│   ├── Readme.md
│   ├── Projeto Final.ipynb
│   ├── registration_system
│   │   ├── __init__.py
│   │   ├── interface
│   │   │   └── Readme.md
│   │   └── Readme.md
│   └── utils
│       └── Readme.md
```


## Contribuições