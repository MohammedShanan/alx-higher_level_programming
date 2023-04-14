#!/usr/bin/python3
"""
return all cities from database via python
parameters given to script: username, password, database
"""


import sys
from model_state import Base, State
from model_city import City
from sqlalchemy import (create_engine)
from sqlalchemy.orm import sessionmaker

if __name__ == "__main__":
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.format(
        sys.argv[1], sys.argv[2], sys.argv[3]), pool_pre_ping=True)

    session = sessionmaker(bind=engine)
    session = session()

    rows = session.query(State.name, City.id, City.name).join(
        City, City.state_id == State.id).order_by(City.id)
    for row in rows:
        print("{:s}: ({:d}) {:s}".format(row[0], row[1], row[2]))

    session.close()
