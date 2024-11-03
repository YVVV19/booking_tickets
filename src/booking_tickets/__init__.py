from quart import Quart
from .db import Config


app = Quart(__name__)

from . import routes


def run():
    try:
        Config.up()
        app.run()
    except Exception as ex:
        raise ex
    finally:
        Config.down()