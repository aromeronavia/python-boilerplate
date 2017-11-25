from sqlalchemy import Column, Integer, String

from server.database.base import Base


class User(Base):
    __tablename__ = 'user'

    id = Column(Integer(), primary_key=True)
    username = Column(String(60), nullable=False)
