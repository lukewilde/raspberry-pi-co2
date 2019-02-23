from RPLCD.gpio import CharLCD
import RPi.GPIO as GPIO

class Lcd:
  def __init__(self):
    print("Init LCD...")
    self.lcd = CharLCD(numbering_mode=GPIO.BOARD, cols = 16, rows = 2, pin_rs = 37, pin_e = 35, pins_data = [33, 31, 29, 23])

  def display(self, output):
    self.lcd.clear()
    self.lcd.write_string(output)
