from quart import render_template
from . import app


@app.get("/contact_info")
async def contact_info():
    return await render_template("help.html")