# importing csv module 
import csv 

class Room():

  def get_rooms(self):
    filename = "CSV/rooms.csv"
    rows = [] 
    # reading csv file 
    with open(filename, 'r') as f: 
        csv_reader = csv.reader(f, delimiter=';')
        for line in csv_reader:
            rows.append(line)