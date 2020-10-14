import socket
from flask import Flask, render_template
import os

APP_PORT = int(os.environ.get('APP_PORT', '8000'))
APP_HOST = os.environ.get('APP_HOST', '0.0.0.0')

VAULT_ENABLED = True if os.environ.get('VAULT_ENABLED', 'false') == "true" else False
DEMO_SECRET = os.environ.get('DEMO_SECRET')

app = Flask(__name__)


@app.route('/')
@app.route('/index')
def index():
    return render_template('hello_world.html', local_hostname=socket.gethostname(), local_ip=socket.gethostbyname(socket.gethostname()), vault_enabled=VAULT_ENABLED)
    # return render_template('hello_kubernetes.html', local_hostname=socket.gethostname(), local_ip=socket.gethostbyname(socket.gethostname()), vault_enabled=VAULT_ENABLED)


if __name__ == '__main__':
    if VAULT_ENABLED:
        print("\n====================")
        print("Vault is enabled! The secret is: {0}".format(DEMO_SECRET))
        print("====================\n")
    app.run(host=APP_HOST, port=APP_PORT)
