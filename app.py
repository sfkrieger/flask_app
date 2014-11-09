from flask import Flask, request, session, redirect, url_for, render_template
from flask.ext.login import LoginManager, login_user, login_required, logout_user

import queries
import config_secret

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
config_secret.install_secret_key(app)

# login_manager = LoginManager()
# login_manager.init_app(app)
#
# @login_manager.user_loader
# def load_user(userid):
# return User.get(userid)
#
# @app.route("/login", methods=["GET", "POST"])
# def login():
#     form = LoginForm()
#     if form.validate_on_submit():
#         # login and validate the user...
#         login_user(user)
#         flash("Logged in successfully.")
#         return redirect(request.args.get("next") or url_for("index"))
#     return render_template("login.html", form=form)
#
#
# @app.route("/logout")
# @login_required
# def logout():
#     logout_user()
#     return redirect(url_for('all_posts'))

# login happening
login_manager = LoginManager()
login_manager.init_app(app)

@app.route('/')
def index():
    return render_template('base_template.html')

"""
=========== auth ================================
"""
@login_manager.user_loader
def load_user(userid):
    return queries.get_user_byid(userid)

@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == 'POST':
        # try to validate user
        name = request.form['username']
        pswd = request.form['password']
        usr = queries.get_user_byname(name)
        if usr:
            if usr.password == pswd:
                login_user(usr)
                session['logged_in'] = True
                # session['username'] = name
                return redirect(url_for("index"))
        else:
            return render_template("login.html", err='No such user with username "' + name + '"')
    user_id = session.get('user_id')
    # session['username'] = request.form['username']
    # print "====================== " + user_id + "=========================="
    user = None
    if user_id:
        user = load_user(user_id)
    return render_template("login.html", user=user)

@app.route("/logout")
@login_required
def logout():
    logout_user()
    return redirect(url_for(all_posts))

#
"""
=========== methods for blog listings ===========
"""


@app.route('/blogs/')
def all_posts():
    # TODO: then the current request is just to get all the blogs...
    # pass # TODO: Display all blog entries (potentially for this page type)
    posts = queries.get_blog_posts_in_order()
    return render_template('all_blog_posts.html', page_type=request.args.get('page_type'), entries=posts)


@app.route('/blogs/<blog_id>')
def single_post(blog_id):
    post = queries.get_byid(blog_id)
    return render_template('single.html', post=post)


#Creates brand new blog post
@app.route('/blogs/', methods=['POST'])
def create_blog_post():
    new_entry = {'title': request.form['title'], 'text': request.form['text'], 'type': request.form['type']}
    title = request.form['title']
    text = request.form['text']
    type = request.form['type']
    print title + " " + text
    queries.create_blog_post(title=title, content=text, type=type)
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
