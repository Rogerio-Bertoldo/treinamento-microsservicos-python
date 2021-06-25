from common import Base
from models import Pessoa

import sys

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


Session = sessionmaker()


if __name__ == '__main__':

    p = Pessoa(name='Rogerio', email='rogerio.silva@radixeng.com.br', last_name='Silva', phone_number="123456789")
    engine = create_engine('', echo=True)
    #print(p.__table__)
    Base.metadata.create_all(engine)

    Session.configure(bind=engine)
    session = Session()

    session.add(p)
    session.commit()

