from sqlalchemy import select
from . import Company, app, Config


@app.get("/companies")
async def companies():
    with Config.SESSION.begin() as session:
        smth=select(Company)
        companies = session.scalars(smth).all()
