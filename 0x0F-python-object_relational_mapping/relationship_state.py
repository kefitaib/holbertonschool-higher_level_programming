#!/usr/bin/python3
""" task 6 """


from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from relationship_city import City, Base


# Base = declarative_base()


class State(Base):
    """ NEW CLASS """

    __tablename__ = 'states'
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(128), nullable=False)
    city = relationship("City", backref="state", cascade="all, delete")
