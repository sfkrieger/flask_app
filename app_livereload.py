from livereload import Server, shell
from app import app

server = Server(app.wsgi_app)
server.watch('scss/*.scss', shell('scss scss/main.scss', output='static/css/style.css'))
server.serve()