from sqlalchemy import Column, Integer, String, Boolean, ForeignKey, TIMESTAMP, ForeignKeyConstraint
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func
from .database import Base

class Post(Base):
    """
    Represents a post in the application.
    """
    __tablename__ = "posts"

    id = Column(Integer, primary_key=True, nullable=False)
    title = Column(String, nullable=False)
    content = Column(String, nullable=False)
    published = Column(Boolean, server_default='TRUE', nullable=False)
    created_at = Column(TIMESTAMP(timezone=True), nullable=False, server_default=func.now())
    owner_id = Column(Integer, ForeignKey("users.id", ondelete="CASCADE"), nullable=False)

    owner = relationship("User")

class User(Base):
    """
    Represents a user in the application.
    """
    __tablename__ = "users"
    id = Column(Integer, primary_key=True, nullable=False)
    email = Column(String, nullable=False, unique=True)
    password = Column(String, nullable=False)
    created_at = Column(TIMESTAMP(timezone=True), nullable=False, server_default=func.now())

class Vote(Base):
    """
    Represents a vote on a post by a user.
    """
    __tablename__ = "votes"
    user_id = Column(Integer, primary_key=True)
    post_id = Column(Integer, primary_key=True)
    
    # Define explicit foreign key constraints
    user = relationship("User", foreign_keys=[user_id])
    post = relationship("Post", foreign_keys=[post_id])
    
    __table_args__ = (
        ForeignKeyConstraint([user_id], ["users.id"], ondelete="CASCADE"),
        ForeignKeyConstraint([post_id], ["posts.id"], ondelete="CASCADE"),
    )
