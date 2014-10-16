"""
SQLAlchemy declarations.
"""
import datetime
import markdown
from sqlalchemy import create_engine, Integer, Column, String, Date, DateTime
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import deferred
from os import environ

conn_string = None
try:
    conn_string = environ['SQL_ALCHEMY_CONN_STRING']
except KeyError:
    print 'You need to set SQL_ALCHEMY_CONN_STRING'
    exit(1)

# This is the creation of the db, stored in memory vs. disk vs. remote (uses db drivers, so must connect through socket)
engine = create_engine(conn_string, echo=True)
Base = declarative_base()


class BlogPost(Base):
    """
    A model representing a Blog Post.
    """
    __tablename__ = 'posts'

    # On class construction all of these Column objects are replaced with
    # python descriptors. This is known as instrumentation and provides the class
    # with the means to move in and out of SQL and python objects.
    id = Column(Integer, primary_key=True)
    title = Column(String, nullable=False)
    content = deferred(Column(String))
    created_at = Column(DateTime, default=datetime.datetime.now)
    updated_at = Column(DateTime, default=datetime.datetime.now,
                        onupdate=datetime.datetime.now)

    @property
    def html(self):
        html = markdown.markdown(self.content)
        return html

    @property
    def date(self):
        return self.created_at.strftime("%A %d %B %Y")


def init_db():
    Base.metadata.create_all(engine)


