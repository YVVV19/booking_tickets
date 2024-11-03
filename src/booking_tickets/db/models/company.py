from typing import List
from sqlalchemy.orm import Mapped, mapped_column, relationship
from . import Config


class Company(Config.BASE):
    name: Mapped[str]
    tickets: Mapped[List["Post"]] = relationship(back_populates="company")