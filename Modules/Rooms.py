# importing csv module 
import csv 

class Room():

  def get_csv(self):
    filename = "CSV/rooms.csv"
    rows = [] 
    # reading csv file 
    with open(filename, 'r') as f: 
        csv_reader = csv.reader(f, delimiter=';')
        for line in csv_reader:
            rows.append(line)
        return rows
  
  def get_room(self,room):
    rows = self.get_csv()
    for row in rows:
      if row[0] == room:
        return row
    else:
      print("Error: Room not found.")