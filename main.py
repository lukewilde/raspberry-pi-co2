from lib.Co2Sensor import Co2Sensor
from lib.Lcd import Lcd
from lib.CsvPersistance import CsvPersistance
from lib.WebSocket import WebSocket

import time

co2Sensor = Co2Sensor()
lcd = Lcd()
csvPersistance = CsvPersistance()
webSocket = WebSocket()

webSocket.send('ello?')

while False:
  co2Ppm = co2Sensor.getReading()

  lcd.display("CO2: " + str(co2Ppm) + " PPM")
  csvPersistance.append(str(time.time()), str(co2Ppm))

  time.sleep(1)
