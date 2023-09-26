from logging.config import fileConfig
from sqlalchemy import create_engine
from alembic import context
from app.models import Base
from app.config import settings

# This is the Alembic Config object, which provides access to the values within the .ini file in use.
config = context.config

# Set the SQLAlchemy URL using the settings from your configuration.
db_url = (
    f'postgresql+psycopg2://{settings.database_username}:{settings.database_password}'
    f'@{settings.database_hostname}:{settings.database_port}/{settings.database_name}'
)
config.set_main_option("sqlalchemy.url", db_url)

# Interpret the config file for Python logging.
fileConfig(config.config_file_name)

# Specify the target metadata for Alembic migrations.
target_metadata = Base.metadata

def run_migrations_offline():
    """
    Run migrations in 'offline' mode.

    This configures the context with just a URL and not an Engine.
    By skipping Engine creation, we don't even need a DBAPI to be available.
    """
    context.configure(
        url=config.get_main_option("sqlalchemy.url"),
        target_metadata=target_metadata,
        literal_binds=True,
        dialect_opts={"paramstyle": "named"},
    )

    with context.begin_transaction():
        context.run_migrations()

def run_migrations_online():
    """
    Run migrations in 'online' mode.

    In this scenario, we create an Engine and associate a connection with the context.
    """
    engine = create_engine(config.get_main_option("sqlalchemy.url"))
    
    with engine.connect() as connection:
        context.configure(
            connection=connection, target_metadata=target_metadata
        )

        with context.begin_transaction():
            context.run_migrations()

if context.is_offline_mode():
    run_migrations_offline()
else:
    run_migrations_online()
