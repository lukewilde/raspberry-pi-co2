# TODO: These imports feel kinda redundant.
from lib.Co2Sensor import Co2Sensor
from lib.Lcd import Lcd
from lib.CsvPersistance import CsvPersistance
from lib.WebSocket import WebSocket
import time

# TODO: As do these instantiations.

co2Sensor = Co2Sensor()
lcd = Lcd()
csvPersistance = CsvPersistance()
webSocket = WebSocket()

while True:
  co2Ppm = co2Sensor.getReading()

  lcd.display("CO2: " + str(co2Ppm) + " PPM")

  timestamp = str(time.time())
  co2Reading = str(co2Ppm)

  csvPersistance.append(timestamp, co2Reading)
  webSocket.send({'date': timestamp, 'co2': co2Reading})

  time.sleep(10)
