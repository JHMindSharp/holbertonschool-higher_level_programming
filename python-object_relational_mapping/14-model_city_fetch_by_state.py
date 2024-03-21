#!/usr/bin/python3
"""
Script that prints all City objects from the database hbtn_0e_14_usa.
Cities are sorted in ascending order by cities.id.
Results are formatted as <state name>: (<city id>) <city name>.
Usage: ./14-model_city_fetch_by_state.py mysql_username
mysql_password database_name
"""

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State
from model_city import City
import sys

if __name__ == "__main__":
    """
    Main method that lists all cities sorted by city id.
    It connects to the database, creates a session,
    and queries the City and State tables to fetch and print city information.
    """
    engine = create_engine(
        f'mysql+mysqldb://{sys.argv[1]}:{sys.argv[2]}@localhost/{sys.argv[3]}'
    )
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    session = Session()

    for city, state in session.query(City, State).filter(
            City.state_id == State.id).order_by(City.id).all():
        print(f"{state.name}: ({city.id}) {city.name}")

    session.close()
