#!/usr/bin/python3
"""lists all State objects from the database hbtn_0e_6_usa"""
import sys
from relationship_state import Base, State
from relationship_city import City
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

if __name__ == "__main__":
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.format(
                           sys.argv[1], sys.argv[2], sys.argv[3]),
                           pool_pre_ping=True)
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    session = Session()
    newState = State(name="California")
    session.add(newState)
    session.commit()
    newCity = City(name="San Francisco", state=newState)
    session.add(newCity)
    session.commit()
    session.close()
