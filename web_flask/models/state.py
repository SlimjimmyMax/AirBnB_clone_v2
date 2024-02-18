#!/usr/bin/python3
# 
from models import storage

class State(BaseModel, Base):
    # Existing code...

    if storage_type != 'db':
        @property
        def cities(self):
            """Getter method to return the list of City objects linked to the current State"""
            cities_list = []
            for city in list(storage.all(City).values()):
                if city.state_id == self.id:
                    cities_list.append(city)
            return cities_list
