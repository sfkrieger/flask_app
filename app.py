from flask import Flask, request, session, g, redirect, url_for, abort, render_template, flash
from models import init_db
import queries

app = Flask(__name__)


# To render a template you can use the render_template() method.
# Provide the name of the template and the variables you want to pass to the template engine as keyword arguments.
@app.route('/')
def index():
    return render_template('base_template.html')


@app.route('/daily/')
def daily():
    entries = [{'date': 'Tuesday, October 14', 'title': 'My first blog', 'text': 'Some things happened today'}]
    return render_template('daily.html', entries=entries)


@app.route('/weeklies/')
def weeklies():
    entries = [{'date': 'Tuesday, October 14', 'title': 'My first blog', 'text': 'Some things happened today'}]
    return render_template('weeklies.html', entries=entries)


@app.route('/projects/')
def proj():
    entries = [{'date': 'Tuesday, October 14', 'title': 'My first blog', 'text': 'Some things happened today'}]
    return render_template('projects.html', entries=entries)


@app.route('/resources/')
def resources():
    entries = [{'date': 'Tuesday, October 14', 'title': 'My first blog', 'text': 'Some things happened today'}]
    return render_template('resources.html', entries=entries)


@app.route('/daily-add/')
@app.route('/weeklies-add/')
@app.route('/projects-add/')
@app.route('/resources-add/')
def add():
    return render_template('add_entry.html')


#
# @app.route('/add', methods=['POST'])
# def add_entry():
#     if not session.get('logged_in'):
#         abort(401)
#     g.db.execute('insert into entries (title, text) values (?, ?)',
#                  [request.form['title'], request.form['text']])
#     g.db.commit()
#     flash('New entry was successfully posted')
#     return redirect(url_for('show_entries'))

@app.route('/add/', methods=['POST'])
def add_entry():
    new_entry = {'title':request.form['title'], 'text':request.form['text']}
    title = request.form['title']
    text = request.form['text']
    # print new_entry['title'] + " " + new_entry['text']
    print title + " " + text
    # queries.create_blog_post(**new_entry)
    queries.create_blog_post(title=title, content=text)
    return redirect(url_for('index'))


if __name__ == '__main__':
    init_db()
    app.run(debug=True)
