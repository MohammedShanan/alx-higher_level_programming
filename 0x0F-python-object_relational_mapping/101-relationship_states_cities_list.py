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
    
    session = sessionmaker(bind=engine)
    session = session()

    states = session.query(State).order_by(State.id)
    for state in states:
        print("{:d}: {:s}".format(state.id, state.name))
        for city in state.cities:
            print("    {:d}: {:s}".format(city.id, city.name))
            
    
    session.close()
