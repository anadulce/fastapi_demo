


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
