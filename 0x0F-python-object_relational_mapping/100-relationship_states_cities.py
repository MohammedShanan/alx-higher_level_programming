#!/usr/bin/python3
"""
return all cities from database via python
parameters given to script: username, password, database
"""


import sys
from relationship_state import Base, State
from relationship_city import City
from sqlalchemy import (create_engine)
from sqlalchemy.orm import sessionmaker

if __name__ == "__main__":
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.format(
        sys.argv[1], sys.argv[2], sys.argv[3]), pool_pre_ping=True)
    Base.metadata.create_all(engine)

    session = sessionmaker(bind=engine)
    session = session()

    new_state = State(name="California")
    new_city = City(name="San Francisco", state=new_state)

    session.add_all([new_state, new_city])
    session.commit()
    session.close()
