#!/usr/bin/python3
"""
script that adds the State object Louisiana to the database hbtn_0e_6_usa
"""
import sys
from model_state import Base, State
from sqlalchemy.orm import Session
from sqlalchemy import create_engine


if __name__ == "__main__":
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'
                           .format(sys.argv[1], sys.argv[2], sys.argv[3]),
                           pool_pre_ping=True)
    Base.metadata.create_all(engine)
    session = Session(bind=engine)
    louisiana_state = State(name="Louisiana")
    session.add(louisiana_state)
    state = session.query(State).filter_by(name='Louisiana').first()
    session.commit()
    print(state.id)
    session.close()
