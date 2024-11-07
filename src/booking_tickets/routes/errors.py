from quart import redirect, url_for
from . import app
from .ticket import tickets


@app.errorhandler(404)
def page_not_found(error):
    return redirect(url_for(tickets.__name__))