from sqlalchemy import Column, Integer, String, ForeignKey
from application.database import Base
from sqlalchemy.orm import relationship


class Profile(Base):
    __tablename__ = 'applications'

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String)
    body = Column(String)
    user_id = Column(Integer, ForeignKey('users.id'))

    creator = relationship("User", back_populates="applications")


class User(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    email = Column(String)
    password = Column(String)

    applications = relationship('Profile', back_populates="creator")
