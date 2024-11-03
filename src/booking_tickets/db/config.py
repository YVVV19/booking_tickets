from sqlalchemy.orm import DeclarativeBase, sessionmaker
from sqlalchemy import create_engine
from .mixins import AutoPrimaryKeyMixin, AutoTableNameMixin

class Base(DeclarativeBase, AutoTableNameMixin, AutoPrimaryKeyMixin):
    ...


class Config(object):
    BASE=Base
    ENGINE=create_engine("sqlite:///tickets.sql", echo=True)
    SESSION=sessionmaker(ENGINE)


    @classmethod
    def up(cls):
        cls.BASE.metadata.create_all(cls.ENGINE)

    
    @classmethod
    def down(cls):
        cls.BASE.metadata.drop_all(cls.ENGINE)