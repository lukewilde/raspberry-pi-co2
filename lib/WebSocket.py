from websocket import create_connection
import thread
import time
import threading
import json

class WebSocket:
  def __init__(self):
    self.ws = create_connection("ws://192.168.0.13:8080")

  def send(self, data):
    self.ws.send(json.dumps(data))

  def close(self):
    self.ws.close()
