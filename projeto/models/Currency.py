from sqlalchemy import Column, String, Integer, Float
from helpers.common import Base


class Currency(Base):
    __tablename__ = "currencies"

    id = Column(Integer, primary_key=True)
    name = Column(String)
    value = Column(Float)

    def __init__(self, **kwargs):
        for key, value in kwargs.items():
            if key == "name":
                self.name = value
            elif key == "value":
                self.value = value
