#!/usr/bin/python3
""" State Module for HBNB project """
import models
from models.base_model import BaseModel, Base
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship, backref
from os import getenv


class State(BaseModel, Base):
    """ State class """
    __tablename__ = "states"
    name = Column(String(128), nullable=False)

    if getenv("HBNB_TYPE_STORAGE") != "db":
        @property
        def cities(self):
            from models.city import City
            list_cities = []
            for cities in models.storage.all(City).values():
                if (cities.state_id) == self.id:
                    list_cities.append(cities)
            return list_cities
    else:
        cities = relationship("City", backref="state",
                              cascade="all, delete", passive_deletes=True)
