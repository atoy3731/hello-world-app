import socket
from flask import Flask, render_template
import os

APP_PORT = int(os.environ.get('APP_PORT', '8000'))
APP_HOST = os.environ.get('APP_HOST', '0.0.0.0')

app = Flask(__name__)

@app.route('/')
@app.route('/index')
def index():
    return render_template('hello_world.html', local_hostname=socket.gethostname(), local_ip=socket.gethostbyname(socket.gethostname()))
    # return render_template('hello_kubernetes.html', local_hostname=socket.gethostname(), local_ip=socket.gethostbyname(socket.gethostname()))


if __name__ == '__main__':
    app.run(host=APP_HOST, port=APP_PORT)
