#!/usr/bin/python3
"""script that prints the State object with
   the name passed as argument from the database
"""
import sys
from model_state import Base, State
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

if __name__ == "__main__":

    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.
                           format(sys.argv[1], sys.argv[2],
                                  sys.argv[3]), pool_pre_ping=True)

    Base.metadata.create_all(engine)

    Session = sessionmaker()
    Session.configure(bind=engine)
    session = Session()
    result = None
    for state in session.query(State).filter(State.name == sys.argv[4]).all():
        result = state.id
    if result:
        print(result)
    else:
        print('Not found')

    session.close()
