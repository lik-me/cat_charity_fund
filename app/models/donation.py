from sqlalchemy import Column, Text, Integer, ForeignKey
from app.core.db import Base, BaseAdd
from app.models import User


class Donation(Base):
    user_id = Column(Integer, ForeignKey(User.id))
    comment = Column(Text)
