# Curso de Introdução ao FastAPI

Vamos criar uma aplicação base do FastAPI, explorando os principais recursos do framework para a criação de endpoints.
Nessa aplicação, usaremos SQLAlchemy e Pydantic.

## Setup

Necessário instalar:
python 3.11.10
poetry 1.8.2
sqlite3 3.37.2

## Variáveis de ambiente
Criar arquivo .env
```
DATABASE_URL="sqlite:///fastapi_demo.db"
```

### Comandos para criação do banco
Inicializa migrações:

```bash
alembic init migrations
```

Comandos para usar **depois** de criar as models :D

Cria arquivos de migrações:
```bash
alembic revision --autogenerate -m "mensagem de criação"
```

Abre terminal interativo do banco:
```bash
sqlite3 fastapi_demo.db
```
Aqui você pode conferir que ainda não há nenhuma tabela

```bash
sqlite> .schema
sqlite> .quit
```
Aí vamos aplicar as migrações
```bash
alembic upgrade head
```
E se voltarmos novamente no banco, elas estarão lá!
```bash
sqlite> .schema
sqlite> .quit
```

## Executando o projeto

```bash
task run
```

## Referências

(Curso FastAPI do Zero)[https://fastapidozero.dunossauro.com/] - criado por Eduardo Mendes. Diferencial: é um conteúdo completo, que abrange não apenas o framework, mas toda a área de desenvolvimento de software para web de uma maneira muito mais profunda e completa, incluindo testes o deploy.

(Curso de introdução ao FastAPI do PyLadies São Carlos)[https://github.com/PyLadiesSanca/curso-fastapi] - criado por Juliana Karoline. Diferencial: usa SQLmodel, uma biblioteca criado pelo mesmo criador do FastAPI e que foi criada especialmente para se integrar ao framework.


