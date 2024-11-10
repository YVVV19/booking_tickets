from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy import ForeignKey
from . import Config


class Poll(Config.BASE):
    id: Mapped[int]=mapped_column(primary_key=True)
    answer:Mapped[str]
