from quart import render_template
from . import app, Config


poll_data = {
    "question" : "What do you think about our site",
    "fields" : ['The best ever', 'Good', 'Not good not bad', 'Bad', 'The worst ever']
}

@app.get("/poll")
async def poll():
    return await render_template("poll.html", data=poll_data)