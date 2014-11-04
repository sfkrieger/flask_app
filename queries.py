from sqlalchemy import desc
from sqlalchemy.orm import Session
from models import BlogPost, engine
from sqlalchemy.orm.exc import NoResultFound

def create_session():
    db_session = Session()
    db_session.bind = engine
    return db_session


def create_blog_post(title, content):
    """
    Creates a new blog post given title and content.

    :param title: Title of the blog post
    :param content: Markdown
    :return:
    """
    db_session = create_session()
    post = BlogPost(title=title, content=content)
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