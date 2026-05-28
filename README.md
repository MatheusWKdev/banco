# Sistema Bancário em Python

Projeto de sistema bancário desenvolvido em Python no terminal para praticar lógica de programação, organização de código e Git/GitHub.

## Funcionalidades atuais

* Cadastro de usuários
* Menu interativo
* Sistema de repetição com `while`
* Organização em múltiplos arquivos
* Estrutura usando funções
* Armazenamento temporário de usuários em listas e dicionários

## Estrutura do projeto

```text id="1ux0k2"
banco.py/
│
├── main.py
├── menus.py
├── funcoes.py
├── dados.py
├── LICENSE
├── README.md
└── .gitignore
```

## Organização dos arquivos

### `main.py`

Responsável pelo fluxo principal do sistema:

* menu
* opções
* loop principal

### `menus.py`

Responsável pelos menus do sistema:

* menu principal
* futuros menus secundários

### `funcoes.py`

Responsável pelas funções do sistema:

* cadastrar usuário
* futuras funções de login
* depósitos
* saques
* transferências

### `dados.py`

Responsável pelo armazenamento dos dados do sistema:

* lista de usuários
* futuras contas bancárias
* histórico de operações

## Conceitos praticados

* Variáveis
* `if` e `elif`
* Loops (`while`)
* Funções
* Listas
* Dicionários
* Imports
* Organização de projeto
* Git e GitHub

## Licença

Este projeto utiliza a licença MIT.

## Como executar

No terminal:

```bash id="p5h9m1"
python main.py
```

## Objetivo do projeto

Treinar Python de forma prática criando um sistema cada vez mais completo, simulando funcionalidades reais de um banco.
