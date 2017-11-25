import os

import config
from server.app import app_factory

current_config = config.Local
env = os.environ.get('ENV', '')

if hasattr(config, env):
    current_config = getattr(config, env)

api = app_factory(current_config)
