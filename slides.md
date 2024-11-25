---
marp: true
theme: rose-pine
---

# Introdução ao FastAPI

---

# Ana Dulce
- Desenvolvedora Python desde 2018 - atualmente engenheira de software no KaBuM!;
- Cofundadora do PyLadies São Carlos;
- Organizadora de eventos da comunidade Python no tempo livre;
- Atual Conselheira e ex-presidente da Associação Python Brasil;
- Python Fellow Member;


---

# Renan 

---

# Alinhando expectativas - o que **não** vamos abordar
- Deploy 
- Testes
- Observabilidade e monitoramento

Spoilers: Testes, observabilidade e muito mais sobre desenvolvimento de sistemas web, quem quiser, tem no minicurso de amanhã :D

---

# Objetivos

Criar uma aplicação web simples usando o framework FastAPI, usando o banco de dados SQLite3, o ORM SQLALchemy e Pydantic, onde possamos explorar essencialmente a **criação de endpoints** usando o framework, e maneiras de tornar o desenvolvimento mais ágil e menos propenso a erros.

---

# Instalação de bibliotecas

python 3.11.10
poetry 1.8.2
sqlite3 3.37.2

---
# Clonar o projeto do GitHub
https://github.com/anadulce/fastapi_demo


---

# Conhecendo o que já está pré-definido
- as bibliotecas necessárias para executar o projeto;
- formatadores e linter;
- alguns testes;
- automações de comandos no taskpy;

---

# Estrutura de arquivos inicial
```bash
fastapi_demo
    src
        __init__.py
        app.py
        database.py
        config.py
        models.py
    .env
    .gitignore
    pyproject.toml
    poetry.lock
    README.md
```

---

# Hello, world!



``` python
# src/app.py

from fastapi import FastAPI

app = FastAPI()


@app.get('/')
def index():
    return "Hello, world!"
```
# Executando

```bash
task run
```

---

# Configurações 

Criando o .env
```bash
# .env
DATABASE_URL="sqlite:///fastapi_demo.db"
```

---

# Configurações
``` python
# src/config.py

from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    model_config = SettingsConfigDict(
        env_file='.env', env_file_encoding='utf-8'
    )
    DATABASE_URL: str


settings = Settings()
```
---

# Criando a conexão com o banco
```python
# src/database.py

from sqlalchemy import create_engine
from sqlalchemy.orm import Session

from src.config import Settings

engine = create_engine(Settings().DATABASE_URL)


def get_session():
    with Session(engine) as session:
        yield session

```
---

# Criando as models
```python
# src/models.py

from datetime import datetime

from sqlalchemy import ForeignKey, func
from sqlalchemy.orm import Mapped, mapped_column, registry, relationship

table_registry = registry()

```
---

# Criando as models

```python
    # src/models.py

    @table_registry.mapped_as_dataclass
class Genre:
    __tablename__ = 'genre'

    id: Mapped[int] = mapped_column(init=False, primary_key=True)
    name: Mapped[str] = mapped_column(unique=True)

    created_at: Mapped[datetime] = mapped_column(default=func.now())
    updated_at: Mapped[datetime] = mapped_column(
        default=func.now(), onupdate=func.now()
    )
    movies: Mapped[list['Movie']] = relationship(
        init=False, back_populates='genre', cascade='all, delete-orphan'
    )
```
---

# Criando as models
```python
    # src/models.py
    @table_registry.mapped_as_dataclass
class Movie:
    __tablename__ = 'movie'

    id: Mapped[int] = mapped_column(init=False, primary_key=True)
    title: Mapped[str]
    director: Mapped[str]
    year: Mapped[int]

    genre_id: Mapped[int] = mapped_column(ForeignKey('genre.id'))

    genre: Mapped[Genre] = relationship(init=False, back_populates='movies')

    created_at: Mapped[datetime] = mapped_column(default=func.now())
    updated_at: Mapped[datetime] = mapped_column(
        default=func.now(), onupdate=func.now()
    )

```
---
# Comandos para criação do banco
Inicializa migrações:

```bash
alembic init migrations
```

---
# Configurando o banco
No arquivo `migrations/env.py`, adicionar depois do import:
```python
from src.models import table_registry
from src.config import Settings
```
Mudar a configuração principal:
```python
config.set_main_option('sqlalchemy.url', Settings().DATABASE_URL)

```
Setar o target_metadata:

```python
target_metadata = table_registry.metadata
```
---

# Cria arquivos de migrações
```bash
alembic revision --autogenerate -m "mensagem de criação"
```
---

# Conferindo o banco

Abrir terminal interativo do banco:
```bash
sqlite3 fastapi_demo.db
```
Aqui você pode conferir que ainda não há nenhuma tabela

```sqlite
sqlite> .schema
sqlite> .quit
```

---
# Aplicando as migrações
```bash
alembic upgrade head
```
E se voltarmos novamente no banco, elas estarão lá!
```bash
sqlite> .schema
sqlite> .quit
```

---

---



---




poetry add sqlalchemy

poetry add pydantic-settings

.env
DATABASE_URL="sqlite:///fastapi_demo.db"

poetry add alembic

Inicializa migrações
alembic init migrations

Cria migrações
alembic revision --autogenerate -m "mensagem de criação"


Abre terminal interativo
sqlite3 fastapi_demo.db

Só mostrar as tabelas que tem no banco (só a do alembic)
sqlite> .schema
sair: .quit ou uns control C 

Aplica migrações
alembic upgrade head

Só mostrar as tabelas que o alembic criou
sqlite> .schema
sair: .quit ou uns control C 
