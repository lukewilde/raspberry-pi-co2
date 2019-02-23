from websocket import create_connection
import thread
import time
import threading
import json

# TODO: If the socket server is shutdown the app crashes. I think I need to add a listener / threading for this?
class WebSocket:
  def __init__(self):
    address = "ws://192.168.0.13:8080"
    print("Connecting to websoket at: " + address + "...")
    self.ws = create_connection(address)

  def send(self, data):
    self.ws.send(json.dumps(data))

  def close(self):
    self.ws.close()
