from websocket import create_connection
import thread
import time
import threading
import json

# TODO: If the socket server is shutdown the will stop taking readings and attempt reconnction. I should really do this on a thread so I can continue taking readings.
class WebSocket:
  def __init__(self):
    self.ensureConnected()

  def send(self, data):
    try:
      self.ws.send(json.dumps(data))
    except:
      self.ensureConnected()

  def close(self):
    self.ws.close()

  def ensureConnected(self):
    address = "ws://192.168.0.13:8080"
    print("Connecting to websocket at: " + address + "...")
    self.ws = create_connection(address)
    print("Connected to websocket!")
