class CsvPersistance:

  def append(self, time, co2):
    self.csvFile = open("local-datastore.txt","a+")
    self.csvFile.write(time + ", " + co2 + "\r\n")

  def read(self):
    self.csvFile = open("local-datastore.txt","r")
    return self.csvFile.read()

  def close(self):
    self.csvFile.close()
