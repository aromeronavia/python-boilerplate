from __future__ import with_statement

import os
import sys

from alembic import context
from sqlalchemy import create_engine

sys.path.insert(0, os.path.realpath(os.path.join(os.path.dirname(__file__), '..')))

import config  # noqa

try:
    environment = os.environ.get('ENV', 'Local')
    AppConfig = getattr(config, environment)
except AttributeError:
    raise Exception(
        'Configuration environment \'' + environment + '\' does '
        'not exists in the configuration file config.py. Please make '
        'sure to add it or use an existing environment.'
    )

config = context.config

from server.database.base import Base  # noqa
target_metadata = Base.metadata


def run_migrations_offline():
    """Run migrations in 'offline' mode.

    This configures the context with just a URL
    and not an Engine, though an Engine is acceptable
    here as well.  By skipping the Engine creation
    we don't even need a DBAPI to be available.

    Calls to context.execute() here emit the given string to the
    script output.

    """
    url = AppConfig.SQLALCHEMY_URI
    context.configure(
        url=url,
        target_metadata=target_metadata,
        literal_binds=True
    )

    with context.begin_transaction():
        context.run_migrations()


def run_migrations_online():
    """Run migrations in 'online' mode.

    In this scenario we need to create an Engine
    and associate a connection with the context.

    """
    connectable = create_engine(AppConfig.SQLALCHEMY_URI)

    with connectable.connect() as connection:
        context.configure(
            connection=connection,
            target_metadata=target_metadata
        )

        with context.begin_transaction():
            context.run_migrations()


if context.is_offline_mode():
    run_migrations_offline()
else:
    run_migrations_online()
