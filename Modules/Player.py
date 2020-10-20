import sqlite3
from tabulate import tabulate

class Player():
  connection = sqlite3.connect("game.db")
  cursor = connection.cursor()

  def __init__(self):
    self.profession = str()
    self.hp = int()
    self.st = int()
    self.mp = int()
    self.strength = int()
    self.vitality = int()
    self.knowledge = int()
    self.luck = int()
    self.wisdom = int()
    self.courage = int()
    self.agility = int()
    self.sanity = int()
    self.personality = int()
    self.level = int()
    self.experience = int()
    self.is_dead = False
    self.room_id = "Outside"


  def get_stats(self,character_id):
    for stat in self.cursor.execute('SELECT * FROM player'):
      if stat[0] == character_id:
        self.profession = stat[1]
        self.hp = stat[2]
        self.st = stat[3]
        self.mp = stat[4]
        self.strength = stat[5]
        self.vitality = stat[6]
        self.knowledge = stat[7]
        self.luck = stat[8]
        self.wisdom = stat[9]
        self.courage = stat[10]
        self.agility = stat[11]
        self.sanity = stat[12]
        self.personality = stat[13]
        self.level = stat[14]
        self.experience = stat[15]
        self.is_dead = stat[16].strip()
        self.room_id = stat[17]


  def score(self):
    table = [["Strength:",self.strength,"Vitality:",self.vitality],["Knowledge:",self.knowledge,"Luck:",self.luck],["Wisdom:",self.wisdom,"Courage:",self.courage],["Agility:",self.agility,"Sanity:",self.sanity],["Personality:",self.personality]]
    print("            CHARACTER STATS             ")
    print(tabulate(table,tablefmt="pretty"))


  def look(self):
    pass


  def move(self):
    pass


player = Player()