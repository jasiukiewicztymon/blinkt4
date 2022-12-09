from flask import Flask, json

import threading
import requests
import socket
import logging
import time
import os

# Setup API
host_name = '0.0.0.0'
ip = 127.0.0.1
port = 5000
api = Flask(__name__)
    
# Game variables
status = False

# Hide Flask output
os.environ['WERKZEUG_RUN_MAIN'] = 'true'
logging.getLogger('werkzeug').disabled = True

# Config functons
def setPort(new_port)
    global port
    port = new_port
def setIP(new_ip)
    global ip
    ip = new_ip

# POST request to join
def join():
    while True:
        hosturl = input('Input the host IP: ') 
        requests.post(hosturl+':5000/host', { 'player_ip': ip })

def changeStatus():
    global status
    status = True

# GET request to host game
@api.route('/host', methods=['GET'])
def get_host():
    if status:
        return json.dumps({ 'status': 101, 'message': 'The player is already in a game' })
    else:
        play = input('A player want to play with you.. Do you accept the challenge ? [y|n] ')
        if play == 'y' or play == 'Y':
            changeStatus()
            return json.dumps({ 'status': 201, 'message': 'The player accepted the request' })
        else:
            return json.dumps({ 'status': 102, 'message': 'The player refused the request' })

def run():
    threading.Thread(target=lambda: api.run(host=host_name, port=port, debug=False, use_reloader=False)).start()
