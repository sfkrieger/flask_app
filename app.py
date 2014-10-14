from flask import Flask, render_template
from models import init_db

app = Flask(__name__)


#To render a template you can use the render_template() method.
# Provide the name of the template and the variables you want to pass to the template engine as keyword arguments.
@app.route('/')
def index():
    return render_template('base_template.html')

@app.route('/daily/')
def daily():
    entries = [{'date':'Tuesday, October 14', 'title': 'My first blog', 'text':'Some things happened today'}]
    return render_template('daily.html', entries=entries)

@app.route('/weeklies/')
def weeklies():
    entries = [{'date':'Tuesday, October 14', 'title': 'My first blog', 'text':'Some things happened today'}]
    return render_template('weeklies.html', entries=entries)

@app.route('/projects/')
def proj():
    entries = [{'date':'Tuesday, October 14', 'title': 'My first blog', 'text':'Some things happened today'}]
    return render_template('projects.html', entries=entries)

@app.route('/resources/')
def resources():
    entries = [{'date':'Tuesday, October 14', 'title': 'My first blog', 'text':'Some things happened today'}]
    return render_template('resources.html', entries=entries)

# @app.route('/')
# def hello_world():
#     return render_template('daily.html')

if __name__ == '__main__':
    init_db()
    app.debug = True
    app.run()
