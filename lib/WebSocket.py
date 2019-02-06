from websocket import create_connection
import thread
import time
import threading

class WebSocket:

  def send(self, message):
    ws = create_connection("ws://192.168.0.13:8080")
    ws.send(message)
    ws.close()
