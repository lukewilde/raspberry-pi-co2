import serial

class Co2Sensor:
  def __init__(self):
    self.serialInterface = serial.Serial("/dev/ttyS0", baudrate = 9600, timeout = 0.5)
    self.serialInterface.flushInput()

  def getReading(self):
    self.serialInterface.flushInput()
    self.serialInterface.write("\xFE\x44\x00\x08\x02\x9F\x25")
    resp = self.serialInterface.read(7)
    high = ord(resp[3])
    low = ord(resp[4])
    co2 = (high * 256) + low

    return co2
