# Aperture

[Repositório original](https://github.com/murilo-toddy/aperture)

**Aperture** é um aplicativo para ajudar estudantes do ensino médio a se prepararem para o vestibular

## Features:

1. Todo-List
2. Acompanhamento de Notas
3. Áreas de Afinidade


## Construção:

O programa é construido em `Python` e conta com uma base de dados implementada utilizando `PostgreSQL`

É feito uso do `Docker` para organização da base e execução de comandos


## Dependências:

- `Python 3.9.5`
- `glade 3.38.2`
- `Psycopg2 2.9.2`
- `Docker 20.10.11`
- `docker-compose 1.29.2`

As bibliotecas para `python` podem ser instaladas utilizando:

```bash
pip install -r requirements.txt
```

## Execução

O programa conta com um `makefile` para organização dos arquivos.

- `make up`: Inicializa o ambiente no `docker`
- `make bg`: Inicializa o ambiente no `docker` em segundo plano
- `make down`: Encerra o processo no `docker`
- `make psql`: Abre o gerenciador do `PostgreSQL` no terminal
- `make setup_db`: Executa o script de criação de tabelas da base
- `make app`: Inicia a aplicação
- `make bootstrap`: Gera as tabelas e abre a aplicação
- `make all`: Realiza toda a configuração do sistema
