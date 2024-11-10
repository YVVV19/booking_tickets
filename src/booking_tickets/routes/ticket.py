from sqlalchemy import select, delete
from quart import render_template, request, redirect, url_for
from . import Company, Ticket, app, Config


@app.get("/tickets")
async def tickets():
    with Config.SESSION.begin() as session:
        smth = select(Ticket)
        tickets = session.scalars(smth).all()
        return await render_template(
            "index.html",
            tickets=tickets,
        )


@app.post("/tickets")
async def create_ticket():
    form = await request.form
    if form:
        with Config.SESSION.begin() as session:
            tickets = [Ticket(
                **form,
                company=Company(name="ddek"),
            )]
            session.add_all(tickets)
    return redirect(url_for("tickets"))


@app.get("/ticket/<int:index>/details")
async def ticket_details(index: int):
    with Config.SESSION.begin() as session:
        ticket = session.query(Ticket).get(index)
        if not ticket:
            raise NotImplementedError("Ticket not found")
        return await render_template("ticket.html", ticket=ticket)

@app.get("/tickets/delete/<int:index>")
async def delete_ticket_page(index: int):
    return await render_template("delete_ticket.html", index=index)


@app.post("/tickets/delete")
async def delete_ticket():
    form = await request.form
    ticket_id = form.get("ticket_id")
    if ticket_id:
        with Config.SESSION.begin() as session:
            session.execute(delete(Ticket).where(Ticket.id == ticket_id))
    return redirect(url_for(tickets.__name__))