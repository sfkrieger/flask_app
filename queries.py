from sqlalchemy import desc
from sqlalchemy.orm import Session
from models import BlogPost, engine, User
from sqlalchemy.orm.exc import NoResultFound


def create_session():
    db_session = Session()
    db_session.bind = engine
    return db_session


def create_blog_post(title, content, type):
    """
    Creates a new blog post given title and content.

    :param title: Title of the blog post
    :param content: Markdown
    :param type: The type of article
    :return:
    """
    db_session = create_session()
    post = BlogPost(title=title, content=content, type=type)
    db_session.add(post)
    db_session.commit()
    return post


def get_blog_posts_in_order():
    """
    Returns all blog posts in date order

    :return:
    """
    db_session = create_session()
    return db_session.query(BlogPost).order_by(desc(BlogPost.created_at))


def get_byid(blog_id):
    """
    Returns the blog post by the id
    :return: the item that you're looking for you dum
    """

    db_session = create_session()
    qry = db_session.query(BlogPost).filter(BlogPost.id == blog_id)
    item = qry.one()
    return item


def delete_id(id):
    db_session = create_session()
    qry = db_session.query(BlogPost).filter(BlogPost.id == id)
    try:
        todel = qry.one()
    except NoResultFound, e:
        print e
        return None
    print todel.id
    print todel.title
    db_session.delete(todel)
    db_session.commit()
    return todel


def modify_byid(blog_id, content, title):
    db_session = create_session()
    qry = db_session.query(BlogPost).filter(BlogPost.id == blog_id)
    try:
        entry = qry.one()
    except NoResultFound, e:
        print e
        return None
    entry.content = content
    entry.title = title
    db_session.commit()
    return entry

def create_user(name, password):
    db_session = create_session()
    usr = User()
    usr.user_name = name
    usr.password = password
    db_session.add(usr)
    db_session.commit()
    return usr

def get_user_byid(id):
    db_session = create_session()
    qry = db_session.query(BlogPost).filter(User.id == id)
    try:
        entry = qry.one()
    except NoResultFound, e:
        print e
        return None
    return qry

def get_user_byname(name):
    db_session = create_session()
    qry = db_session.query(User).filter(User.user_name == name)
    try:
        entry = qry.one()
    except NoResultFound, e:
        print e
        return None
    return entry
