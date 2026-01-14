from sqlalchemy import Column, Integer, String, Text
from database import Base


class Profile(Base):
    __tablename__ = "profile"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)
    email = Column(String, nullable=False)
    skills = Column(Text)
    projects = Column(Text)
    github = Column(String)
    linkedin = Column(String)
