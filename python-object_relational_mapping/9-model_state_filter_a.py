#!/usr/bin/python3
"""
Module containing the State class definition and Base instance
"""

import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State  # Import your State and Base models from model_state

def print_states_with_a(username, password, db_name):
    engine = create_engine(f'mysql+mysqldb://{username}:{password}@localhost:3306/{db_name}')

    Session = sessionmaker(bind=engine)
    session = Session()
    states_with_a = session.query(State).filter(State.name.like('%a%')).order_by(State.id).all()

    for state in states_with_a:
        print(f"{state.id}: {state.name}")

    session.close()

if __name__ == "__main__":
    username, password, db_name = sys.argv[1], sys.argv[2], sys.argv[3]
    print_states_with_a(username, password, db_name)
