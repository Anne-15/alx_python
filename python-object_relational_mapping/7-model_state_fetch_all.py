import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
# Import your State and Base models from model_state
from model_state import Base, State


def list_states(username, password, db_name):
    engine = create_engine(
        f'mysql+mysqldb://{username}:{password}@localhost:3306/{db_name}')

    Session = sessionmaker(bind=engine)
    session = Session()

    # Query and list all state objects order_by ID
    states = session.query(State).order_by(State.id).all()

    for state in states:
        print(f"{state.id}: {state.name}")

    session.close()


if __name__ == "__main__":
    username, password, db_name = sys.argv[1], sys.argv[2], sys.argv[3]
    list_states(username, password, db_name)
