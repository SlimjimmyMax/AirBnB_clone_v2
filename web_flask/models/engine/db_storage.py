#!/usr/bin/python3
# 
from sqlalchemy.orm import sessionmaker

class DBStorage:
    # Existing code...

    def close(self):
        """Calls remove() method on the private session attribute (self.__session)"""
        self.__session.close()
