#!/usr/bin/python3
""" Module for State class """
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship
import os


class State(BaseModel, Base):
    """ Class representing a state """

    __tablename__ = 'states'
    name = Column(String(128), nullable=False)

    if os.getenv('HBNB_TYPE_STORAGE') != 'db':
        @property
        def cities(self):
            """ Getter method to return the list of City objects linked to the current State """
            from models import storage
            cities_list = []
            for city in list(storage.all(City).values()):
                if city.state_id == self.id:
                    cities_list.append(city)
            return cities_list
