from logging.config import fileConfig
from sqlalchemy import engine_from_config, pool
from alembic import context
import os
import sys

# 🔹 Adiciona o diretório raiz ao sys.path para permitir imports do app/
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))

# 🔹 Importa seu config e Base do SQLAlchemy
from app.core.config import config as app_config
from app.db.user_schema import Base

# 🔹 Configuração padrão do Alembic
alembic_config = context.config
fileConfig(alembic_config.config_file_name)

# 🔹 Substitui a URL do alembic.ini pela sua do projeto
alembic_config.set_main_option("sqlalchemy.url", app_config.db_url)

# 🔹 Metadados usados para autogeração
target_metadata = Base.metadata


def run_migrations_offline():
    """Executa migrações no modo offline (sem conexão direta)"""
    url = alembic_config.get_main_option("sqlalchemy.url")
    context.configure(
        url=url,
        target_metadata=target_metadata,
        literal_binds=True,
        dialect_opts={"paramstyle": "named"},
    )

    with context.begin_transaction():
        context.run_migrations()


def run_migrations_online():
    """Executa migrações no modo online (com engine real)"""
    connectable = engine_from_config(
        alembic_config.get_section(alembic_config.config_ini_section),
        prefix="sqlalchemy.",
        poolclass=pool.NullPool,
    )

    with connectable.connect() as connection:
        context.configure(connection=connection, target_metadata=target_metadata)

        with context.begin_transaction():
            context.run_migrations()


if context.is_offline_mode():
    run_migrations_offline()
else:
    run_migrations_online()
