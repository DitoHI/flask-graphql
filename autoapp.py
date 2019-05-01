from flask.helpers import get_debug_flag

from boilerplate.app import create_app
from boilerplate.settings import DevConfig, ProdConfig

CONFIG = DevConfig if get_debug_flag() else ProdConfig

app = create_app(CONFIG)