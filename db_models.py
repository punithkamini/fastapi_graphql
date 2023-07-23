from db_connections import Base
from sqlalchemy import Column, Integer, String


class Items(Base):
    __tablename__ = "items"

    itemId = Column(Integer, primary_key=True)
    itemName = Column(String, nullable=False)
    description = Column(String, nullable=False)
    price = Column(Integer, nullable=False)
