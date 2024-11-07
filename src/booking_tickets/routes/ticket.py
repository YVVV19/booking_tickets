from sqlalchemy import select
from quart import render_template, request, redirect, url_for
from . import Company, Ticket, app, Config

@app.post("/tickets")
async def create_ticket():
    form = await request.form
    if form:
        with Config.SESSION.begin() as session:
            ticket = Ticket(
                **form,
                company=Company(name="ddek"),
            )
            session.add(ticket)
    return redirect(url_for("__base.html"))


@app.get("/ticket_details/<int:index>")
async def ticket_details(index: int):
    with Config.SESSION.begin() as session:
        ticket = session.query(Ticket).get(index)
        if not ticket:
            raise NotImplementedError("Ticket not found")
        return await render_template()


@app.get("/tickets")
async def tickets():
    with Config.SESSION.begin() as session:
        smth = select(Ticket)
        tickets = session.scalars(smth).all()
        return await render_template(
            "index.html",
            tickets=[
                Ticket(
                    
                )
                for x in tickets
            ],
        )