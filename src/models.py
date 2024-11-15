import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship, declarative_base
from sqlalchemy import create_engine
from eralchemy2 import render_er


Base = declarative_base()

class User(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True)
    username = Column(String(80), unique=True, nullable=False)
    email = Column(String(120), unique=True, nullable=False)
    password= Column(String(255), nullable=False)
  
    
    favorites = relationship('Favorite')


class Character(Base):
    __tablename__ = 'characters'
    id = Column(Integer, primary_key=True)
    name = Column(String(100), nullable=False)
    description = Column(String)
    gender = Column(String, nullable=True)  
    hairColor = Column(String(100), nullable=False)
    eyeColor = Column(String)

    
    favorites = relationship('Favorite')


class Planet(Base):
    __tablename__ = 'planets'
    id = Column(Integer, primary_key=True)
    name = Column(String(100), nullable=False)
    description = Column(String(100))
    population = Column(Integer)
    terrain = Column(String(100))

    
    favorites = relationship('Favorite')


class Vehicle(Base):
    __tablename__ = 'vehicles'

    id = Column(Integer, primary_key=True)
    name = Column(String(100), nullable=False)
    type = Column(String(100))  
    model = Column(String(100))
    manufacturer = Column(String(100))
    description = Column(String)

    
    favorites = relationship('Favorite')


class Favorite(Base):
    __tablename__ = 'favorites'

    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('users.id'), nullable=False)
    character_id = Column(Integer, ForeignKey('characters.id'), nullable=True)
    planet_id = Column(Integer, ForeignKey('planets.id'), nullable=True)
    vehicle_id = Column(Integer, ForeignKey('vehicles.id'), nullable=True)


    user = relationship('User')
    character = relationship('Character')
    planet = relationship('Planet')
    vehicle = relationship('Vehicle')


try:
    result = render_er(Base, 'diagram.png')
    print("Success! Check the diagram.png file")
except Exception as e:
    print("There was a problem generating the diagram")
    raise e
