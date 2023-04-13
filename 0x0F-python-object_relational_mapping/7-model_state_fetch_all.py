#!/usr/bin/python3
"""
return all state objects from database via python
parameters given to script: username, password, database
"""
import sys
from model_state import Base, State
from sqlalchemy import (create_engine)
from sqlalchemy.orm import sessionmaker

if __name__ == "__main__":
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.format(
        sys.argv[1], sys.argv[2], sys.argv[3]), pool_pre_ping=True)
    session = sessionmaker(bind=engine)
    session = session()

    for instance in session.query(State).all():
        print("{:d}: {:s}".format(instance.id, instance.name))

    session.close()
