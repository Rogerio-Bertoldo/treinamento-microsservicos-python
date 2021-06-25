from sqlalchemy import Column, String, Integer, Float, DateTime, ForeignKey
from helpers.common import Base


class Quotations(Base):
    __tablename__ = "quotations"

    id = Column(Integer, primary_key=True)
    from_currency_id = Column('from_currency_id', Integer, ForeignKey('currencies.id'))
    from_currency_value = Column(Float)
    to_currency_id = Column('to_currency_id', Integer, ForeignKey('currencies.id'))
    to_currency_value = Column(Float)
    author = Column(String)
    date = Column(DateTime)

    def __init__(self, **kwargs):
        for key, value in kwargs.items():
            if key == "from_currency_id":
                self.from_currency_id = value
            elif key == "from_currency_value":
                self.from_currency_value = value
            elif key == "to_currency_id":
                self.to_currency_id = value
            elif key == "to_currency_value":
                self.to_currency_value = value
            elif key == "author":
                self.author = value
            elif key == "date":
                self.date = value
