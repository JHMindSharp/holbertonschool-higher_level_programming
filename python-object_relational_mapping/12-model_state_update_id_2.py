#!/usr/bin/python3
"""
Script that changes the name of the State object with the id 2 to "New Mexico"
in the database hbtn_0e_6_usa.
Usage: ./12-model_state_update_id_2.py mysql_username
mysql_password database_name
"""

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State
import sys

if __name__ == "__main__":
    engine = create_engine(
        f'mysql+mysqldb://{sys.argv[1]}:{sys.argv[2]}@localhost/{sys.argv[3]}'
        )
    Session = sessionmaker(bind=engine)
    session = Session()
    state = session.query(State).get(2)
    if state:
        state.name = "New Mexico"
    session.commit()
    session.close()
