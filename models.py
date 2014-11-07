"""
SQLAlchemy declarations.
"""
import datetime
from flask.ext.login import UserMixin
import markdown
import os
from sqlalchemy_utils.types.password import PasswordType
from sqlalchemy import create_engine, Integer, Column, String, Date, DateTime
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import deferred
from os import environ
from sqlalchemy import create_engine, update, ForeignKey
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
    __tablename__ = 'post'

    # On class construction all of these Column objects are replaced with
    # python descriptors. This is known as instrumentation and provides the class
    # with the means to move in and out of SQL and python objects.
    id = Column(Integer, primary_key=True)
    title = Column(String, nullable=False)
    content = deferred(Column(String))
    created_at = Column(DateTime, default=datetime.datetime.now)
    updated_at = Column(DateTime, default=datetime.datetime.now,
                        onupdate=datetime.datetime.now)
    summary = Column(String)
    # type = Column(String)
    type = Column(String, nullable=False, index=True)

    __mapper_args__ = {
        'polymorphic_on':type,
        'polymorphic_identity':'post'
    }

    @property
    def html(self):
        # converts the content (which is in markdown), into html
        # html contains the content as html, the function is rendering markdown as html...
        html = markdown.markdown(self.content)
        return html

    @property
    def date(self):
        return self.created_at.strftime("%A %d %B %Y")

    # @todo: finish this property if we want to include an abbreviation of the summary
    # @property
    # def abbreviated(self):


class Daily(BlogPost):
    # __tablename__ = "daily"

    __mapper_args__ = {
        'polymorphic_identity':'daily',
    }

class Weekly(BlogPost):
    # __tablename__ = "weekly"

    __mapper_args__ = {
        'polymorphic_identity':'weekly',
    }

class Project(BlogPost):
    # __tablename__ = "project"

    __mapper_args__ = {
        'polymorphic_identity':'project',
    }

class Todo(BlogPost):
    # __tablename__ = "todo"

    __mapper_args__ = {
        'polymorphic_identity':'todo',
    }

# class Type(object):
#     daily = 1
#     weekly = 2
#     project = 3
#     todo = 4

class User(Base, UserMixin):
    __tablename__ = 'User'
    id = Column(Integer, primary_key=True)
    user_name = Column(String)
    password = Column(PasswordType(
        schemes=[
            'pbkdf2_sha512'
        ]
    ))
    # self.active = active

Base.metadata.create_all(engine)
# user_datastore = SQLAlchemyUserDatastore(db, User, Role)
# security = Security(app, user_datastore)
#
# db.create_all()