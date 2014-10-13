from sqlalchemy.orm import Session
from models import BlogPost, engine


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
    return db_session.query(BlogPost).order_by(BlogPost.created_at)