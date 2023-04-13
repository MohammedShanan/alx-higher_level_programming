#!/usr/bin/python3
"""
update state: given id, change state name
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

    state = session.query(State).filter_by(id=2).first() 
    state.name = "New Mexico"
    
    session.commit()
    session.close()
