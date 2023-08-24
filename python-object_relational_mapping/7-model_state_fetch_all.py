#!/usr/bin/python3
"""
Module containing the State class definition and Base instance
"""

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State
import sys

if __name__ == "__main__":
    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]

    engine = create_engine("mysql+mysqldb://{} \
                           :{}@localhost:3306/{}"
                           .format(username, password, database))
    # Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    session = Session()
    new_states = ["California", "Arizona", "Texas", "New York", "Nevada"]
    for state_name in new_states:
        state = session.query(State).filter_by(name=state_name).first()
        if not state:
            new_state = State(name=state_name)
            session.add(new_state)
            session.commit()
