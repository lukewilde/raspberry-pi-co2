import websocket
import thread
import time

def on_open(ws):
    def run(*args):
        for i in range(3):
            time.sleep(1)
            ws.send("Hello %d" % i)
        time.sleep(1)
        ws.close()
        print("thread terminating...")
    thread.start_new_thread(run, ())


def on_message(ws, message):
  print(message)

def on_error(ws, error):
  print(error)

def on_close(ws):
  print("### closed ###")

class WebSocket:
  def __init__(self):
    # websocket.enableTrace(True)
    self.ws = websocket.WebSocketApp("ws://echo.websocket.org/", on_message = on_message, on_error = on_error, on_close = on_close)
    self.ws.on_open = on_open
    self.ws.run_forever()

  def send(self, message):
    self.ws.send(message)