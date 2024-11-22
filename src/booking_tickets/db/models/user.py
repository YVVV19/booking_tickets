from sqlalchemy.orm import Mapped, mapped_column
from . import Config


class User(Config.BASE):
    id: Mapped[int]=mapped_column(primary_key=True)
    username: Mapped[str]
    email: Mapped[str]
    password: Mapped[str] 