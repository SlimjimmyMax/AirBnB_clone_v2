#!/usr/bin/python3
""" Module for DBStorage class """
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, scoped_session
from models.base_model import BaseModel, Base
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review


class DBStorage:
    """ Class for managing database storage """

    __engine = None
    __session = None

    def __init__(self):
        """ Initialize DBStorage instance """
        self.__engine = create_engine('mysql+mysqldb://{}:{}@{}/{}'.
                                      format(os.getenv('HBNB_MYSQL_USER'),
                                             os.getenv('HBNB_MYSQL_PWD'),
                                             os.getenv('HBNB_MYSQL_HOST'),
                                             os.getenv('HBNB_MYSQL_DB')),
                                      pool_pre_ping=True)
        if os.getenv('HBNB_ENV') == 'test':
            Base.metadata.drop_all(self.__engine)

    def all(self, cls=None):
        """ Returns a dictionary of all objects """
        objs = {}
        if cls:
            for obj in self.__session.query(cls).all():
                key = "{}.{}".format(type(obj).__name__, obj.id)
                objs[key] = obj
        else:
            for clazz in [User, State, City, Amenity, Place, Review]:
                for obj in self.__session.query(clazz).all():
                    key = "{}.{}".format(type(obj).__name__, obj.id)
                    objs[key] = obj
        return objs

    def new(self, obj):
        """ Adds object to current database session """
        self.__session.add(obj)

    def save(self):
        """ Commits all changes to the current database session """
        self.__session.commit()

    def delete(self, obj=None):
        """ Deletes obj from current database session """
        if obj:
            self.__session.delete(obj)

    def reload(self):
        """ Reloads objects from database """
        Base.metadata.create_all(self.__engine)
        session_factory = sessionmaker(bind=self.__engine,
                                       expire_on_commit=False)
        self.__session = scoped_session(session_factory)

    def close(self):
        """ Calls remove() method on the private session attribute """
        self.__session.close()
