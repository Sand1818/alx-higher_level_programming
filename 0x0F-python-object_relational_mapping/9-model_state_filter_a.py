#!/usr/bin/pytho3
"""
Lists all State objects that contain the
letter a from hbtn_0e_6_usa
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
    ssession = Session()
    for _id_, _name_ in ssession.query(
                State.id, State.name
            ).order_by(State.id).filter(
                State.name.contains('a')
            ):
        print("{}: {}".format(_id_, _name_))