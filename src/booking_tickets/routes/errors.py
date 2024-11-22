from quart import redirect, url_for
from . import app
from .ticket_user import user_tickets


@app.errorhandler(404)
def page_not_found(error):
    return redirect(url_for(user_tickets.__name__))