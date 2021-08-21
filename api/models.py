from lib.db import Base
from sqlalchemy import Column, Integer, String


class Project(Base):
    __tablename__ = "project"
    id = Column(Integer, primary_key=True)
    name = Column(String)
