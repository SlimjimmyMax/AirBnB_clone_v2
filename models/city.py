from models.base_model import BaseModel, Base
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship

class City(BaseModel, Base):
    """City class"""
    __tablename__ = 'cities'
    name = Column(String(128), nullable=False)
    places = relationship('Place', backref='city', cascade='all, delete-orphan')
