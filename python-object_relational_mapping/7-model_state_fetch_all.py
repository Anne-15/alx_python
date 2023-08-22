#!/usr/bin/python3
"""
Module containing the State class definition and Base instance
"""

from sqlalchemy import create_engine, select
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from model_state import Base, State
import sys

if __name__ == "__main__":
    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]

    engine = create_engine("mysql+mysqldb://username\
                           :password@localhost:3306/dbname")
    Session = sessionmaker(bind=engine)
    Base.metadata.create_all(engine)
    session = Session(engine)
    stmt = select(State).order_by(State.id)
    for user in session.scalars(stmt):
        print(user)
