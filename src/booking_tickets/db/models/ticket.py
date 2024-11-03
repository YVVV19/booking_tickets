from typing import List
from decimal import Decimal
from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy import ForeignKey
from . import Config

class Ticket(Config.BASE):
    title:Mapped[str]
    clas:Mapped[int]
    where_start: Mapped[str]
    where_end: Mapped[str]
    date:Mapped[str]
    company: Mapped["Company"] = relationship(back_populates="tickets")
    company_id: Mapped[int] = mapped_column(ForeignKey("company.id"))
    price: Decimal