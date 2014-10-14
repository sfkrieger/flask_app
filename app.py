from flask import Flask, render_template
from models import init_db

app = Flask(__name__)


#To render a template you can use the render_template() method.
# Provide the name of the template and the variables you want to pass to the template engine as keyword arguments.
@app.route('/')
def hello_world():
    return render_template('child_template.html')


if __name__ == '__main__':
    init_db()
    app.run()
