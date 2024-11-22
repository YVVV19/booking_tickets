from quart import render_template, request, redirect, url_for
from . import app, Config, Poll


poll_data = {
    "question" : "What do you think about our site",
    "fields" : ['The best ever', 'Good', 'Not good not bad', 'Bad', 'The worst ever']
}

@app.get("/poll")
async def poll():
    return await render_template("poll.html", data=poll_data)

@app.post("/poll")
async def create_poll():
    form = await request.form
    if form:
        with Config.SESSION.begin() as session:
            polls = Poll(
                **form,
            )
            session.add(polls)
    return redirect(url_for("poll"))