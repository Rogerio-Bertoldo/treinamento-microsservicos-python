from sqlalchemy import create_engine
from sqlalchemy.sql import select
from sqlalchemy.orm import sessionmaker
import sys
# from helpers import params
from helpers.common import Base
from models.Currency import Currency

Session = sessionmaker()

if __name__ == '__main__':
    dollar = Currency(name="Dollar", value=5.09)
    euro = Currency(name="Euro", value=6.04)
    iene = Currency(name="Iene Japones", value=0.046)

    engine = create_engine('postgresql://postgres:Teste123@localhost/treinamento_radix', echo=True)
    Base.metadata.create_all(engine)

    Session.configure(bind=engine)
    session = Session()

    q = session.query(Currency)
    result = [r for r in q]
    print(result[0].name)

    if len(sys.argv) > 1 and sys.argv[1] == 'init':
        session.add(dollar)
        session.add(euro)
        session.add(iene)
        session.commit()
