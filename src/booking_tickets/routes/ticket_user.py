from sqlalchemy import select, delete
from quart import render_template, request, redirect, url_for
from . import Company, Ticket, app, Config


@app.get("/book_tickets")
async def user_tickets():
    with Config.SESSION.begin() as session:
        smth = select(Ticket)
        tickets = session.scalars(smth).all()
        return await render_template(
            "index_book.html",
            tickets=tickets,
        )
    

@app.get("/tickets/book/<int:index>")
async def user_book_ticket_page(index: int):
    return await render_template("book_ticket.html", index=index)


@app.post("/tickets/book")
async def user_book_ticket():
    form = await request.form
    ticket_id = form.get("ticket_id")
    if ticket_id:
        with Config.SESSION.begin() as session:
            session.execute(delete(Ticket).where(Ticket.id == ticket_id))
    return redirect(url_for(user_tickets.__name__))
