# ADA - Registration System
![Build Status](https://travis-ci.org/joemccann/dillinger.svg?branch=master)

- Instituição: Let's Code
- Curso: Data4All
- Disciplina: Lógica de Programação I
- Professores: Henrique Assis Cordeiro & Wenderson Alexandre de Sousa Silva
- Alunos: Matheus Carvalho de Brito, Matheus Miranda Brandão, Roberto Bruno Pontes dos Santos & Wendrik de Oliveira Santana.

Este projeto tem como objetivo a conclusão do módulo I do curso Data4All. Ela consiste em um sistema simples de cadastro de pessoas.

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
conda activate genome_search-venv
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
python -m venv genome_search-venv
```

- Ativar
```sh
source ./genome_search-venv/bin/activate
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
│   ├── registration_system
│   │   ├── __init__.py
│   │   ├── interface
│   │   │   └── Readme.md
│   │   └── Readme.md
│   └── utils
│       └── Readme.md
```


## Contribuições