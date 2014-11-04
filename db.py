__author__ = 'Samiam'

import sqlalchemy
import os
from os import environ
from sqlalchemy import create_engine
from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

conn_string = None
try:
    conn_string = environ['SQL_ALCHEMY_CONN_STRING']
except KeyError:
    print 'You need to set SQL_ALCHEMY_CONN_STRING'
    exit(1)

#there was something missing ps...
engine = create_engine(conn_string, echo=True)

# Classes mapped using the Declarative system are defined in terms of a base class
# which maintains a catalog of classes and tables relative to that base -
# this is known as the declarative base class.
DBase = declarative_base()

class Entry(DBase):
    __tablename__ = 'entry'

    id = Column(Integer, primary_key=True, autoincrement=True)
    title = Column(String)
    content = Column(String)


DBase.metadata.create_all(engine)
Session = sessionmaker(bind=engine)

# creating a new user
# ed_user = User(name='ed', fullname='Ed Jones', password='edspassword')
# >>> session.add(ed_user)

# double checking
# our_user = session.query(User).filter_by(name='ed').first()
# >>> our_user

# commit changes to the session (persist on db)
# >>> session.commit()\\

if __name__ == '__main__':
    pass