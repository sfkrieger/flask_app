from unittest import TestCase
from models import init_db, BlogPost
from queries import create_blog_post, get_blog_posts_in_order, create_session


class CustomTestCase(TestCase):
    @classmethod
    def setUpClass(cls):
        super(CustomTestCase, cls).setUpClass()
        init_db()

    def tearDown(self):
        super(CustomTestCase, self).tearDown()
        create_session().query(BlogPost).delete()


class TestQueries(CustomTestCase):
    def test_create_blog_post(self):
        title = 'My Blog Post'
        content = 'My Content'
        post = create_blog_post(title=title,
                                content=content)
        self.assertEqual(post.title, title)
        self.assertEqual(post.content, content)
        self.assertTrue(post.created_at)
        self.assertTrue(post.updated_at)

    def test_get_blog_posts(self):
        for x in range(0, 3):
            create_blog_post(str(x), str(x))
        posts = get_blog_posts_in_order()
        self.assertEqual(posts[0].title, '0')
        self.assertEqual(posts[1].title, '1')
        self.assertEqual(posts[2].title, '2')
