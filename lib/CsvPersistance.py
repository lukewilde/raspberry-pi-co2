class CsvPersistance:

  filename = "local-datastore.txt"

  def append(self, time, co2):
    self.csvFile = open(self.filename, "a+")
    self.csvFile.write(time + ", " + co2 + "\r\n")

  def read(self):
    self.csvFile = open(self.filename, "r")
    return self.csvFile.read()

  def close(self):
    self.csvFile.close()
