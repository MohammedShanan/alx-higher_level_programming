#!/usr/bin/python3

"""
return first state object from database via python
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

    first_column = session.query(State).first()
    if first_column:
        print("{:d}: {:s}".format(first_column.id, first_column.name))
    else:
        print("Nothing")

    session.close()
