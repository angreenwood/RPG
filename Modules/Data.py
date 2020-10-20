import sqlite3
import re
from passlib.hash import pbkdf2_sha256
import random
from tabulate import tabulate

class Database():
  connection = sqlite3.connect("game.db")
  cursor = connection.cursor()
  character_name = ""

  def create_table(self):
    # Creation of players table
    self.cursor.execute('CREATE TABLE IF NOT EXISTS player(playerID INTEGER PRIMARY KEY, Profession TEXT, HP INTEGER, ST INTEGER, MP INTEGER, Strength INTEGER, Vitality INTEGER, Knowledge INTEGER, Luck INTEGER, Wisdom INTEGER, Courage INTEGER, Agility INTEGER, Sanity INTEGER, Personality INTEGER, Level INTEGER, Experience INTEGER, is_dead TEXT, room_ID INTEGER)')

    # Creation of users table for username and password
    self.cursor.execute('CREATE TABLE IF NOT EXISTS users(userID INTEGER PRIMARY KEY,username TEXT, password TEXT, FOREIGN KEY(userID) REFERENCES player(playerID) )')


  def create_user(self,username, password):

    for row in self.cursor.execute('SELECT username FROM users'):

      if username == row[0]:
        print("That user already exists.")
        self.create_user()

    password = input("What would you like your password to be? >:")
    password_check = input("Please enter your password again >:")

    if password == password_check:
      hashed_password = pbkdf2_sha256.hash(password)
      user = username, hashed_password
      self.cursor.execute("INSERT INTO users (username, password) VALUES(?,?);",user)
      self.create_character()

    else:
      print("NO MATCH")
  

  def validate_user(self):
    username = input("Username >:")

    for user in self.cursor.execute('SELECT * FROM users'):

      if username.lower() == user[1]:
        password = input("Password >:")

        if pbkdf2_sha256.verify(password, user[2]):
          self.character_id = user[0]
          return

        else:
          print("Password Incorrect")
          password = input("Password >:")
      
      if username.lower() == "quit":
        break

    if username.lower() not in user[1]:
      print("User not found.")
      self.validate_user()

  
  def create_character(self):
    profession = input("What class do you choose?\n1. Warrior\n2. Healer\n3. Rogue\n>:").lower()

    if profession == "1" or profession == "warrior":
      profession_choice = input('''Barbarianism is the natural state of mankind. Civilization is unnatural. It is the whim of circumstance,\n and barbarianism must ultimately triumph. With blade and brute strength, the warrior glides over the battlefield.\nDo you wish to select "Warrior" as your profession? (yes or no).\n>:''')

      if profession_choice == "yes" or profession_choice == "y":
        profession_name = "Warrior"
        self.roll_stats(profession_name)

      elif profession_choice == "no" or profession_choice == "n":
        self.create_character()

      else:
        print("not a valid choice")
        self.create_character()

    if profession == "2" or profession == "healer":
      profession_choice = input('''Draped in holy robes and solidified with divine light,a healing touch eases weary allies.\nRestoring life from death and navigating the Realm through acts of mysticism.\nDo you wish to select "Healer" as your profession? (yes or no).\n>:''')

      if profession_choice == "yes" or profession_choice == "y":
        profession_name = "Healer"
        self.roll_stats(profession_name)

      elif profession_choice == "no" or profession_choice == "n":
        self.create_character()

      else:
        print("not a valid choice")
        self.create_character()

    if profession == "3" or profession == "rogue":
      profession_choice = input('''Armed in the way of tretchery, a thief prevails. With the aid of traps and nefarious\nintent this scoundrel takes advantage.\nDo you wish to select "Rogue" as your profession? (yes or no).\n>:''').lower()

      if profession_choice == "yes" or profession_choice == "y":
        profession_name = "Rogue"
        self.roll_stats(profession_name)

      elif profession_choice == "no" or profession_choice == "n":
        self.create_character()

      else:
        print("not a valid choice")
        self.create_character()

  def roll_stats(self,profession_name):
    i = 6

    while i > 0:
      Strength = random.randint(6, 19)
      Vitality = random.randint(6, 19)
      Knowledge = random.randint(6, 19)
      Luck = random.randint(6, 19)
      Wisdom = random.randint(6, 19)
      Courage = random.randint(6, 19)
      Agility = random.randint(6, 19)
      Sanity = random.randint(6, 19) 
      Personality = random.randint(6, 19)
      i -= 1

      table = [["Strength:",Strength,"Vitality:",Vitality],["Knowledge:",Knowledge,"Luck:",Luck],["Wisdom:",Wisdom,"Courage:",Courage],["Agility:",Agility,"Sanity:",Sanity],["Personality:",Personality]]
      
      print("            CHARACTER STATS             ")
      print(tabulate(table,tablefmt="pretty"))
      print(f"You have {i} Rolls left.")

      choice = input("Do you accept these stats? (yes or no)\n>:")

      if choice == "yes" or choice == "y":
        player = [profession_name,100,100,100,Strength,Vitality,Knowledge,Luck,Wisdom,Courage,Agility,Sanity,Personality,1,100,'False','Outside']
        
        self.cursor.execute("INSERT INTO player (Profession,HP,ST,MP,Strength,Vitality,Knowledge,Luck,Wisdom,Courage,Agility,Sanity,Personality,Level,Experience,is_dead,room_id) VALUES(?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?);",player)

        self.connection.commit()
        print("Your character has been created!")
        return

  def save_character(self,player_data):
        data = player_data
        
        for row in self.cursor.fetchall():
          self.cursor.executemany('UPDATE player SET playerID= ?,Profession= ?,HP= ?,ST= ?,MP= ?,Strength= ?,Vitality= ?,Knowledge= ?,Luck= ?,Wisdom= ?,Courage= ?,Agility= ?,Sanity= ?,Personality= ?,Level= ?,is_dead= ?,room_ID= ? WHERE playerID = ?', data[0],data[1],data[2],data[3],data[4],data[5],data[6],data[7],data[8],data[9],data[10],data[11],data[12],data[13],data[14],data[15],data[16],data[0])
        self.connection.commit()


 






  



