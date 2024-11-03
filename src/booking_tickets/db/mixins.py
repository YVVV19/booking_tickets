from sqlalchemy.orm import (
    Mapped,
    declared_attr,
    declarative_mixin,
    mapped_column,
)


@declarative_mixin
class AutoTableNameMixin:
    @declared_attr
    def __tablename__(cls):
        return cls.__name__.lower() + "s"


@declarative_mixin
class AutoPrimaryKeyMixin:
    id: Mapped[int] = mapped_column(primary_key=True)