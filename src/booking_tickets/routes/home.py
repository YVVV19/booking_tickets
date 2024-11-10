from quart import render_template
from sqlalchemy import select
from . import app, Config, Ticket


@app.get("/home")
async def home():
    with Config.SESSION.begin() as session:
        smth = select(Ticket)
        tickets = session.scalars(smth).all()
    return await render_template("home.html", tickets=tickets)
