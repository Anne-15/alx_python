#!/usr/bin/python3
"""
Module containing the State class definition and Base instance
"""

from sqlalchemy import create_engine, select
from sqlalchemy.orm import sessionmaker
from model_state import Base, State
import sys

if __name__ == "__main__":
    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]

    engine = create_engine("mysql+mysqldb://{} \
                           :{}@localhost:3306/{}" 
                           .format(username, password, database),
                           pool_pre_ping=True)
    
    Base.metadata.create_all(engine)

    Session = sessionmaker(bind=engine)
    session = Session(engine)

    states = select([State]).order_by(State.id)
    for state in states:
        print("{}: {}".format(state.id, state.name))

    session.close()
