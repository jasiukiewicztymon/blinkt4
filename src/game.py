from flask import Flask, json

import threading
import requests
import socket

# Setup API
host_name = "0.0.0.0"
port = 5000
api = Flask(__name__)

# POST request to join
def join():
    hosturl = input('Input the host IP: ') 
    print('Linking...', hosturl, 'and', socket.gethostbyname(socket.gethostname()))
    requests.post(hosturl, { 'player_ip': socket.gethostbyname(socket.gethostname()) })

# GET request to host game
@api.route('/host', methods=['GET'])
def get_host():
  return json.dumps({ "name": "hello" })

threading.Thread(target=lambda: api.run(host=host_name, port=port, debug=True, use_reloader=False)).start()
