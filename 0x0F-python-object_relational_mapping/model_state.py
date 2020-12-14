#!/usr/bin/python3
"""
python file that contains the class definition of a State and an instance
Base = declarative_base():
"""
from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declrative import declarative_base

Base = declarative_base()


Class State(Base):
    """
    Class State inherits from Base Tips
    """
    id = Column(Integer, primary_key=True)
    name = Column(String(128), nullable=False)
    __tablename__ = "states"
