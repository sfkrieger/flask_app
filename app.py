from flask import Flask, request, session, g, redirect, url_for, abort, render_template, flash
import models, queries

"""
INFORMATION ABOUT CONVENTIONS USED:
Attempting to use RESTFUL API.

In the pursuit of this glorious endevour, Tommy boy has implemented a nice lil switch statement that basically
deals with all actions associated with a single blog post. I have no idea how this will work yet because I've been
a secretary on this project, but I'm seeeww stoked to see how things turn out for him.

So for starters, the way things are formatted:
We map resources with methods. There should be a single path given, and it should map different actions to that path.


UNDERSCORES:
Underscores are used to denote actions. They are the non-resful parts of the api.
When an action is an html page (such as add/edit), both the function and the path name will be appended with underscores

HELPER FUNCTIONS AND STATUS SYMBOLS:
1. For all helper functions, status symbols are returned.
- If the status is 1, it was successful, if it was -1 it was unsucessful

"""

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('base_template.html')


"""
=========== methods for blog listings ===========
"""


@app.route('/blogs/')
@app.route('/blogs/<page_type>')
def all_posts(page_type=None):
    # TODO: then the current request is just to get all the blogs...
    # pass # TODO: Display all blog entries (potentially for this page type)
    posts = queries.get_blog_posts_in_order()
    return render_template('all_blog_posts.html', page_type=page_type, entries=posts)

@app.route('/blogs/<blog_id>')
def single_post(blog_id):
    posts = [queries.get_byid(blog_id)]
    return render_template('all_blog_posts.html', page_type=None, entries=posts, single_page=True);

#Creates brand new blog post
@app.route('/blogs/', methods=['POST'])
def create_blog_post():
    new_entry = {'title': request.form['title'], 'text': request.form['text']}
    title = request.form['title']
    text = request.form['text']
    print title + " " + text
    queries.create_blog_post(title=title, content=text)
    return redirect(url_for('all_posts'))


# Renders the markdown form for adding new blog
@app.route('/blogs/editor')
@app.route('/blogs/editor/<blog_id>')
def editor(blog_id=None):
    blog = None
    if blog_id is not None:
        blog = queries.get_byid(blog_id)
    return render_template('editor.html', blog_item=blog)


"""
--------------------------------------------------
=========== switch for individual blog ===========
--------------------------------------------------
"""


@app.route('/blog/<blog_id>/', methods=['POST', 'GET'])
def manage_entry(blog_id):
    # Extract 'real' HTTP method from form hidden input
    input_method = request.form.get('method')
    if input_method and request.method == 'POST':
        # User submitted a form.
        if blog_id:
            if input_method == 'delete':
                blog = delete_blog(blog_id)
                if blog:
                    posts = queries.get_blog_posts_in_order()
                    return render_template('all_blog_posts.html', entries=posts)
                else:
                    pass  # TODO: Couldnt find the blog post to delete. Return an error.
                    # Delete blog post.
            elif input_method == 'put':
                # Update existing blog post.
                blog = update_blog(blog_id, request.form)
                if blog:
                    # TODO: Eventually should show the post that we just updated.
                    posts = queries.get_blog_posts_in_order()
                    return render_template('all_blog_posts.html', entries=posts)
                else:
                    pass  # TODO: Couldnt find the blog post to update. Return an error.
            else:
                pass  # TODO: Return an error. Enforce that no other method can be used here.
    else:
        # Browser requests ourwebsite.com/blog/ or ourwebsite.com/blog/<blog_id>
        if request.method == 'GET':
            if blog_id:
                pass  # TODO: Render jinja2 template to display a specific blog post.

        else:
            pass  # TODO: Return error.


"""
---------------------------------
=======HELPER FUNCTIONS==========
---------------------------------
"""

def delete_blog(blog_id):
    print "In the delete entry function..."
    type = request.form['type']
    id = request.form['id']
    deleted_blg = queries.delete_id(id)

    # not sure what this is doing...
    if (type == 'BlogPost'):
        print 'Recognized the type'
    else:
        print "Didn't recognize the type: " + type

    return deleted_blg


def update_blog(blog_id, request_form):
    print request_form
    # if request_form doesnt contain a key and throws a KeyError, Flask catches this and returns an error 400...
    # We have content as text in the form rather than just content...
    return queries.modify_byid(blog_id, title=request_form['title'], content=request_form['text'])


if __name__ == '__main__':
    # init_db()
    app.run(debug=True)
