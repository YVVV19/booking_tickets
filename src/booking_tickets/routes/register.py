from quart import redirect, request, render_template, url_for
from . import User, app, Config


@app.get("/register")
async def register():
    return await render_template("register.html")


@app.post("/register")
async def create_register():
    form = await request.form
    if form:
        with Config.SESSION.begin() as session:
            register = [User(
                **form,
            )]
            session.add_all(register)
    return redirect(url_for("register"))