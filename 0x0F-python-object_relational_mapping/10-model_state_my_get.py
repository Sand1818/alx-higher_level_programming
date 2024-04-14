#!/usr/bin/pytho3
"""
Prints the State object with the name passed as
argument from hbtn_0e_6_usa
"""

import sys
from model_state import Base, State
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

if __name__ == "__main__":
    engine = create_engine(
            'mysql+mysqldb://{}:{}@localhost:3306/{}'.format(
                sys.argv[1],
                sys.argv[2],
                sys.argv[3]
                ), pool_pre_ping=True)
    Session = sessionmaker(bind=engine)
    ssesssion = Session()
    query = ssession.query(State).order_by(State.id).filter(
            State.name == sys.argv[4]
            )
    if len(query.all()) == 0:
        print("Not found")
    else:
        for row in ssession.query(State).order_by(State.id).filter(
                State.name == sys.argv[4]
                ):
            print(row.id)
