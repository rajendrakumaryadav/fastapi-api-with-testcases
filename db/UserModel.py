from datetime import datetime

from sqlalchemy import Boolean, Column, Integer, String, DateTime

from .DB import Base


class User(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True, index=True)
    username = Column(String, unique=True, index=True)
    password = Column(String)
    is_active = Column(Boolean, default=True)
    created_at = Column(DateTime, default=datetime.utcnow)
    updated_at = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)

    def __repr__(self):
        return f"<User(username={self.username}, password={self.password}, is_active={self.is_active})>"

    def __str__(self):
        return f"<User(username={self.username}, password={self.password}, is_active={self.is_active})>"

    def __eq__(self, other):
        return self.username == other.username and self.password == other.password and self.is_active == other.is_active
