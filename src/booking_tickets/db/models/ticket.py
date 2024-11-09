from typing import List
from decimal import Decimal
from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy import ForeignKey
from . import Config


class Ticket(Config.BASE):
    title:Mapped[str]
    content:Mapped[str]
    company: Mapped["Company"] = relationship(back_populates="tickets")
    company_id: Mapped[int] = mapped_column(ForeignKey("companys.id"))